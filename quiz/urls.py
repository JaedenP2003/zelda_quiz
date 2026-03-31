from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("quiz/", views.quiz_view, name="quiz"),
    path("result/", views.result_view, name="result"),
    path("character/<slug:slug>/", views.character_detail, name="character_detail"),
]