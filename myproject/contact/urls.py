
from django.urls import path

from contact.views import *
from message.views import *
app_name='contact'
urlpatterns = [
    path('/<int:id>/compose/',  view=MessageCreateView.as_view(), name='message_create'),
    path('/<int:id>/',  view=ContactDetailView.as_view(), name='contact_detail'),
    path('',  view=ContactListView.as_view(), name='contact_list'),
    # path('/<int:id>/udpate/',  view=ContactUpdateView.as_view(), name='contact_update'),
    # path('/<int:id>/delete/',  view=ContactDeleteView.as_view(), name='contact_delete'),
]