from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import decimal


class MyPage(Page):
    def vars_for_template(self):

        total_score = self.participant.vars['quiz_score'] + self.participant.vars['market_score'] + self.participant.vars['mpl_score']

        return {
            'fee': self.session.config['participation_fee'],
            'score': total_score,
            'score_in_currency': self.participant.payoff.to_real_world_currency(self.session),
            'payment': self.participant.payoff_plus_participation_fee,
        }


page_sequence = [MyPage]
