from django.test import TestCase
from model_mommy import mommy   
from blog.models import Post, Tag, Subscriber
# Create your tests here.

class TagTestCase(TestCase):
    def setUp(self):
        self.django_tag = mommy.make(Tag, name="Django")
        self.python_tag = mommy.make(Tag, name="Python")

    def test_tag_creation(self):
        """Test Tag creation"""
        self.assertEqual(self.django_tag.__str__(), 'Django')
        self.assertEqual(self.python_tag.__str__(), 'Python')

class PostTestCase(TestCase):
    def setUp(self):
        self.tag = mommy.make(Tag, name="Django")
        self.post = mommy.make(Post, title="Django project")
        self.post.tags.set([self.tag])
    
    def test_post_creation(self):
        """Test post creation"""
        self.assertEqual(self.post.title, 'Django project')


class SubscriberTestCase(TestCase):
    def setUp(self):
        self.subscriber = mommy.make(Subscriber, email="johnnatan.barros@outlook.com")

    def test_subscription(self):
        """Test subscription"""
        self.assertEqual(self.subscriber.active, True)

    def test_unsubscription(self):
        """Test unsubscription"""
        self.subscriber.unsubscribe()
        self.assertEqual(self.subscriber.active, False)