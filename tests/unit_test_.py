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
