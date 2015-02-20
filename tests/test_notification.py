from unittest import TestCase

from pigeon.notification import Notification
from .handlers import pigeon_handler


class TestNotification(TestCase):
    """Test the Notification class."""

    def test_register_handler(self):
        """A custom handler can be registered with the Notification class."""
        Notification.register_handler(pigeon=pigeon_handler)
        expected_handlers = {'pigeon': pigeon_handler}
        self.assertEqual(Notification.handlers, expected_handlers)
