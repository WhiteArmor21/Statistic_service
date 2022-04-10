from django.urls import path
from .views import *

urlpatterns = [
    path('', GetEventsInfoView.as_view(), name = 'events_main'),
    path('add/', RegistrationView.as_view()),
    path('delete/', DeleteEvents.as_view()),
]