from .models import Place, PlaceReservePeriod, Reserve, Category
from datetime import datetime
from django.utils import timezone
from .serializers import PlaceSerializer


def get_place_reservations(category_id, user, date=timezone.now()):
    category = Category.objects.get(id=category_id)
    places = Place.objects.filter(category=category)
    result = {}
    for place in places:
        place_serializer = PlaceSerializer(place)
        reserves_periods = PlaceReservePeriod.objects.filter(place=place)
        for data, period in zip(
            place_serializer.data["periods"], reserves_periods
        ):
            reserve = Reserve.objects.filter(
                reserve_period=period, date=date
            ).first()
            if reserve:
                if reserve.user == user:
                    data["status"] = "your reserve"
                else:
                    data["status"] = "reserved"
            else:
                data["status"] = "free"
        result[place.name] = place_serializer.data
    return result


def get_my_reserves(user, date=0):
    if not date:
        return Reserve.objects.filter(user=user)
    return Reserve.objects.filter(user=user, date=date)


def is_place_only_accessible_to_administrators(place):
    return place.only_administrators


def create_reservation(period, date, reason, user):
    return Reserve.objects.create(
        reserve_period=period, date=date, reason=reason, user=user
    )
