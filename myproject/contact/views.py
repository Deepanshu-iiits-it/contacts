
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from contact.models import Contact
from contact.serializers import ContactSerializer

from django.template.loader import get_template
from django.shortcuts import render

class ContactDetailView(GenericAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, id=None):
        contact = Contact.objects.get(id=id)

        if not contact:
            response = {
                'error': True,
                'message': f'Contact with {id} not found!'
            }

            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        response = {
            'error': False,
            'data': self.get_serializer(contact).data
        }
        print(response['data'])
        template_path= 'contact/detail.html'
        template = get_template(template_path)
        return HttpResponse(template.render(response))


class ContactListView(GenericAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        contacts = self.get_queryset()

        response = {
            'error': False,
            'data': self.get_serializer(contacts, many=True).data
        }
        print(response['data'])
        template_path= 'contact/list.html'
        template = get_template(template_path)
        return HttpResponse(template.render(response))
