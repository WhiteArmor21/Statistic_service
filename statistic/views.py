from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers.event import *
from .models import Event
from django.db.models import F, DecimalField, ExpressionWrapper
from django.db.models.functions.comparison import NullIf


class RegistrationView(APIView):
    """View for registration new event"""
    permission_classes = (
        AllowAny,
    )
    request_body = NewEventSerializer
    serializer_class = NewEventSerializer

    def post(self, request, format=None):
        obj = NewEventSerializer(data=request.data)
        obj.is_valid(raise_exception=True)
        obj.save()
        return Response(status=status.HTTP_200_OK)


class GetEventsInfoView(APIView):
    """View for detailed info about events"""


    def get(self, request):
        order = request.GET.get("order", "date")
        from_date = request.GET.get("from", 0)
        to_date = request.GET.get("to", 0)

        queryset = Event.objects.all()

        if from_date != 0:
            queryset = queryset.filter(date__gte = from_date)
        if to_date != 0:
            queryset = queryset.filter(date__lte = to_date)

        queryset = queryset.annotate(
            cpc=ExpressionWrapper(F('cost') * 1.00 / NullIf(F('clicks'), 0),
                                  output_field=DecimalField())
        ).annotate(
            cpm=ExpressionWrapper(F('cost') * 1.00 / NullIf(
                F('views'),0) * 1000,
                                  output_field=DecimalField())
        ).order_by(order)


        serializer = EventSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer.data)


class DeleteEvents(APIView):
    permission_classes = (
        AllowAny,
    )

    def delete(self, request):
        Event.objects.all().delete()
        return Response(status=status.HTTP_200_OK)