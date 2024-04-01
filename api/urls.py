from django.urls import path

from api.views import FeedbackApiView

app_name = "api"

urlpatterns = [
    path("", FeedbackApiView.as_view(), name="feedback_api")
]
