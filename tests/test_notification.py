from unittest import TestCase
from unittest.mock import MagicMock

from pigeon.notification import Notification


class TestNotification(TestCase):
    """Test the Notification class."""

    def setUp(self):
        self.pigeon_handler = MagicMock()

    def test_register_handler(self):
        """A custom handler can be registered with the Notification class."""
        Notification.register_handler(pigeon=self.pigeon_handler)
        expected_handlers = {'pigeon': self.pigeon_handler}
        self.assertEqual(Notification.handlers, expected_handlers)

    def test_notify(self):
        """The notification uses each registered handler to notify a user."""
        Notification.register_handler(pigeon=self.pigeon_handler)

        user = 'Test User'
        about = object()
        notification = Notification(about=about)
        notification.notify(user)

        self.pigeon_handler.assert_called_once_with(about, user)
