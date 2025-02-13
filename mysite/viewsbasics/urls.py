from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'viewsbasics'
urlpatterns = [
    path('', TemplateView.as_view(template_name='viewsbasics/index.html')),
    path('funktionally', views.funktionally),
    path('danger', views.danger),
    path('safer', views.safer),
    path('prettyurldata/<thing>', views.prettyurldata),
    path('bounce', views.bounce),
    path('icecream',views.Icecream.as_view()),
    path('icecream/<flavor>',views.Icecream.as_view()),  
    path('bigtext/',views.bigtext.as_view()),
    path('bigtext/<text>',views.bigtext.as_view()),
    path('color/',views.color.as_view()), 
    path('color/<color>',views.color.as_view()),
    path('BMI/<h>/<w>',views.BMI.as_view()),
    path('BMI/',views.BMI.as_view()),
    path('RPC/<p>/<int:r>',views.RPC.as_view()),
    path('RPC/',views.RPC.as_view()),
]
