from rest_framework import serializers

from core.models import Activity, Meal, ActivityUser, MealUser


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class ActivityUserSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    activity = serializers.HyperlinkedRelatedField(view_name='activity-detail', read_only=True)

    class Meta:
        model = ActivityUser
        fields = '__all__'


class MealUserSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    meal = serializers.HyperlinkedRelatedField(view_name='meal-detail', read_only=True)

    class Meta:
        model = MealUser
        fields = '__all__'
