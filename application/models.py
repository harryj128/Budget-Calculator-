from application import db


# Tables for the Database User is one to many with Budget
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(20), nullable =False)
    email = db.Column(db.String(30), nullable =False)
    annual_salary = db.Column(db.Integer, nullable = False )
    budgets = db.relationship('Budget', backref = 'user')

    def __str__(self):
        return (f"{self.user_name} £{self.annual_salary} {self.email} {self.budgets}")

#Budget is one to many with Tasks
class Budget(db.Model):
    budget_id = db.Column(db.Integer, primary_key = True)
    max_budget = db.Column(db.Integer, nullable = False )
    budget_name = db.Column(db.String(20), nullable =False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable = False)
    items = db.relationship('Item', backref = 'budget')

    def __str__(self):
        return (f"{self.budget_name} £{self.max_budget} {self.user.user_name} {self.items}")


class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.String(20), nullable =False)
    item_desc = db.Column(db.String(30), nullable =True)
    item_amount = db.Column(db.Integer, nullable = False)
    income = db.Column(db.Boolean , nullable  = False)
    budget_id = db.Column(db.Integer, db.ForeignKey('budget.budget_id'), nullable = False)

    def __str__(self):
        #works out percentage of total budget for each item
        per_budget = (self.item_amount/self.budget.max_budget) * 100
        return (f"{self.item_name} £{self.item_amount} Income: {str(self.income)} {per_budget}%")


