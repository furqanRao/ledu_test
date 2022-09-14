from .models import *
from django.contrib import admin


class UserActivitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'activity', 'reward', 'created_at')

    search_fields = ['user__username', 'activity']
    list_filter = [
                    'user', 'activity', 'created_at'
                ]

    actions = ["export_as_csv"]


admin.site.register(UserActivities, UserActivitiesAdmin)
