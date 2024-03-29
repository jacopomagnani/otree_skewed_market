from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'smpl'
    players_per_group = None
    num_rounds = 12
    lottery_payoff_big = [100, 100, 50, 100, 100, 50, 100, 100, 50, 100, 100, 50]
    lottery_payoff_small = [50, 0, 0, 50, 0, 0, 50, 0, 0, 50, 0, 0]
    lottery_prob_big = [2.5, 2.5, 2.5, 5, 5, 5, 25, 25, 25, 50, 50, 50]
    certain_payoff_big = [100, 100, 50, 100, 100, 50, 100, 100, 50, 100, 100, 50]
    certain_payoff_small = [50, 0, 0, 50, 0, 0, 50, 0, 0, 50, 0, 0]
    certain_payoff_step = [5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5]


class Subsession(BaseSubsession):

    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['mpl_paying_round'] = random.randint(1, Constants.num_rounds)
            p.participant.vars['mpl_paying_row'] = random.randint(1, 11)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    switching_point = models.IntegerField()
    score = models.IntegerField()

    def get_outcome(self):
        paying_round = self.participant.vars['mpl_paying_round']
        paying_row = self.participant.vars['mpl_paying_row']
        if self.round_number == paying_round:
            sure_payoffs = range(Constants.certain_payoff_big[self.round_number-1],
                                 Constants.certain_payoff_small[self.round_number - 1]-1,
                                 -Constants.certain_payoff_step[self.round_number - 1])
            if self.switching_point < sure_payoffs[paying_row - 1]:
                self.score = sure_payoffs[paying_row - 1]
            else:
                this_lottery_payoff_big = Constants.lottery_payoff_big[paying_round - 1]
                this_lottery_payoff_small = Constants.lottery_payoff_small[paying_round - 1]
                this_lottery_prob_big = Constants.lottery_prob_big[paying_round - 1]
                this_lottery_prob_small = 100 - Constants.lottery_prob_big[paying_round - 1]
                pay = random.choices([this_lottery_payoff_big, this_lottery_payoff_small],
                                     weights=[this_lottery_prob_big, this_lottery_prob_small], k=1)
                self.score = int(pay[0])
            self.payoff = c(self.score)
            self.participant.vars['mpl_score'] = self.score
