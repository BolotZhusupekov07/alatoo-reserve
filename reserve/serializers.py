from rest_framework import serializers

from .models import Place, Reserve, PlaceReservePeriod, Category
from users.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class PlaceReservePeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceReservePeriod
        fields = ["id", "starting_time", "finishing_time"]


class ReserveSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    reserve_period = PlaceReservePeriodSerializer()

    class Meta:
        model = Reserve
        fields = ["id", "user", "date", "reserve_period", "reason"]


class PlaceSerializer(serializers.ModelSerializer):

    periods = PlaceReservePeriodSerializer(
        source="placereserveperiod_set", many=True
    )

    class Meta:
        model = Place
        fields = [
            "id",
            "name",
            "category",
            "rent_from",
            "rent_to",
            "slug",
            "periods",
        ]


class DateInputSerializer(serializers.ModelSerializer):
    date = serializers.DateField()

    class Meta:
        model = Reserve
        fields = ["date"]


class ReserveCreationSerializer(serializers.ModelSerializer):
    reason = serializers.CharField()

    class Meta:
        model = Reserve
        fields = ["reason"]
