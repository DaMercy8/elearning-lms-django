from django.urls import path, include
from .views import (
    UpdateCreatorProfileView,
    CreateCreatorProfileView
)

urlpatterns = [
    path('', CreateCreatorProfileView.as_view(), name='register-creator'),
    path('edit/<int:pk>/',UpdateCreatorProfileView.as_view(),name='edit-creator')
]