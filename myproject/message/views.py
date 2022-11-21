from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from contact.models import Contact
from message.models import Message
from message.serializers import MessageSerializer
from django.template.loader import get_template
from django.shortcuts import render
import random
import string

letters = string.ascii_lowercase
generated_otp = ''.join(random.choice(letters) for i in range(5))

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+15017122661',
         to='+15558675310'
     )

print(message.sid)

class MessageCreateView(GenericAPIView):
    template_name = 'message/compose.html'
    success_url = reverse_lazy('contact:list')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    # def post(self, request, pk=None):
    #     form = CreateForm(request.POST, request.FILES or None)

    #     if not form.is_valid():
    #         ctx = {'form': form}
    #         return render(request, self.template_name, ctx)

    #     # Add owner to the model before saving
    #     poll = form.save(commit=False)
    #     poll.owner = self.request.user
    #     poll.save()
    #     ch1 = Choice(poll= poll, choice= str(poll.choice1))
    #     ch1.save()
    #     ch2 = Choice(poll= poll, choice= str(poll.choice2))
    #     ch2.save()
    #     ch3 = Choice(poll= poll, choice= str(poll.choice3))
    #     ch3.save()
    #     ch4 = Choice(poll= poll, choice= str(poll.choice4))
    #     ch4.save()
    #     return redirect(self.success_url)
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data
        message = Message.objects.create(**validated_data)

        response = {
            'error': False,
            'data': self.get_serializer(message).data
        }

        return Response(response, status=status.HTTP_201_CREATED)


class MessageListView(GenericAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [permissions.AllowAny]
    

    def get(self, request, *args, **kwargs):
        messages = self.get_queryset()

        response = {
            'error': False,
            'data': self.get_serializer(messages, many=True).data
        }
        print(response['data'])
        template_path= 'message/list.html'
        template = get_template(template_path)
        return HttpResponse(template.render(response))
