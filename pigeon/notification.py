class Notification:
    """
    Notification holds the information necessary to notify a user.

    Notifying a user requires at least one notification handler to be
    registered using `register_handler`.
    """
    handlers = {}

    def __init__(self, about):
        """Store the object the notification is about."""
        self.about = about

    @classmethod
    def register_handler(cls, **kwargs):
        """Register a notification handler."""
        cls.handlers.update(kwargs)

    def notify(self, user):
        """Use all registered handlers to notify a user."""
        for handler in self.handlers.values():
            handler(self.about, user)
