from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new email succ"""
        email = 'nikola@gmail.com'
        password = 'nikola123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_norimalzied(self):

        email = 'nikola@GMAIL.COM'
        user = get_user_model().objects.create_user(
            email,
            'nikola123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None,
                'nikola123'
            )

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'nikola@gmail.com',
            'nikola123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)