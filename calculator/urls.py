from django.urls import path

from . import views

urlpatterns = [
    path('', views.Topview.as_view(), name="top"),
    path('calcu/', views.CalculatorView.as_view(), name="index"),
    path('calcu45/', views.CalcuView.as_view(), name="calcu45"),
]