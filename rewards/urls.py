from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='hello'),
    path('activity/', views.ActivityView.as_view(), name='activity'),
]
