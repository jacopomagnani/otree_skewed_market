from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1


class Decide(Page):
    form_model = 'player'
    form_fields = ['switching_point']

    def vars_for_template(self):
        return {'left_side_amounts': Constants.sure_payoffs,
                'lottery_payoff_big': Constants.lottery_payoff_big[self.round_number-1],
                'lottery_payoff_small': Constants.lottery_payoff_small[self.round_number - 1],
                'lottery_prob_big': Constants.lottery_prob_big[self.round_number - 1],
                'lottery_prob_small': 100-Constants.lottery_prob_big[self.round_number - 1]
                }

    def before_next_page(self):
        self.player.get_outcome()


class Results(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        paying_round = self.player.participant.vars['mpl_paying_round']
        paying_row = self.player.participant.vars['mpl_paying_row']
        return {
            'left_side_amounts': Constants.sure_payoffs[paying_row-1],
            'lottery_payoff_big': Constants.lottery_payoff_big[paying_round - 1],
            'lottery_payoff_small': Constants.lottery_payoff_small[paying_round - 1],
            'lottery_prob_big': Constants.lottery_prob_big[paying_round - 1],
            'lottery_prob_small': 100 - Constants.lottery_prob_big[paying_round - 1],
            'chosen_sure': (self.player.in_round(paying_round).switching_point < Constants.sure_payoffs[paying_row - 1]),
            'final_payoff': self.player.in_round(paying_round).score
        }


page_sequence = [Instructions, Decide, Results]
