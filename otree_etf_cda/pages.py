from ._builtin import Page, WaitPage
from otree_markets.pages import BaseMarketPage
import json


class Intro(Page):

    def vars_for_template(self):
        config = self.subsession.config
        structure = config.asset_structure
        endowment_cash = self.player.cash_endowment()
        endowment_a = self.player.asset_endowment()["X"]
        endowment_b = self.player.asset_endowment()["Y"]
        endowment_c = self.player.asset_endowment()["Z"]
        return {
            'endowment_cash': endowment_cash,
            'endowment_A': endowment_a,
            'endowment_B': endowment_b,
            'endowment_C': endowment_c,
            'structure': structure
        }


class Market(BaseMarketPage):

    def is_displayed(self):
        return self.round_number <= self.subsession.config.num_rounds
    
    def vars_for_template(self):
        config = self.subsession.config
        return {
            'asset_structure': json.dumps(config.asset_structure),
        }
    

class ResultsWaitPage(WaitPage):

    def is_displayed(self):
        return self.round_number <= self.subsession.config.num_rounds
    
    after_all_players_arrive = 'set_payoffs'


class Results(Page):

    def is_displayed(self):
        return self.round_number <= self.subsession.config.num_rounds

    def vars_for_template(self):
        config = self.subsession.config
        structure = config.asset_structure
        value_x = structure["X"]["payoffs"][self.group.state_x]
        value_y = structure["Y"]["payoffs"][self.group.state_y]
        value_z = structure["Z"]["payoffs"][0]
        final_cash = self.player.settled_cash / self.subsession.config.currency_scale
        return {
            'final_cash': final_cash,
            'X_payoff': value_x,
            'Y_payoff': value_y,
            'Z_payoff': value_z
        }


class FinalResult(Page):

    def is_displayed(self):
        return self.round_number == self.subsession.config.num_rounds

    def vars_for_template(self):
        return {
            'pay_round': self.session.vars['market_paying_round'],
            'market_payoff': self.participant.vars['market_score']
        }

    def app_after_this_page(self, upcoming_apps):
        return upcoming_apps[0]


page_sequence = [Intro, Market, ResultsWaitPage, Results, FinalResult]