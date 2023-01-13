from django.urls import path, include
from .views import (
    Blog,
    BlogCreate,
    BlogDetail,
    BlogView,
    BlogUpdate,
)

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('add/',BlogCreate.as_view(),name='add-blog'),
    path('read/<int:pk>/',BlogDetail.as_view(),name='detail-blog'),
    path('edit/<int:pk>/',BlogUpdate.as_view(),name='edit-blog'),
]
