from django.urls import path
from .views import base, post_detail

urlpatterns = [
    path('', base, name="base"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
]