from django.urls import path

from app.views import MyView

urlpatterns = [
    path("endpoint/", MyView.as_view()),
]
