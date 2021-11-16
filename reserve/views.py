from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Place,
    Reserve,
    PlaceReservePeriod,
    Category,
    PlaceAdministrator,
)
from .serializers import (
    PlaceSerializer,
    ReserveSerializer,
    DateInputSerializer,
    PlaceReservePeriodSerializer,
    ReserveCreationSerializer,
    CategorySerializer,
)
from . import services

User = get_user_model()


class CategoryListView(ListAPIView):
    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryPlacesReservesListView(APIView):

    serializer_class = ReserveSerializer
    date_input_serializer_class = DateInputSerializer
    second_serializer_class = PlaceReservePeriodSerializer

    def get(self, request, pk):
        data = services.get_place_reservations(pk, request.user)
        return Response(data)

    def post(self, request, pk):
        serializer = self.date_input_serializer_class(data=request.data)
        if serializer.is_valid():
            date = serializer.data.get("date")
            data = services.get_place_reservations(pk, request.user, date)
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyReservesListView(APIView):
    serializer_class = ReserveSerializer
    date_input_serializer_class = DateInputSerializer

    def get(self, request):
        reserves = services.get_my_reserves(request.user)
        serializer = self.serializer_class(reserves, many=True)
        return Response(serializer.data)

    def post(self, request):
        date_input_serializer = self.date_input_serializer_class(
            data=request.data
        )
        if date_input_serializer.is_valid():
            date = date_input_serializer.data.get("date")
            reserves = services.get_my_reserves(request.user, date)
            serializer = self.serializer_class(reserves, many=True)
            return Response(serializer.data)
        return Response(
            date_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class MyReservesDetailView(APIView):
    def delete(self, request, reserve_id):
        reserve = get_object_or_404(Reserve, pk=reserve_id)
        reserve.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReserveCreateView(APIView):
    serializer_class = ReserveCreationSerializer
    reserve_serializer_class = ReserveSerializer
    period_serializer_class = PlaceReservePeriodSerializer

    def get(self, request, period_id, date, *args, **kwargs):
        period = get_object_or_404(PlaceReservePeriod, pk=period_id)
        if not is_place_only_accessible_to_administrators(period.place):
            data = self.period_serializer_class(period).data
            data["date"] = date
            return Response(data, status=status.HTTP_200_OK)
        return Response(data, status=status.HTTP_403_FORBIDDEN)

    def post(self, request, period_id, date, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            period = get_object_or_404(PlaceReservePeriod, pk=period_id)
            services.create_reservation(
                period, date, serializer.data.get("reason"), request.user
            )
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
