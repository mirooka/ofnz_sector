from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
UserModel = get_user_model()


class Shoe(models.Model):
    # Constants
    NAME_MAX_LENGTH = 25
    BOOTS = 'BOOTS'
    WORK_BOOTS = 'WORK_BOOTS'
    PLATFORM_HEELS = 'PLATFORM_HEELS'
    CONE_HEELS = 'CONE_HEELS'
    RUNNING_SHOES = 'RUNNING_SHOES'
    CLIMBING_SHOES = 'CLIMBING_SHOES'
    FLIP_FLOPS = 'FLIP_FLOPS'

    TYPES = [(x, x) for x in (BOOTS, WORK_BOOTS, PLATFORM_HEELS, CONE_HEELS, RUNNING_SHOES, CLIMBING_SHOES,
                              FLIP_FLOPS, )]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
    )
