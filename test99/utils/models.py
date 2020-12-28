"""Django models utilities."""

#Django
from django.db import models

class UpdateModel(models.Model):
    """ Update base model to share create and update properties.
    This class provides every table with the following attributes:
        + created(DateTime): Store the datetime the object was created
        + modified (DateTime): Store the last datetime the objects was modified.
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now_add=True,
        help_text='Dime time on which the object was last modified.'
    )

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']