from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def is_displayed(self):
        if self.subsession.round_number == 1:
            return True
        else:
            return False


class Quiz(Page):

    form_model = 'player'
    form_fields = ['answer']

    def answer_choices(self):

        choices = [[1, Constants.questions_list[self.subsession.round_number-1]["q1"]],
                   [2, Constants.questions_list[self.subsession.round_number-1]["q2"]],
                   [3, Constants.questions_list[self.subsession.round_number-1]["q3"]],
                   [4, Constants.questions_list[self.subsession.round_number-1]["q4"]], ]
        return choices

    def before_next_page(self):
        if self.subsession.round_number == Constants.num_rounds:
            self.player.get_outcome()


class Results(Page):

    def is_displayed(self):
        if self.subsession.round_number == Constants.num_rounds:
            return True
        else:
            return False

    def vars_for_template(self):
        questions = []
        i = 0
        for x in Constants.questions_list:
            i = i+1
            y = [x["q1"], x["q2"], x["q3"], x["q4"], x["correct_answer"], self.player.in_round(i).answer]
            questions.append(y)

        return {
            'questions': questions
        }


class MyWaitPage(WaitPage):
    def is_displayed(self):
        if self.subsession.round_number == Constants.num_rounds:
            return True
        else:
            return False


page_sequence = [Instructions, Quiz, Results, MyWaitPage]
