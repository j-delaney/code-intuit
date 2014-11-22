from app import app, db
from flask import render_template_string


@app.route('/dev/data')
def main():
    # Delete all items
    users = db.User.find()
    questions = db.Question.find()
    all_items = list(users) + list(questions)
    for item in all_items:
        item.delete()

    create_users()
    create_questions()

    return render_template_string("It worked :)")

def create_questions():
    questions = [
        {'text': u'text','article': u'article','choices': [{'text': u'text1','correct': False},{'text': u'text2','correct': False},{'text': u'text3','correct': False},{'text': u'text4','correct': False}]},
        {'text': u'Joe works for a company that has a pretty nice 401(k) plan. His company will match 100% of the first 6% of pay the employee contributes to his 401(k). Joe earns $100,000 per year and this year he contributed $10,000. How much will his company match for him','article': u'retirement','choices': [{'text': u'$0','correct': False},{'text': u'$10,000','correct': False},{'text': u'$6,000','correct': True},{'text': u'$600','correct': False}]},
        {'text': u'Which of the following is true about the main difference between an IRA and a 401(k)?','article': u'retirement','choices': [{'text': u'IRAs are usually something you open personally while 401(k)s are provided by your company.','correct': True},{'text': u'IRAs are taxed when you deposit to them while 401(k) are not.','correct': False},{'text': u'IRAs are taxed when you deposit to them while 401(k) are not.','correct': False},{'text': u'All of the above are true.','correct': False}]},
        {'text': u'What is the primary advantage of a 401(k)?','article': u'retirement','choices': [{'text': u'The government will match your contributions to them.','correct': False},{'text': u'Dividends, capital gains, and interest are not taxed until disbursement.','correct': True},{'text': u'It increases by $401 every year.','correct': False},{'text': u'401(k)s will always grow no matter how the market is doing.','correct': False}]},
        {'text': u'What is the primary difference between a credit card and a debit card?','article': u'plastic','choices': [{'text': u'Debit cards allow for accrued debt that can be payed off over time.','correct': False},{'text': u'Credit cards must be payed off immediately.','correct': False},{'text': u'Debit cards directly use funds in your account while credit cards accrue debt that you must pay off.','correct': True},{'text': u'Debit cards can be used without a bank account.','correct': False}]},
        {'text': u'What is one of the risks involved in using plastic money over paper money?','article': u'plastic','choices': [{'text': u'It is easier to make excessive purchases when the physical exchange of money cannot be seen.','correct': True},{'text': u'The magnetic strips on plastic cards can be cancerous.','correct': False},{'text': u'Purchases using plastic money cannot be easily tracked.','correct': False},{'text': u'Using a credit card after it expires can result in jail-time.','correct': False}]},
        {'text': u'What is a major difference between charge cards and credit cards?','article': u'plastic','choices': [{'text': u'Charge cards automatically charge your bank account when making a purchase, while credit cards allow for debt accruement.','correct': False},{'text': u'Charge cards are government issued, while only credit cards can be issued without government approval.','correct': False},{'text': u'A credit cards differs from a charge card because "charge card" is just another term for debit card.','correct': False},{'text': u'A credit card allows for debt to be accrued for an elongated period of time, while the debt on a charge card must be paid in full by the end of the month.','correct': True}]},
        {'text': u'Which of the following would be an appropriate first car to buy?','article': u'expenditures','choices': [{'text': u'An expensive sports car','correct': False},{'text': u'An inexpensive truck with a low MPG','correct': False},{'text': u'A moderately-priced car','correct': True},{'text': u'An 18-wheeler','correct': False}]},
        {'text': u'True or False: It\'s not worth it to start saving up small amounts for college every week?','article': u'expenditures','choices': [{'text': u'TRUE','correct': False},{'text': u'FALSE','correct': True},{'text': u'','correct': False},{'text': u'','correct': False}]},
        {'text': u'Which of the following is a source you can use to pay for college?','article': u'expenditures','choices': [{'text': u'A state-sponsored grant system','correct': False},{'text': u'A 529 Plan','correct': False},{'text': u'Your personal savings account','correct': False},{'text': u'All of the above','correct': True}]},
        {'text': u'What is a major difference between receiving a bank loan and borrowing from a loan shark?','article': u'borrowing','choices': [{'text': u'Loan sharks are generally trustworthy and patient in regard to repayment schedules, while banks are strict and will ensure that they are paid in full.','correct': False},{'text': u'Loan sharks and banks have no major difference as the term "loan shark" is the title of a bank employee.','correct': False},{'text': u'Although banks are strict in regards to loan terms and repayment terms, loan sharks usually lend money with exorbitant interest rates and may turn use illegal means to ensure repayment.','correct': True},{'text': u'Loan sharks have government backing, while banks do not.','correct': False}]},
        {'text': u'What is the key difference between a subsidized and unsubsidized government loan?','article': u'borrowing','choices': [{'text': u'For a subsidized loan, the U.S. Department of Education pays the interest on the loan, while with an unsubsidized loan, the individual must pay the interest as well.','correct': True},{'text': u'Subsidized loans are for undergraduate students, while unsubsidized loans are for graduate students only.','correct': False},{'text': u'The amount borrowed for a subsidized loan is determined by the school, while the amount borrowed for an unsubsidized loan is determined by the government.','correct': False},{'text': u'No interest is due on an unsubsidized loan, while interest is due on a subsidized loan.','correct': False}]},
        {'text': u'The stress of borrowing from a friend money could degrade an otherwise strong relationship.','article': u'borrowing','choices': [{'text': u'TRUE','correct': True},{'text': u'FALSE','correct': False},{'text': u'','correct': False},{'text': u'','correct': False}]},
        {'text': u'What most accurately describes a person who is budget-conscious?','article': u'budgeting','choices': [{'text': u'An individual who frequently shops at expensive stores weekly.','correct': False},{'text': u'An individual who checks their bank account before deciding whether or not to make a purchase.','correct': True},{'text': u'An individual who spends more than they have in income.','correct': False},{'text': u'An individual who gives money away.','correct': False}]},
        {'text': u'What best describes the outcome of a well-designed budget?','article': u'budgeting','choices': [{'text': u'increased stress','correct': False},{'text': u'reduced savings','correct': False},{'text': u'inability to spend money on activities with friends','correct': False},{'text': u'decreased stress, increased savings, money to spend on memorable moments','correct': True}]},
        {'text': u'You are about to plan to a budget, should you start early or wait to plan a budget when you have a greater source of income?','article': u'budgeting','choices': [{'text': u'Start early','correct': True},{'text': u'Wait it out','correct': False},{'text': u'','correct': False},{'text': u'','correct': False}]},
        {'text': u'Which of the following would be considered taxable income?','article': u'income','choices': [{'text': u'child income','correct': False},{'text': u'certain veterans benefit','correct': False},{'text': u'life insurance proceeds','correct': False},{'text': u'interest and dividends','correct': True}]},
        {'text': u'What is the difference between a withholding tax and a retention tax?','article': u'income','choices': [{'text': u'Withholding taxes can apply to rent, sale of real estate, and royalties, retention taxes do not.','correct': False},{'text': u'Withholding taxes and retention taxes are the same thing.','correct': True},{'text': u'Withholding taxes apply to employment income, while retention taxes only apply to payments of interest or dividends.','correct': False},{'text': u'Withholding taxes are applied by the federal government, while retention taxes are applied by the local government.','correct': False}]},
        {'text': u'True or False: Income tax strictly refers to the income of a taxpayer?','article': u'income','choices': [{'text': u'TRUE','correct': False},{'text': u'FALSE','correct': True},{'text': u'','correct': False},{'text': u'','correct': False}]}
    ]

    for question in questions:
        new_q = db.Question()
        new_q.text = question['text']
        new_q.article = question['article']
        new_q.choices = question['choices']
        new_q.save()


def create_users():
    users = [
        {'username': u'j', 'password': u'j'},
        {'username': u'aaron', 'password': u'aaron'},
        {'username': u'ryan', 'password': u'ryan'},
    ]

    for user in users:
        new_user = db.User()
        new_user.username = user['username']
        new_user.password = user['password']
        new_user.save()
