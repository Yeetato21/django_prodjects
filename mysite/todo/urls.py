from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index.as_view(), name = 'index'),
    path('<int:pk>', views.detail.as_view(), name = 'detail'),
    path('add/',views.CreateView.as_view(), name = 'add'),
    path('delete/<int:pk>',views.DeleteView.as_view(), name = 'delete'),
]
