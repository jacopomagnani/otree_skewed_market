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
    name_in_url = 'market_intro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    answer1 = models.IntegerField(
        choices=[
            [1, '150'],
            [2, '200'],
            [3, '250'],
            [4, '300']
        ],
        widget=widgets.RadioSelect
    )
