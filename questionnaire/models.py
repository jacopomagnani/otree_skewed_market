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
            'question': 'What is your gender?',
            'answers': ['Female', 'Male', 'Prefer not to say']
        },
        {
            'question': 'What is your age?',
            'answers': range(18, 45)
        },
        {
            'question': 'What is your field of study?',
            'answers': ['Science, Technology, Engineering and Maths',
                        'Humanities',
                        'Social sciences',
                        'Business, Finance and Economics']
        },
        {
            'question': 'Have you ever traded any stocks or other financial securities?',
            'answers': ['Yes',
                        'No']
        },
    ]
    crt_questions = [
        {
            'question': 'If it takes 10 mechanics 10 hours to fix 10 cars, how long would it take 80 mechanics to fix 80 cars? (Answer in hours)',
            'correct_answer': 10
        },
        {
            'question': 'A table and a chair cost $150 in total. The table costs 100 dollars more than the chair. How much does the chair cost? (Answer in dollars)',
            'correct_answer': 25
        },
        {
            'question': 'In the zoo, the lions eat one ton of meat every 6 weeks, and the tigers eat another ton of meat every 12 weeks, how long would it take them (lions and tigers) to eat one ton of meat together? (Answer in weeks)',
            'correct_answer': 4
        },
        {
            'question': 'John obtained the 25th fastest mark and the 25th slowest mark in a race. How many people participated in the race?',
            'correct_answer': 49
        }
    ]
    finance_questions = [
        {
            'question': 'Suppose you had $100 in a savings account and the interest rate was 2% per year. After 5 years, how much do you think you would have in the account if you left the money to grow?',
            'answers': ['More than $102', 'Exactly $102', 'Less than $102', 'Don’t know', 'Refuse to answer'],
            'correct_answer': 'More than $102'
        },
        {
            'question': 'Imagine that the interest rate on your savings account was 1% per year and inflation was 2% per year. After 1 year, with the money in this account, would you be able to buy…',
            'answers': ['More than today', 'Exactly the same as today', 'Less than today', 'Don’t know',
                        'Refuse to answer'],
            'correct_answer': 'Less than today'
        },
        {
            'question': 'If interest rates rise, what will typically happen to bond prices?',
            'answers': ['They will rise', 'They will fall', 'They will stay the same',
                        'There is no relationship between bond prices and the interest rate', 'Don’t know',
                        'Prefer not to say'],
            'correct_answer': 'They will fall'
        },
        {
            'question': 'A 15-year mortgage typically requires higher monthly payments than a 30-year mortgage, but the total interest paid over the life of the loan will be less.',
            'answers': ['True', 'False', 'Don’t know', 'Prefer not to say'],
            'correct_answer': 'True'
        },
        {
            'question': 'Buying a single company’s stock usually provides a safer return than a stock mutual fund.',
            'answers': ['True', 'False', 'Don’t know', 'Prefer not to say'],
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
    demographics_age = models.IntegerField(
        label=Constants.demographics_questions[1]["question"],
        choices=Constants.demographics_questions[1]["answers"]
    )
    demographics_field = models.StringField(
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
