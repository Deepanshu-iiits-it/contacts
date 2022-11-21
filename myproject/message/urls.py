
from django.urls import path

from message.views import *
app_name='message'
urlpatterns = [
    # path('v1/create/',  view=BatchCreateView.as_view(), name='batch_create'),
    # path('/<int:id>/',  view=MessageDetailView.as_view(), name='message_fetch'),
    path('',  view=MessageListView.as_view(), name='message_list'),
    # path('v1/<int:id>/udpate/',  view=BatchUpdateView.as_view(), name='batch_update'),
    # path('v1/<int:id>/delete/',  view=BatchDeleteView.as_view(), name='batch_delete'),
]