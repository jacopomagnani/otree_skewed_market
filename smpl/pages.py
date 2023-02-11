from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Decide(Page):
    form_model = 'player'
    form_fields = ['switching_point']

    def vars_for_template(self):
        return dict(right_side_amounts=range(10, 21, 1))


class Results(Page):
    pass


page_sequence = [Decide, Results]