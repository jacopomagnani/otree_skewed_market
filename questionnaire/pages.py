from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Questionnaire_1(Page):
    form_model = 'player'
    form_fields = ['demographics_gender', 'demographics_age', 'demographics_field', 'demographics_traded']


class Questionnaire_2(Page):
    form_model = 'player'
    form_fields = ['crt_q1', 'crt_q2', 'crt_q3', 'crt_q4']
    timeout_seconds = 180

    def before_next_page(self):
        self.player.get_crt_outcome()


class Questionnaire_3(Page):
    form_model = 'player'
    form_fields = ['finance_q1', 'finance_q2', 'finance_q3', 'finance_q4', 'finance_q5']
    timeout_seconds = 180

    def before_next_page(self):
        self.player.get_finance_outcome()


class Results(Page):
    pass


page_sequence = [Questionnaire_1, Questionnaire_2, Questionnaire_3]
