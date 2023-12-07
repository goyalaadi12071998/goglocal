from django.urls import path
from . import controller


urlpatterns = [
    path('posts/', controller.create_new_post),
    path('posts/<int:id>/analysis', controller.analysis)
]
