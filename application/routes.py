from application import app,db
from application.models import *
from application.forms import *
from flask import url_for, request, redirect, render_template

# Home
@app.route('/')
def home():
    return render_template('model.html')


#C - User
@app.route('/add_user' , methods = ['GET', 'POST'])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        user_name = form.user_name.data
        email = form.email.data
        annual_salary = form.annual_salary.data
        add_user = User(user_name = user_name, email = email, annual_salary =annual_salary)
        db.session.add(add_user)
        db.session.commit()
        return redirect(url_for('users'))
    return render_template('add_users.html', form = form)
#R - User
@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users = users)

#U - User
@app.route('/update_user/<int:user_id>' , methods = ['GET', 'POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    form = UserForm()
    if form.validate_on_submit():
        user_name = form.user_name.data
        email = form.email.data
        annual_salary = form.annual_salary.data
        user.user_name = user_name
        user.email = email
        user.annual_salary = annual_salary
        db.session.commit()
        return redirect(url_for('users'))
    form.user_name.data = user.user_name
    form.email.data = user.email
    form.annual_salary.data = user.annual_salary
    return render_template('add_users.html', form = form)
#D - User
@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    user = User.query.get(user_id)
    for budget in user.budgets:
        for item in budget.items:
            db.session.delete(item)
        db.session.delete(budget)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users'))

#C - Budget
@app.route('/add_budget' , methods = ['GET', 'POST'])
def add_budget():
    form = BudgetForm()
    users = User.query.all()
    for user in users:
        form.user_id.users.append((user.user_id, f'{user.user_name}'))
    if form.validate_on_submit():
        budget_name = form.budget_name.data
        max_budget = form.max_budget.data
        user_id = form.user_id.data
        add_budget = Budget(budget_name = budget_name, max_budget = max_budget, user_id =user_id)
        db.session.add(add_budget)
        db.session.commit()
        return redirect(url_for('budgets'))
    return render_template('add_budgets.html', form = form)
#R - Budget
@app.route('/budgets')
def budgets():
    budgets = Budget.query.all()
    return render_template('budgets.html', budgets = budgets)

@app.route('/budgets/<int:user_id>')
def budgets_specific(user_id):
    # Query the db for all budgets linked to a certain user
    budgets = Budget.query.filter_by(user_id = user_id)
    return render_template('budgets.html', budgets = budgets)

#U - Budget
@app.route('/update_budget/<int:budget_id>' , methods = ['GET', 'POST'])
def update_budget(budget_id):
    budget = Budget.query.get(budget_id)
    form = BudgetForm()
    users = User.query.all()
    for user in users:
        form.user_id.users.append((user.user_id, f'{user.user_name}'))
    if form.validate_on_submit():
        budget_name = form.budget_name.data
        max_budget = form.max_budget.data
        user_id = form.user_id.data
        budget.budget_name = budget_name
        budget.max_budget = max_budget
        budget.user_id = user_id
        db.session.commit()
        return redirect(url_for('budgets'))
    form.budget_name.data = budget.budget_name
    form.max_budget.data = budget.max_budget
    return render_template('add_budgets.html', form = form)

#D - Budget
@app.route('/delete_budget/<int:budget_id>')
def delete_budget(budget_id):
    budget = Budget.query.get(budget_id)
    for item in budget.items:
        db.session.delete(item)
    db.session.delete(budget)
    db.session.commit()
    return redirect(url_for('budgets'))


#C - Items
@app.route('/add_item' , methods = ['GET', 'POST'])
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        item_name = form.item_name.data
        item_desc = form.item_desc.data
        item_amount = form.item_amount.data
        income = form.income.data
        budget_id = form.budget_id.data
        add_item = Item(item_name = item_name, item_desc = item_desc, item_amount = item_amount, income = income, budget_id = budget_id )
        db.session.add(add_item)
        db.session.commit()
        return redirect(url_for('budgets'))
    return render_template('add_item.html', form = form)

#R - Items
@app.route('/items/<int:budget_id>')
def items_specific(budget_id):
     # Query the db for all items linked to a certain budget
    budget_name = Budget.query.get(budget_id)
    items = Item.query.filter_by(budget_id = budget_id)
    return render_template('items.html', items = items, budget_name = budget_name.budget_name )

#U - Items
@app.route('/update_item/<int:item_id>' , methods = ['GET', 'POST'])
def update_item(item_id):
    item = Item.query.get(item_id)
    form = ItemForm()
    budgets = Budget.query.all()
    for budget in budgets:
        form.budget_id.budgets.append((budget.budget_id, f'{budget.budget_name}'))
    if form.validate_on_submit():
        item_name = form.item_name.data
        item_desc = form.item_desc.data
        item_amount = form.item_amount.data
        income = form.income.data
        budget_id = form.budget_id.data
        item.item_name = item_name
        item.item_desc = item_desc
        item.item_amount = item_amount
        item.income = income
        item.budget_id = budget_id
        db.session.commit()
        return redirect(url_for('budgets'))
    form.item_name.data = item.item_name
    form.item_desc.data = item.item_desc
    form.item_amount.data = item.item_amount
    return render_template('add_item.html', form = form)
#D - Items
@app.route('/delete_item/<int:item_id>')
def delete_item(item_id):
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('budgets'))
