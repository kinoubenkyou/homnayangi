from django.db.models import CharField, IntegerChoices, IntegerField, Model


class Place(Model):
    class PriceGroupChoices(IntegerChoices):
        UNKNOWN = 0, "unknown"
        TO_50 = 1, "lower 50k/person"
        FROM_50_TO_100 = 2, "50-100k/person"
        FROM_100_TO_200 = 3, "100-200k/person"
        FROM_200_TO_500K = 4, "200-500k/person"
        FROM_500_TO_1000 = 5, "500k-1m/person"
        FROM_1000 = 6, "upper 1m/person"

    address = CharField(unique=True)
    name = CharField(blank=True)
    price_group = IntegerField(choices=PriceGroupChoices)
