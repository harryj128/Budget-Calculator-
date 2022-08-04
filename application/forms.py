from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

#The form classes for inputing and updating Users, Budgets and tasks

class UserForm(FlaskForm):
    user_name = StringField('Username', validators = [DataRequired(), Length(min = 1, max = 20)])
    email = StringField('Email', validators = [DataRequired(), Length(min = 1, max = 30)])
    annual_salary = IntegerField('Annual Salary')
    submit = SubmitField('Submit')

class BudgetForm(FlaskForm):
    budget_name = StringField('Budget name', validators = [DataRequired(), Length(min = 1, max = 20)])
    max_budget =  IntegerField('Max Budget')
    user_id = SelectField('User', choices =[])
    submit = SubmitField('Submit')

class ItemForm(FlaskForm):
    item_name = StringField('Item name', validators = [DataRequired(), Length(min = 1, max = 20)])
    item_desc = StringField('Description', validators = [Length(min = 1, max = 30)])
    item_amount = IntegerField('Amount')
    income = BooleanField()
    budget_id = SelectField('Budget', choices =[])
    submit = SubmitField('Submit')