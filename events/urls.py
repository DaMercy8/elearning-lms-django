from django.urls import path
from .views import (events, event_detail)

urlpatterns = [
	path('', events, name="events"),
	path('details/<int:id>', event_detail, name="details"),
]