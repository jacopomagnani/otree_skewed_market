from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class Quiz(Page):

    form_model = 'player'
    form_fields = ['answer1']


class Results(Page):
    pass


class MyWaitPage(WaitPage):
    pass


page_sequence = [Instructions, Quiz, Results, MyWaitPage]
