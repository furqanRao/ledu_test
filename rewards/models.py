from django.db import models
from django.contrib.auth.models import User
from datetime import date

activity_rewards = {
    "sign_up": 50, "invite_friend": 20, "watch_video": 150,
    "like_video": 2, "comment_video": 4, "social_share": 50
}


class UserActivities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    activity = models.CharField(max_length=255, blank=False, null=False,
                                default=activity_rewards["sign_up"])
    reward = models.IntegerField(default=0)
    created_at = models.DateField(default=date.today())

    def __str__(self):
        return f"User: {self.user.username} --- Activity: {self.activity}"
