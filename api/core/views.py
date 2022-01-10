import datetime

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core.serializers import ActivitySerializer, MealUserSerializer, ActivityUserSerializer, MealSerializer
from core.models import *


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class MealUserViewSet(viewsets.ModelViewSet):
    queryset = MealUser.objects.all()
    serializer_class = MealUserSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)

    @action(detail=False, methods=['GET'], name='today_meal')
    def today(self, request, pk=None):
        """Action for viewing today's meal list"""
        queryset = self.get_queryset().filter(date=datetime.datetime.today())
        serializer = MealUserSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class ActivityUserViewSet(viewsets.ModelViewSet):
    queryset = ActivityUser.objects.all()
    serializer_class = ActivityUserSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)
