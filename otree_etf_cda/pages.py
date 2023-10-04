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
        state_probabilities = {k: v['prob_weight'] for k, v in config.states.items()}
        return {
            'asset_structure': json.dumps(config.asset_structure),
            'state_probabilities': json.dumps(state_probabilities)
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
        value_a = structure["X"]["payoffs"][self.group.state_a]
        value_b = structure["Y"]["payoffs"][self.group.state_b]
        value_c = structure["Z"]["payoffs"][0]
        final_cash = self.player.settled_cash / self.subsession.config.currency_scale
        return {
            'final_cash': final_cash,
            'A_payoff': value_a,
            'B_payoff': value_b,
            'C_payoff': value_c,
            'net_payoff': self.player.payoff - config.initial_points

        }


class FinalResult(Page):

    def is_displayed(self):
        return self.round_number == self.subsession.config.num_rounds

    def vars_for_template(self):
        return {
            'market_payoff': self.player.in_round(self.subsession.config.pay_round).payoff
        }



page_sequence = [Intro, Market, ResultsWaitPage, Results, FinalResult]