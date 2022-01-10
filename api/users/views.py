from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated

from .serializers import CustomUserSerializer
from . import constants
from formules import calories
from formules import fats
from formules import proteins
from formules import carbohydrates


class CustomUserView(APIView):
    """
    View for retrieving and editing user
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)

        return Response(serializer.data)

    def put(self, request):
        serializer = CustomUserSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class NutrientsRetrieveAPIView(APIView):
    """Represents amount of nutrients according option(gain, loss, maintain)"""
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        option = request.user.option
        calories_ = calories.daily_calories(request.user.current_weight,
                                            request.user.height,
                                            request.user.age)

        if option == options.MAINTAIN:
            carbohydrates_ = carbohydrates.carbohydrates_maintain(calories_)
            fats_ = fats.fats_maintain(calories_)
            proteins_ = proteins.proteins_maintain(calories_)

        elif option == options.LOSS:
            carbohydrates_ = carbohydrates.carbohydrates_loss(calories_)
            fats_ = fats.fats_loss(calories_)
            proteins_ = proteins.proteins_loss(calories_)

        elif option == options.GAIN:
            carbohydrates_ = carbohydrates.carbohydrates_gain(calories_)
            fats_ = fats.fats_gain(calories_)
            proteins_ = proteins.proteins_gain(calories_)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data={
            'calories': calories_,
            'carbohydrates': carbohydrates_,
            'fats': fats_,
            'proteins': proteins_,
        },
            status=status.HTTP_200_OK)
