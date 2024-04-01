from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from api.serializers import FeedbackSerializer

class FeedbackApiView(APIView):
    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({"detail": e.detail}, status=400)
        serializer.send_email()
        return Response({"detail": "Feedback sent successfully"}, status=201)
        