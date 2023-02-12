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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'smpl'
    players_per_group = None
    num_rounds = 15
    lottery_payoff_big = [100, 100, 50, 100, 100, 50, 100, 100, 50, 100, 100, 50, 100, 100, 50]
    lottery_payoff_small = [0, 50, 0, 0, 50, 0, 0, 50, 0, 0, 50, 0, 0, 50, 0]
    lottery_prob_big = [10, 10, 10, 25, 25, 25, 33, 33, 33, 50, 50, 50, 75, 75, 75]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    switching_point = models.IntegerField()
