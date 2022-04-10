from rest_framework import serializers
from ..models import Event
from django.conf import settings


class EventSerializer(serializers.ModelSerializer):
    cpc = serializers.DecimalField(decimal_places=2,
                                   max_digits=10,
                                   default=0)
    cpm = serializers.DecimalField(decimal_places=2,
                                   max_digits=10,
                                   default=0)
    date = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Event
        fields = '__all__'


class NewEventSerializer(serializers.ModelSerializer):
    date = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Event
        fields = '__all__'


