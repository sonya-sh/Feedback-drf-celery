from rest_framework import serializers
from feedback.tasks import send_feedback_email_task

class FeedbackSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Email Address")
    message = serializers.CharField()

    def send_email(self):
        send_feedback_email_task.delay(
            self.validated_data["email"], self.validated_data["message"]
        )