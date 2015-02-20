class Notification:
    """
    Notification holds the information necessary to notify a user.

    Notifying a user requires at least one notification handler to be
    registered using `register_handler`.
    """
    handlers = {}

    @classmethod
    def register_handler(cls, **kwargs):
        """Register a notification handler."""
        cls.handlers.update(kwargs)
