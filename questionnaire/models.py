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
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1
    demographics_questions = [
        {
            'question': 'Quel est votre genre?',
            'answers': ['Féminin', 'Masculin', 'Autre']
        },
        {
            'question': 'Quel est votre niveau d’étude?',
            'answers': ['Sans diplôme',
                        'Certificat des écoles',
                        'Brevet',
                        'BEP-CAP',
                        'Baccalauréat général ou professionel',
                        'Bac +2 - DEUG - IUT - DUT - BTS',
                        'Bac +3 - License',
                        'Bac + 4 = Maitrise',
                        'BAc +5 - Master - DESS - DEA',
                        'Plus de Bac +5 - Doctorat -Thèse']
        },
        {
            'question': 'Quelle est votre école si vous êtes étudiant? ("Autre" si vous n’êtes pas étudiant)',
            'answers': ['ECLyon',
                        'EMLyon',
                        'Fac de sciences économiques et gestion',
                        'ITECH',
                        'ISOSTEO',
                        'Autre']
        },
        {
            'question': 'Avez-vous déjà acheté des actions ou d’autres actifs financiers?',
            'answers': ['Oui',
                        'Non']
        },
    ]
    crt_questions = [
        {
            'question': 'S’il faut 10 mécaniciens pendant 10 heures pour réparer 10 voitures, combien de heures faudrait-il à 80 mécaniciens pour réparer 80 voitures?',
            'correct_answer': 10
        },
        {
            'question': 'Une table et une chaise coûtent 150 euros au total. La table coûte 100 euros de plus que la chaise. Combien d’euros coûte la chaise ?',
            'correct_answer': 25
        },
        {
            'question': 'Au zoo, les lions mangent une tonne de viande toutes les 6 semaines et les tigres une autre tonne de viande toutes les 12 semaines. Combien de semaines leur faudra-t-il (aux lions et aux tigres) pour manger une tonne de viande ensemble ? ',
            'correct_answer': 4
        },
        {
            'question': 'Jean a obtenu le 25ème temps le plus rapide et le 25ème temps le plus lent lors d’une course. Combien de personnes ont participé à cette course ?',
            'correct_answer': 49
        }
    ]
    finance_questions = [
        {
            'question': 'Supposons que vous ayez 100 euros sur un compte épargne et que le taux d’intérêt soit de 2 % par an. Au bout de 5 ans, combien pensez-vous avoir sur le compte si vous laissez l’argent fructifier ?',
            'answers': ['Plus de 102 euros', 'Exactement 102 euros', 'Moins de 102 euros', 'Ne sait pas', 'Refuse de répondre'],
            'correct_answer': 'Plus de 102 euros'
        },
        {
            'question': 'Imaginez que le taux d’intérêt sur votre compte épargne soit de 1 % par an et que l’inflation soit de 2 % par an. Au bout d’1 an, l’argent disponible sur ce compte vous permettra acheter...',
            'answers': ['Plus qu’aujourd’hui', 'Exactement la même chose qu’aujourd’hui', 'Moins qu’aujourd’hui', 'Ne sait pas', 'Refuse de répondre'],
            'correct_answer': 'Moins qu’aujourd’hui'
        },
        {
            'question': 'Quand les taux d’intérêt augmentent, que se passe-t-il généralement pour les prix des obligations?',
            'answers': ['Ils augmentent', 'Ils baissent', 'Ils restent inchangés',
                        'Il n’y a pas de relation entre le prix des obligations et le taux d’intérêt',
                        'Ne sait pas', 'Refuse de répondre'],
            'correct_answer': 'Ils baissent'
        },
        {
            'question': 'Un prêt hypothécaire sur 15 ans nécessite généralement des paiements mensuels plus élevés qu’un prêt hypothécaire sur 30 ans, mais le montant total des intérêts payés sur la durée du prêt sera moins élevé.',
            'answers': ['Vrai', 'Faux', 'Ne sait pas', 'Refuse de répondre'],
            'correct_answer': 'Vrai'
        },
        {
            'question': 'L’achat d’actions d’une seule société offre généralement un rendement plus sûr qu’un fonds commun de placement en actions.',
            'answers': ['Vrai', 'Faux', 'Ne sait pas', 'Refuse de répondre'],
            'correct_answer': 'False'
        }
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    demographics_gender = models.StringField(
        label=Constants.demographics_questions[0]["question"],
        choices=Constants.demographics_questions[0]["answers"]
    )
    demographics_level = models.StringField(
        label=Constants.demographics_questions[1]["question"],
        choices=Constants.demographics_questions[1]["answers"]
    )
    demographics_school = models.StringField(
        label=Constants.demographics_questions[2]["question"],
        choices=Constants.demographics_questions[2]["answers"]
    )
    demographics_traded = models.StringField(
        label=Constants.demographics_questions[3]["question"],
        choices=Constants.demographics_questions[3]["answers"]
    )
    crt_q1 = models.IntegerField(
        label=Constants.crt_questions[0]["question"]
    )
    crt_q2 = models.IntegerField(
        label=Constants.crt_questions[1]["question"]
    )
    crt_q3 = models.IntegerField(
        label=Constants.crt_questions[2]["question"]
    )
    crt_q4 = models.IntegerField(
        label=Constants.crt_questions[3]["question"]
    )
    finance_q1 = models.StringField(
        label=Constants.finance_questions[0]["question"],
        choices=Constants.finance_questions[0]["answers"]
    )
    finance_q2 = models.StringField(
        label=Constants.finance_questions[1]["question"],
        choices=Constants.finance_questions[1]["answers"]
    )
    finance_q3 = models.StringField(
        label=Constants.finance_questions[2]["question"],
        choices=Constants.finance_questions[2]["answers"]
    )
    finance_q4 = models.StringField(
        label=Constants.finance_questions[3]["question"],
        choices=Constants.finance_questions[3]["answers"]
    )
    finance_q5 = models.StringField(
        label=Constants.finance_questions[4]["question"],
        choices=Constants.finance_questions[4]["answers"]
    )

    crt_num_correct = models.IntegerField()
    finance_num_correct = models.IntegerField()

    def get_crt_outcome(self):
        k = 0
        if self.crt_q1 == Constants.crt_questions[0]["correct_answer"]:
            k = k + 1
        if self.crt_q2 == Constants.crt_questions[1]["correct_answer"]:
            k = k + 1
        if self.crt_q3 == Constants.crt_questions[2]["correct_answer"]:
            k = k + 1
        if self.crt_q4 == Constants.crt_questions[3]["correct_answer"]:
            k = k + 1
        self.crt_num_correct = k

    def get_finance_outcome(self):
        k = 0
        if self.finance_q1 == Constants.finance_questions[0]["correct_answer"]:
            k = k + 1
        if self.finance_q2 == Constants.finance_questions[1]["correct_answer"]:
            k = k + 1
        if self.finance_q3 == Constants.finance_questions[2]["correct_answer"]:
            k = k + 1
        if self.finance_q4 == Constants.finance_questions[3]["correct_answer"]:
            k = k + 1
        if self.finance_q5 == Constants.finance_questions[4]["correct_answer"]:
            k = k + 1
        self.finance_num_correct = k
