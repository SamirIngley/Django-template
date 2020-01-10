from django.urls import path
from journal.views import PageListView, PageDetailView, PageCreateView


urlpatterns = [
    path('', PageListView.as_view(), name='journal-list-page'),
    path('create/', PageCreateView.as_view(), name='new-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='journal-details-page'),
]
