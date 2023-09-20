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
    num_rounds = 7
    questions_list = [{'q1': 'There are two safe assets (X and Y).',
                       'q2': 'There are three risky assets (X, Y and Z).',
                       'q3': 'There are two safe assets (X and Y) and a risky one (Z).',
                       'q4': 'There are two risky assets (X and Y) and a safe one (Z).',
                       'correct_answer': 4
                       },
                      {
                          'q1': 'The payoffs of the risky assets are not related.',
                          'q2': 'When the payoffs of Asset A is high then the payoff of Asset B is low.',
                          'q3': 'When the payoffs of Asset A is high then the payoff of Asset B is high.',
                          'q4': 'When the payoffs of Asset A is low then the payoff of Asset B is low.',
                          'correct_answer': 1
                      },
                      {
                          'q1': 'Your endowment in a round depends on your earnings in the previous round.',
                          'q2': 'Each round you start with a new endowment of cash and shares.',
                          'q3': 'Your cash in a round is impacted by your trading in the previous round.',
                          'q4': 'Your endowment in a round depends on the asset payoffs in the previous round.',
                          'correct_answer': 2
                      },
                      {
                          'q1': 'A trade occurs when a trader enters a bid greater than or equal to the lowest ask, or enters an ask lower than or equal to the highest bid.',
                          'q2': 'A trade occurs when a trader enters a bid lower than or equal to the lowest ask, or  enters an ask lower than or equal to the highest bid.',
                          'q3': 'A trade can only occur when a trader enters a bid that is equal to an ask.',
                          'q4': 'A trade can only occur when at least a bid and an ask have already been posted.',
                          'correct_answer': 1
                      },
                      {
                          'q1': 'A trade occurs when a trader clicks on a number in the trades column.',
                          'q2': 'A trade occurs when a trader clicks on Bid.',
                          'q3': 'A trade occurs when a trader clicks on Ask.',
                          'q4': 'A trade occurs when a trader double-clicks on a current ask or bid.',
                          'correct_answer': 4
                      },
                      {
                          'q1': 'Your available and settled amount of assets are always equal.',
                          'q2': 'Your settled amount of assets decreases when you place an ask.',
                          'q3': 'Your available amount of assets decreases when you place an ask.',
                          'q4': 'Your available amount of assets decreases when you place a bid.',
                          'correct_answer': 3
                      },
                      {
                          'q1': 'Your available and settled amount of cash are always equal.',
                          'q2': 'Your available cash decreases when you place a bid whereas your settled cash stays the same.',
                          'q3': 'Your settled cash decreases when you place a bid whereas your available cash stays the same.',
                          'q4': 'Your available cash increases when you place a bid.',
                          'correct_answer': 2
                      }
                      ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.IntegerField(
        widget=widgets.RadioSelect
    )

    num_correct = models.IntegerField()

    def get_outcome(self):
        k = 0
        for i in range(1, Constants.num_rounds):
            if self.in_round(i).answer == Constants.questions_list[i-1]["correct_answer"]:
                k = k + 1
        self.num_correct = k
