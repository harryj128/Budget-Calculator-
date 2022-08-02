from application import app,db
from application.models import *
from flask import url_for, request, redirect, render_template

# Home

#C - User
#R - User
@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users', users = users)

#U - User
#D - User

#C - Budget
#R - Budget
@app.route('/budgets')
def budgets():
    budgets = Budget.query.all()
    return render_template('budgets', budgets = budgets)

@app.route('/budgets/<int:user_id>')
def budgets_specific(user_id):
    # need a line here to query the db for all budgets linked to a certain user
    budgets = Budget.query.get(user_id)
    return render_template('budgets', budgets = budgets)
#U - Budget
#D - Budget

#C - Items
#R - Items
@app.route('/items/<int:budget_id>')
def budgets_specific(budget_id):
     # need a line here to query the db for all items linked to a certain budget
    items = Item.query.get(budget_id)
    return render_template('items', items = items)
#U - Items
#D - Items