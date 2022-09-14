from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserActivities
from .serializers import RegisterSerializer, CreateActivitySerializer, ActivityListSerializer

activity_rewards = {
    "sign_up": 50, "invite_friend": 20, "watch_video": 150,
    "like_video": 2, "comment_video": 4, "social_share": 50
}


class SignUpView(generics.CreateAPIView):
    """
        Register a user.
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ActivityView(APIView):
    permission_classes = (IsAuthenticated,)
    """
        Create Activity and List activities.
    """
    @staticmethod
    def get(request):
        snippets = UserActivities.objects.all()
        serializer = ActivityListSerializer(snippets, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        if not activity_rewards.get(request.data.get("activity")):
            return Response(
                data={"error": "Invalid activity(activity field is required)"},
                status=status.HTTP_409_CONFLICT
            )
        user = request.user
        serializer = CreateActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user, reward=activity_rewards.get(request.data.get("activity")))
            return Response(
                data={"message": "Success"},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data={"error": "Invalid Form!"},
                status=status.HTTP_400_BAD_REQUEST
            )
