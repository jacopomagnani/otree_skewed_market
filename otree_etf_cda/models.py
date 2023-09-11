from otree.api import (
    models, BaseConstants
)
import random
from otree_markets import models as markets_models
from .configmanager import ETFConfig
from .bots import ETFMakerBot, pcode_is_bot


class Constants(BaseConstants):
    name_in_url = 'otree_etf_cda'
    players_per_group = None
    num_rounds = 3


class Subsession(markets_models.Subsession):

    @property
    def config(self):
        config_name = self.session.config['session_config']
        return ETFConfig.get(config_name, self.round_number)
    
    def asset_names(self):
        return list(self.config.asset_structure.keys())

    def do_grouping(self):
        ppg = self.config.players_per_group
        # if ppg is None, just use the default grouping where everyone is in one group
        if not ppg:
            return
        group_matrix = []
        players = self.get_players()
        for i in range(0, len(players), ppg):
            group_matrix.append(players[i:i+ppg])
        self.set_group_matrix(group_matrix)

    def creating_session(self):
        if self.round_number > self.config.num_rounds:
            return
        self.do_grouping()
        if self.config.bots_enabled:
            for group in self.get_groups():
                group.create_bots()
        self.group_randomly()
        return super().creating_session()


class Group(markets_models.Group):

    state_a = models.IntegerField()
    state_b = models.IntegerField()

    def get_player(self, pcode):
        if pcode_is_bot(pcode):
            return None
        else:
            return super().get_player(pcode)

    def create_bots(self):
        for asset_name, structure in self.subsession.config.asset_structure.items():
            if structure['is_etf']:
                ETFMakerBot.objects.create(
                    group=self,
                    profit=0,
                    etf_name=asset_name,
                    etf_composition=structure['etf_weights']
                )

    def period_length(self):
        return self.subsession.config.period_length
    
    def do_realized_state_draw(self):
        structure = self.subsession.config.asset_structure
        self.state_a = random.choices([0, 1], weights=structure["A"]["probabilities"], k=1)[0]
        self.state_b = random.choices([0, 1], weights=structure["B"]["probabilities"], k=1)[0]


    def set_payoffs(self):
        self.do_realized_state_draw()
        for player in self.get_players():
            player.set_payoff()

    def confirm_enter(self, order):
        super().confirm_enter(order)
        for bot in self.bots.all():
            bot.on_order_entered(order)

    def confirm_trade(self, trade):
        super().confirm_trade(trade)
        for bot in self.bots.all():
            bot.on_trade(trade)
    
    def confirm_cancel(self, order):
        super().confirm_cancel(order)
        for bot in self.bots.all():
            bot.on_order_canceled(order)


class Player(markets_models.Player):

    def check_available(self, is_bid, price, volume, asset_name):
        config = self.subsession.config
        structure = config.asset_structure[asset_name]
        if is_bid and config.allow_short_cash and self.available_cash - (price * volume) >= -config.short_limit_cash * config.currency_scale:
            return True
        elif not is_bid and structure['allow_short'] and self.available_assets[asset_name] - volume >= -structure['short_limit']:
            return True
        return super().check_available(is_bid, price, volume, asset_name)

    def asset_endowment(self):
        endowments = {}
        for asset_name, structure in self.subsession.config.asset_structure.items():
            endowment = structure['endowment']
            if isinstance(endowment, list):
                # calculate index into endowments mod length of endowment
                # this way if there are more players than the length of the array, we wrap back around
                index = (self.id_in_group-1) % len(endowment)
                endowments[asset_name] = int(endowment[index])
            else:
                endowments[asset_name] = int(endowment)
        return endowments
    
    def cash_endowment(self):
        config = self.subsession.config
        if isinstance(config.cash_endowment, list):
            index = (self.id_in_group-1) % len(config.cash_endowment)
            endowment = int(config.cash_endowment[index])
        else:
            endowment = int(config.cash_endowment)
        # rescale cash endowment by currency scale so that config cash endowment
        # can be in human-readable form
        return (endowment + config.loan_value) * config.currency_scale
    
    def set_payoff(self):
        config = self.subsession.config
        structure = config.asset_structure
        value_a = structure["A"]["mypayoffs"][self.group.state_a]
        value_b = structure["B"]["mypayoffs"][self.group.state_b]
        value_c = structure["C"]["mypayoffs"][0]
        self.payoff += value_a * self.settled_assets["A"] + value_b * self.settled_assets["B"] + value_c * self.settled_assets["C"]

        # add cash gains/losses
        self.payoff += (self.settled_cash / config.currency_scale) - config.loan_value

        if self.round_number != config.pay_round:
            self.participant.payoff -= self.payoff
