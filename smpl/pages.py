from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1


class Attention(Page):

    def is_displayed(self):
        return self.subsession.round_number > 1


class Decide(Page):
    form_model = 'player'
    form_fields = ['switching_point']

    def vars_for_template(self):
        return {'left_side_amounts': range(Constants.certain_payoff_big[self.round_number-1],
                                           Constants.certain_payoff_small[self.round_number - 1]-1,
                                           -Constants.certain_payoff_step[self.round_number - 1]),
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
        sure_payoffs = range(Constants.certain_payoff_big[paying_round - 1],
                             Constants.certain_payoff_small[paying_round - 1] - 1,
                             -Constants.certain_payoff_step[paying_round - 1])
        return {
            'left_side_amounts': sure_payoffs[paying_row-1],
            'lottery_payoff_big': Constants.lottery_payoff_big[paying_round - 1],
            'lottery_payoff_small': Constants.lottery_payoff_small[paying_round - 1],
            'lottery_prob_big': Constants.lottery_prob_big[paying_round - 1],
            'lottery_prob_small': 100 - Constants.lottery_prob_big[paying_round - 1],
            'chosen_sure': (self.player.in_round(paying_round).switching_point < sure_payoffs[paying_row - 1]),
            'final_payoff': self.player.in_round(paying_round).score
        }


page_sequence = [Instructions, Attention, Decide, Results]
