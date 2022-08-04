from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for
from application import app, db
from application.models import *
from application.forms import *

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test-inter.db',
            LIVESERVER_PORT = self.TEST_PORT,
            DEBUG = True,
            TESTING = True
        )

        return app

    def setUp(self):
        db.create_all()
        options = webdriver.chrome.options.Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(f'http://localhost:{self.TEST_PORT}/add_user')

    def tearDown(self):
        self.driver.quit()
        db.session.remove()
        db.drop_all()

    def test_server_connectivity(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}/add_user')
        assert response.status == 200


class TestAddUser(TestBase):
    def submit_input(self, test_case):
        user_name_field = self.driver.find_element_by_xpath('/html/body/div/form/input[1]')
        email_field = self.driver.find_element_by_xpath('/html/body/div/form/input[2]')
        annual_salary_field = self.driver.find_element_by_xpath('/html/body/div/form/input[3]')
        submit = self.driver.find_element_by_xpath('/html/body/div/form/input[4]')
        user_name_field.send_keys(test_case[0])
        email_field.send_keys(test_case[1])
        annual_salary_field.send_keys(test_case[2])
        submit.click()

    def test_add_task(self):
        test_case = ('Spaceman', 'horse@spacemane.com', '20000')
        self.submit_input(test_case)
        assert list(User.query.all()) != []
        assert User.query.filter_by(user_name="Spaceman").first() is not None
