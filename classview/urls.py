from django.urls import path
from .views import TopicListView

app_name = 'classview'
urlpatterns = [
    path('', TopicListView.as_view(), name='topic-list')
]