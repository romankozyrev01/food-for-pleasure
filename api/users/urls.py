from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.CustomUserView.as_view()),
    path('nutrients/', views.NutrientsRetrieveAPIView.as_view())
]
