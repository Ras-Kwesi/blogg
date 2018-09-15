import unittest
from app.models import Blog,Comments

class TestPitches(unittest.TestCase):

    def setUp(self):
        self.new_blog = Blog(title='Make it', pitch='We shall finish what we started')
        self.new_comment = Comments(comment = "There is no other way")

    def tearDown(self):
        Blog.query.delete()
        Comments.query.delete()

    def test_instance_variable(self):
        self.assertEquals(self.new_comment.comment, 'There is no other way')

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.query.all()) > 0)

    def test_get_comment(self):
        self.new_comment.save_comment()
        got_coments = Comments.get_comments(12)
        self.assertTrue(len(got_coments) == 0)



