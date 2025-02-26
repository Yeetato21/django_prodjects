from django.urls import path

from . import views

app_name = "Culinary"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("timeslot/<int:pk>/", views.TimeSlotDetail.as_view(), name="timeslot_detail"),
    path("reservation/<int:pk>/", views.ReserDetail.as_view(), name="reser_detail"),
]
