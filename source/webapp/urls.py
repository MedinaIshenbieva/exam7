from django.urls import path
from django.views.generic import RedirectView

from webapp.views import (
    IndexView,
    PollCreateView,
    PollView,
    PollUpdateView,
    PollDeleteView,
    )
from webapp.views.choices import ChoiceCreateView, ChoiceUpdateView, ChoiceDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('polls/', RedirectView.as_view(pattern_name="index")),
    path('polls/add/', PollCreateView.as_view(), name="poll_add"),
    path('poll/<int:pk>/', PollView.as_view(template_name="polls/view.html"), name="poll_view"),
    path('poll/<int:pk>/update/', PollUpdateView.as_view(), name="poll_update_view"),
    path('poll/<int:pk>/delete/', PollDeleteView.as_view(), name="poll_delete_view"),
    path('poll/<int:pk>/choices/add/', ChoiceCreateView.as_view(), name="poll_choice_create"),
    path('choice/<int:pk>/update/', ChoiceUpdateView.as_view(), name="choice_update_view"),
    path('choice/<int:pk>/delete/', ChoiceDeleteView.as_view(), name="choice_delete_view"),
]
