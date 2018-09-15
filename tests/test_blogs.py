import unittest
from app.models import Blog, User
from flask_login import current_user
from app import db

class TestPitches(unittest.TestCase):

    def setUp(self):
        self.user_James = User(id = 12, username='Ras', pass_key='Sword', email='ras@sword.com')
        self.new_blog = Blog(title = 'Make it', pitch='We shall finish what we started')

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_instance_variables(self):
        self.assertEquals(self.new_blog.title,'Make it')
        self.assertEquals(self.new_blog.post,'We shall finish what we started')

    def test_save_blog(self):
        self.new_blog.save_post()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog(self):
        self.new_blog.save_blog()
        got_blog = Blog.get_blog(12)
        self.assertTrue(len(got_blog) == 1)