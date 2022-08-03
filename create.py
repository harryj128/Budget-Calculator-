from application import db
from application.models import *


db.drop_all()
db.create_all()

testuser = User(user_name = 'Cowboy', email ='cowboy@cowboy.com', annual_salary = 30000)
testbudget = Budget(max_budget = 15000, budget_name ='firstbudget', user_id = 1 )
testitem = Item(item_name = 'water', item_amount = 200, income = False, budget_id = 1  )

db.session.add(testbudget)
db.session.add(testuser)
db.session.add(testitem)
db.session.commit()