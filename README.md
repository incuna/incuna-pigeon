# Incuna Pigeon

Incuna Pigeon abstracts the sending of notifications.

## Installation

    pip install incuna-pigeon

## Usage

To use Incuna Pigeon, you will need to define a notification handler for
each transport method. These handlers can be attached to a subclass of
`Notification`:

```python
>>> from pigeon.notification import Notification
>>> def pigeon_handler(notification):
...     print('Pigeon:', notification.pigeon_name)
...     print('Destination:', notification.destination)
...     print('Message:', notification.message)
...     print('From:', notification.user)
...
>>> class CustomNotification(Notification):
...     handlers = (pigeon_handler,)
>>> notification = CustomNotification(
...     user='Fred',
...     pigeon_name='Murphy',
...     destination="Jim's House",
...     message='Party at my house. 7pm Monday.',
... )
>>> notification.notify()
Pigeon: Murphy
Destination: Jim's House
Message: Party at my house. 7pm Monday.
From: Fred
```
