from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import filters
from datetime import datetime
from .models import Event, Data, Form
from .serializers import EventSerializer, EventElementSerializer, EventFormSerializer, EventSerializerAll

class EventAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ['session_id', 'category']

    def get_queryset(self):

        queryset = Event.objects.all()

        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')

        if start is not None and end is not None:
            start = datetime.fromisoformat(str(start))
            end = datetime.fromisoformat(str(end))
            queryset = queryset.filter(timestamp__range=(start, end))
            return queryset
        return queryset

    def get_serializer_class(self):
        data = self.request.data

        if self.request.data:
            if "element" in data['data'][0]:
                return EventElementSerializer
            elif "form" in data['data'][0]:
                return EventFormSerializer
            else:
                return EventSerializer
        return EventSerializerAll
