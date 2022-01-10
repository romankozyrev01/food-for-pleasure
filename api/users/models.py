import datetime

from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from . import constants


class CustomUser(AbstractUser):
    """Customized user model, includes special fields such weight, height end et al."""
    height = models.FloatField(null=True)
    start_weight = models.FloatField(null=True)
    final_weight = models.FloatField(null=True)
    current_weight = models.FloatField(null=True)
    birthday = models.DateField(null=True)
    gender = models.CharField(choices=(('F', 'Female'), ('M', 'Male')), max_length=8, null=True)
    option = models.CharField(choices=(
        (constants.LOSS, 'Loss'), (constants.GAIN, 'Gain'), (constants.MAINTAIN, 'Maintain')),
                              max_length=8, null=False, default='M')

    @property
    def age(self) -> int:
        """Returns age in years"""
        return int((datetime.date.today() - self.birthday).days / 365)

    def __str__(self):
        return f"{self.username}"
