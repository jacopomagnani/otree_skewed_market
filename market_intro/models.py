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
    questions_list = [{'q1': 'Il existe deux actifs sans risques (X et Y).',
                       'q2': 'Il existe trois actifs risqués (X, Y et Z).',
                       'q3': 'Il y a deux actifs sans risques (X et Y) et un actif risqué (Z).',
                       'q4': 'Il y a deux actifs risqués (X et Y) et un actif sans risque (Z).',
                       'correct_answer': 4
                       },
                      {
                          'q1': 'Le rendement de l’actif X ne dépend pas du rendement de l’actif Y et vice versa.',
                          'q2': 'Lorsque le rendement de l’actif X est élevé, le rendement de l’actif Y est faible.',
                          'q3': 'Lorsque le rendement de l’actif X est faible, le rendement de l’actif Y est faible.',
                          'q4': 'Lorsque le rendement de l’actif X est élevé, le rendement de l’actif Y est élevé.',
                          'correct_answer': 1
                      },
                      {
                          'q1': 'Votre dotation initiale pour une période dépend de vos gains lors de la période précédente.',
                          'q2': 'À chaque période, vous commencez avec une nouvelle dotation en argent et en actifs.',
                          'q3': 'Votre gain au cours d’une période est influencé par vos transactions lors de la période précédente.',
                          'q4': 'Votre dotation pour une période dépend des gains des actifs lors de la période précédente.',
                          'correct_answer': 2
                      },
                      {
                          'q1': 'Une transaction a lieu lorsqu’un participant saisit une offre d’achat supérieure ou '
                                'égale à l’offre de vente la plus faible, ou saisit une offre de vente inférieure ou '
                                'égale à l’offre d’achat la plus élevée.',
                          'q2': 'Une transaction a lieu lorsqu’un participant saisit une offre d’achat inférieure ou égale à l’offre de vente la plus faible, ou saisit une offre de vente supérieure ou égale à l’offre d’achat la plus élevée.',
                          'q3': 'Une transaction ne peut avoir lieu que lorsqu’un participant entre une offre d’achat égale à une offre de vente.',
                          'q4': 'Une transaction ne peut avoir lieu que lorsqu’au moins une offre d’achat et une offre de vente ont déjà été saisies.',
                          'correct_answer': 1
                      },
                      {
                          'q1': 'Une transaction se produit lorsqu’un participant clique sur un nombre dans la colonne des transactions.',
                          'q2': 'Une transaction a lieu lorsqu’un participant clique sur une offre d’achat.',
                          'q3': 'Une transaction a lieu lorsqu’un participant clique sur une offre de vente.',
                          'q4': 'Une transaction a lieu lorsqu’un participant double-clique sur une offre d’achat ou sur une offre de vente.',
                          'correct_answer': 4
                      },
                      {
                          'q1': 'Votre nombre d’actifs disponibles et votre nombre d’actifs effectifs sont toujours égaux.',
                          'q2': 'Le nombre de vos actifs effectifs diminue lorsque vous placez une offre d’achat ou de vente.',
                          'q3': 'Le nombre de vos actifs disponibles diminue lorsque vous placez une offre d’achat.',
                          'q4': 'Le nombre de vos actifs disponibles diminue lorsque vous placez une offre de vente.',
                          'correct_answer': 3
                      },
                      {
                          'q1': 'Votre montant d’argent disponible et votre montant d’argent effectif sont toujours égaux.',
                          'q2': 'Votre montant d’argent disponible diminue lorsque vous faites une offre d’achat, tandis que votre montant d’argent effectif reste inchangé.',
                          'q3': 'Votre montant d’argent effectif diminue lorsque vous faites une offre d’achat, tandis que votre montant d’argent disponible reste inchangé.',
                          'q4': 'Votre montant d’argent disponible augmente lorsque vous faites une offre d’achat.',
                          'correct_answer': 2
                      }
                      ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    score = models.IntegerField()

    answer = models.IntegerField(
        widget=widgets.RadioSelect
    )

    num_correct = models.IntegerField()

    def get_outcome(self):
        k = 0
        for i in range(1, Constants.num_rounds + 1):
            if self.in_round(i).answer == Constants.questions_list[i - 1]["correct_answer"]:
                k = k + 1
        self.num_correct = k
        if self.num_correct == Constants.num_rounds:
            self.score = 100
        else:
            self.score = 0
        self.payoff = c(self.score)
        self.participant.vars['quiz_score'] = self.score
