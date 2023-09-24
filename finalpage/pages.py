from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import decimal


class MyPage(Page):
    def vars_for_template(self):
        # final_pay = decimal.Decimal(self.participant.payoff_plus_participation_fee)
        # final_pay = final_pay.quantize(decimal.Decimal('0.01'))
        # final_pay = final_pay.quantize(decimal.Decimal('0.1'), rounding='ROUND_UP')
        # final_pay = final_pay + self.session.config['participation_fee']
        return {
            'rate': self.session.config['real_world_currency_per_point'],
            'fee': self.session.config['participation_fee'],
            'total_payoff_in_currency': self.participant.payoff.to_real_world_currency(self.session),
            'raw_payment': self.participant.payoff_plus_participation_fee,
            # 'final_payment': final_pay
        }


page_sequence = [MyPage]
