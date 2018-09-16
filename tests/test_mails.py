import unittest
from app.models import User, Mailer
from flask_login import current_user
from app import db

class TestPitches(unittest.TestCase):

    def setUp(self):
        self.user_James = User(id = 12, username='Ras', pass_key='Sword', email='ras@sword.com')
        self.new_sub = Mailer(emails= 'r@s.com', name = "Ras")

    def tearDown(self):
        Mailer.query.delete()
        User.query.delete()

    def test_instance_variables(self):
        self.assertEquals(self.new_sub.emails,'r@s.com')
        self.assertEquals(self.new_sub.name,'Ras')

    def test_save_mail(self):
        self.new_sub.save_mail()
        self.assertTrue(len(Mailer.query.all()) > 0)

    def test_get_blog(self):
        self.new_sub.save_mail()
        got_blog = Mailer.get_email()
        self.assertTrue(len(got_blog) == 1)