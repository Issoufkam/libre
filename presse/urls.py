from django.urls import path
from . import views


urlpatterns = [
    path("recharge_compte/", views.recharge_compte, name="recharge_compte"),
    path("", views.home, name="home"),
    path("confirmation_recharge/", views.confirmation_recharge, name="confirmation_recharge"),
    path('echec_recharge/<str:message>/', views.echec_recharge, name='echec_recharge'),
]
