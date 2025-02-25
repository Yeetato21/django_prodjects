from django.urls import path

from . import views

app_name = "Culinary"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("<int:pk>/", views.TimeSlotDetail.as_view(), name="detail"),
    path("reserdetail/<int:pk>/", views.ReserDetail.as_view(), name="reser"),
]
