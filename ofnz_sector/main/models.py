from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
UserModel = get_user_model()


class Shoes(models.Model):
    # Constants
    NAME_MAX_LENGTH = 25
    BOOTS = 'BOOTS'
    HEELS = 'HEELS'
    SPORT_SHOES = 'SPORT_SHOES'
    FLIP_FLOPS = 'FLIP_FLOPS'

    TYPES = [(x, x) for x in (BOOTS, HEELS, SPORT_SHOES, FLIP_FLOPS,)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
    )


class Pants(models.Model):
    # Constants
    NAME_MAX_LENGTH = 25
    JEANS = 'JEANS'
    SHORTS = 'SHORTS'
    TRACKSUIT = 'TRACKSUIT'
    PANTS = 'PANTS'
    SKIRT = 'SKIRT'

    TYPES = [(x, x) for x in (JEANS, SHORTS, TRACKSUIT, PANTS, SKIRT)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
    )


class Shirt(models.Model):
    # Constants
    NAME_MAX_LENGTH = 25
    T_SHIRT = 'T-SHIRT'
    SWEATSHIRT = 'SWEATSHIRT'
    SWEATER = 'SWEATER'
    SHIRT = 'SHIRT'
    TANK_TOP = 'TANK TOP'

    TYPES = [(x, x) for x in (T_SHIRT, SWEATSHIRT, SWEATER, SHIRT, TANK_TOP)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
    )


class Underwear(models.Model):
    # Constants
    NAME_MAX_LENGTH = 25

    BRIEFS = 'BRIEFS'
    BOXERS = 'BOXERS'
    BRA = 'BRA'
    THONG_BIKINI = 'Thong bikini'
    BIKINI = 'BIKINI'
    CORSET = 'Corset'

    TYPES = [(x, x) for x in (BRIEFS, BOXERS, BRA, THONG_BIKINI, BIKINI, CORSET)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
    )


class Hat(models.Model):
    # Constants
    NAME_MAX_LENGTH = 25

    STRAW_HAT = 'Straw hat'
    CYLINDER = 'Cylinder'
    WINTER_HAT = 'Winter hat'
    CAP = 'Cap'

    TYPES = [(x, x) for x in (STRAW_HAT, CYLINDER, WINTER_HAT, CAP)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
    )


class Socks(models.Model):
    # Constants
    NAME_MAX_LENGTH = 25

    SPORTS_SOCKS = 'Sports socks'
    CASUAL_SOCKS = 'Casual socks'
    WINTER_SOCKS = 'Winter socks'
    TIGHTS = 'Tights'

    TYPES = [(x, x) for x in (SPORTS_SOCKS, CASUAL_SOCKS, WINTER_SOCKS, TIGHTS)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
    )


class Jacket(models.Model):
    # Constants
    NAME_MAX_LENGTH = 25
    WINTER_JACKET = 'Winter jacket'
    SUMMER_JACKET = 'Summer jacket'
    LEATHER_JACKET = 'Leather jacket'
    VEST = 'VEST'

    TYPES = [(x, x) for x in (WINTER_JACKET, SUMMER_JACKET, LEATHER_JACKET, VEST)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
    )
