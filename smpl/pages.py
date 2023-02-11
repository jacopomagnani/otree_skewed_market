from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Decide(Page):
    form_model = 'player'
    form_fields = ['switching_point']

    def vars_for_template(self):
        return {'left_side_amounts': range(100, -1, -10),
                'right_side_amount': 10,
                'lottery_payoff_big': Constants.lottery_payoff_big[self.round_number-1],
                'lottery_payoff_small': Constants.lottery_payoff_small[self.round_number - 1],
                'lottery_prob_big': Constants.lottery_prob_big[self.round_number - 1]
                }


class Results(Page):
    pass


page_sequence = [Decide, Results]