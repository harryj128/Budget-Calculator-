from urllib import response
from flask_sqlalchemy import SQLAlchemy
from application import app, db
from application.models import *

from flask import url_for
from flask_testing import TestCase


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test-db.db',
            WTF_CSRF_ENABLED = False,
            DEBUG = True,
            SECRET_KEY = 'OCANIEONAAVEADA'
        )
        return app

    def setUp(self):
        db.create_all()
        testuser = User(user_name = 'Cowboy', email ='cowboy@cowboy.com', annual_salary = 30000)
        testbudget = Budget(max_budget = 15000, budget_name ='firstbudget', user_id = 1 )
        testitem = Item(item_name = 'water', item_amount = 200, income = False, budget_id = 1  )
        db.session.add(testbudget)
        db.session.add(testuser)
        db.session.add(testitem)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestGets(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Budget Calculator', response.data)