from django.urls import path
from .views import (
    CategoryListView,
    CategoryPlacesReservesListView,
    MyReservesListView,
    MyReservesDetailView,
    ReserveCreateView,
)

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="categories-list"),
    path(
        "categories/<int:pk>/",
        CategoryPlacesReservesListView.as_view(),
        name="category-place-reserve-list",
    ),
    path(
        "categories/<int:pk>/<int:period_id>/<str:date>/",
        ReserveCreateView.as_view(),
        name="reserve-create",
    ),
    path(
        "my_reserves/", MyReservesListView.as_view(), name="my-reserves-list"
    ),
    path(
        "my_reserves/<int:reserve_id>/",
        MyReservesDetailView.as_view(),
        name="my-reserve-delete",
    ),
]
