from urllib import response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete
from application import app, db
from application.models import *
from application.forms  import *

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
        testbudget2 = Budget(max_budget = 15000, budget_name ='secondbudget', user_id = 1 )
        testitem = Item(item_name = 'water', item_amount = 200, income = False, budget_id = 1  )
        db.session.add(testbudget , testbudget2)
        db.session.add(testuser)
        db.session.add(testitem)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestRead(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Budget Calculator', response.data)

    def test_users_read(self):
        response = self.client.get(url_for('users'))
        self.assert200(response)
        self.assertIn(b'Cowboy', response.data)

    def test_budget_read(self):
        response = self.client.get(url_for('budgets'))
        self.assert200(response)
        self.assertIn(b'firstbudget', response.data)

    def test_budget_read(self):
        response = self.client.get(url_for('items_specific', budget_id = 1))
        self.assert200(response)
        self.assertIn(b'water', response.data)

class  TestDelete(TestBase):
    def test_item_delete(self):
        response = self.client.get(url_for('delete_item', item_id = 1), follow_redirects = True)
        self.assert200(response)
        self.assertNotIn(b'water', response.data)

    def test_budget_delete(self):
        response = self.client.get(url_for('delete_budget', budget_id = 1), follow_redirects = True)
        self.assert200(response)
        self.assertNotIn(b'firstbudget', response.data)

    def test_user_delete(self):
        response = self.client.get(url_for('delete_user', user_id = 1), follow_redirects = True)
        self.assert200(response)
        self.assertNotIn(b'Cowboy', response.data)

class TestPosts(TestBase):
    def test_add_user(self):
        response = self.client.post(
            url_for('add_user'),
            data = dict(user_name = 'Robot',
            email ='robot@robot.com',
            annual_salary = 30000),
            follow_redirects = True
        )
        self.assert200(response)
        assert User.query.filter_by(user_name = 'Robot').first() is not None

    def test_update_user(self):
        response = self.client.post(
            url_for('update_user', user_id = 1),
            data = dict(user_name = 'Cowdoy',
            email ='cowboy@cowboy.com',
            annual_salary = 30000),
            follow_redirects = True
        )
        self.assert200(response)
        assert User.query.filter_by(user_name = 'Cowboy').first() is None
        assert User.query.filter_by(user_name = 'Cowdoy').first() is not None
#Budgets
    def test_add_budget(self):
        response = self.client.post(
            url_for('add_budget'),
            data = dict(max_budget = 3000, budget_name ='thirdbudget', user_id = 1 ),
            follow_redirects = True
        )
        self.assert200(response)
        assert Budget.query.filter_by( budget_name ='thirdbudget').first() is not None

    def test_update_budget(self):
        response = self.client.post(
            url_for('update_budget', budget_id = 1),
            data = dict(max_budget = 3000, budget_name ='update', user_id = 1 ),
            follow_redirects = True
        )
        self.assert200(response)
        assert Budget.query.filter_by(budget_name = 'firstbudget').first() is None
        assert Budget.query.filter_by(budget_name = 'update').first() is not None
#Items
    def test_add_item(self):
        response = self.client.post(
            url_for('add_item'),
            data = dict(item_name = 'electric', item_amount = 400, income = False, budget_id = 1),
            follow_redirects = True
        )
        self.assert200(response)
        assert Item.query.filter_by( item_name ='electric').first() is not None

    def test_update_item(self):
        response = self.client.post(
            url_for('update_item', item_id = 1),
            data = dict(item_name = 'update', item_amount = 3000, income = False, budget_id = 1 ),
            follow_redirects = True
        )
        self.assert200(response)
        assert Item.query.filter_by(item_name = 'water').first() is None
        assert Item.query.filter_by(item_name = 'update').first() is not None