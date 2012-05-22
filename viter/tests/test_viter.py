from django.utils import unittest
from django.contrib.auth.models import User
from django.core import mail
from ..viter import Viter

class ViterTestCase(unittest.TestCase):
    def setUp(self):
        self.viter = Viter()
        self.user1 = User.objects.create(username='test', email='test@test.com', first_name='John', last_name='Doe')
        self.user2 = User.objects.create(username='test2', email='test2@test.com', first_name='Jane', last_name='Doe')

    def tearDown(self):
        User.objects.all().delete()
    
    def test_generate(self):
        invitation = self.viter.generate(inviter=self.user1)
        self.assertEqual(invitation.inviter, self.user1)

        invitation = self.viter.generate()
        self.assertEqual(invitation.inviter, None)

    def test_register_usage(self):
        invitation = self.viter.generate(inviter=self.user1)

        self.assertTrue(self.viter.register_usage(invitation.hash))
        self.assertEqual(invitation.usages.count(), 1)

        self.assertTrue(self.viter.register_usage(invitation.hash))
        self.assertEqual(invitation.usages.count(), 2)

        self.assertTrue(self.viter.register_usage(invitation.hash, user=self.user2))
        self.assertEqual(invitation.usages.count(), 3)

        self.assertTrue(self.viter.register_usage(invitation.hash, user=self.user2))
        self.assertEqual(invitation.usages.count(), 4)

        self.assertFalse(self.viter.register_usage('Not Valid Hash'))

    def test_get(self):
        invitation = self.viter.generate(inviter=self.user1)

        self.assertEqual(invitation, self.viter.get(invitation.hash))

        self.assertEqual(self.viter.get('Not Valid Hash'), None)

    def test_send_by_mail(self):
        invitation1 = self.viter.generate(inviter=self.user1)
        invitation2 = self.viter.generate(inviter=self.user1, email='testmail@test.com')

        self.assertTrue(self.viter.send_by_mail(invitation1, email='test@test.com'))
        self.assertEqual(len(mail.outbox), 1)

        self.assertFalse(self.viter.send_by_mail(invitation1))
        self.assertEqual(len(mail.outbox), 1)

        self.assertTrue(self.viter.send_by_mail(invitation2, email='test@test.com'))
        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(mail.outbox[-1].to[0], 'test@test.com')

        self.assertTrue(self.viter.send_by_mail(invitation2))
        self.assertEqual(len(mail.outbox), 3)
        self.assertEqual(mail.outbox[-1].to[0], 'testmail@test.com')

        self.assertFalse(self.viter.send_by_mail(None))
        self.assertEqual(len(mail.outbox), 3)
