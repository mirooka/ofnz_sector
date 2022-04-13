from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
UserModel = get_user_model()


class AbstractModel(models.Model):
    NAME_MAX_LENGTH = 25
    MALE = 'Male'
    FEMALE = 'Female'
    KIDS = 'Kids'
    GENDER_TYPES = [(x, x) for x in (MALE, FEMALE, KIDS)]

    title = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    gender = models.CharField(
        max_length=max(len(x) for (x, _) in GENDER_TYPES),
        choices=GENDER_TYPES,
        default=MALE
    )
    picture = models.URLField(
        null=True,
        blank=True,
    )
    

class Shoes(AbstractModel):
    # Constants
    NAME_MAX_LENGTH = 25
    BOOTS = 'Boots'
    HEELS = 'Heels'
    SPORT_SHOES = 'Sport shoes'
    FLIP_FLOPS = 'Flip flops'

    TYPES = [(x, x) for x in (BOOTS, HEELS, SPORT_SHOES, FLIP_FLOPS,)]

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )


class Pants(AbstractModel):
    JEANS = 'Jeans'
    SHORTS = 'Shorts'
    TRACKSUIT = 'Tracksuit'
    PANTS = 'Pants'
    SKIRT = 'Skirt'

    TYPES = [(x, x) for x in (JEANS, SHORTS, TRACKSUIT, PANTS, SKIRT)]

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )


class Shirt(AbstractModel):
    T_SHIRT = 'T-shirt'
    SWEATSHIRT = 'Sweatshirt'
    SWEATER = 'Sweater'
    SHIRT = 'Shirt'
    TANK_TOP = 'Tank top'

    TYPES = [(x, x) for x in (T_SHIRT, SWEATSHIRT, SWEATER, SHIRT, TANK_TOP)]

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )


# class Underwear(AbstractModel):
#     BRIEFS = 'Briefs'
#     BOXERS = 'Boxers'
#     BRA = 'Bra'
#     THONG_BIKINI = 'Thong bikini'
#     BIKINI = 'Bikini'
#     CORSET = 'Corset'
#
#     TYPES = [(x, x) for x in (BRIEFS, BOXERS, BRA, THONG_BIKINI, BIKINI, CORSET)]
#
#     type = models.CharField(
#         max_length=max(len(x) for (x, _) in TYPES),
#         choices=TYPES,
#     )


class Hat(AbstractModel):
    STRAW_HAT = 'Straw hat'
    CYLINDER = 'Cylinder'
    WINTER_HAT = 'Winter hat'
    CAP = 'Cap'

    TYPES = [(x, x) for x in (STRAW_HAT, CYLINDER, WINTER_HAT, CAP)]

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )


# class Socks(AbstractModel):
#     SPORTS_SOCKS = 'Sports socks'
#     CASUAL_SOCKS = 'Casual socks'
#     WINTER_SOCKS = 'Winter socks'
#     TIGHTS = 'Tights'
#
#     TYPES = [(x, x) for x in (SPORTS_SOCKS, CASUAL_SOCKS, WINTER_SOCKS, TIGHTS)]
#
#     type = models.CharField(
#         max_length=max(len(x) for (x, _) in TYPES),
#         choices=TYPES,
#     )


class Jacket(AbstractModel):
    WINTER_JACKET = 'Winter jacket'
    SUMMER_JACKET = 'Summer jacket'
    LEATHER_JACKET = 'Leather jacket'
    VEST = 'VEST'

    TYPES = [(x, x) for x in (WINTER_JACKET, SUMMER_JACKET, LEATHER_JACKET, VEST)]

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )
