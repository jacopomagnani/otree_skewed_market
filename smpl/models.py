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
    sure_payoffs = range(100, -1, -10)


class Subsession(BaseSubsession):

    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['mpl_paying_round'] = random.randint(1, Constants.num_rounds)
            p.participant.vars['mpl_paying_row'] = random.randint(1, 11)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    switching_point = models.IntegerField()

    def get_outcome(self):
        paying_round = self.participant.vars['mpl_paying_round']
        paying_row = self.participant.vars['mpl_paying_row']
        if self.round_number == paying_round:
            if self.switching_point < Constants.sure_payoffs[paying_row - 1]:
                self.payoff = c(Constants.sure_payoffs[paying_row - 1])
            else:
                this_lottery_payoff_big = Constants.lottery_payoff_big[paying_round - 1]
                this_lottery_payoff_small = Constants.lottery_payoff_small[paying_round - 1]
                this_lottery_prob_big = Constants.lottery_prob_big[paying_round - 1]
                this_lottery_prob_small = 100 - Constants.lottery_prob_big[paying_round - 1]
                pay = random.choices([this_lottery_payoff_big, this_lottery_payoff_small],
                                     weights=[this_lottery_prob_big, this_lottery_prob_small], k=1)
                self.payoff = c(int(pay[0]))
