from django.urls import path, include
from .views import *

urlpatterns = [
    # Спринт №1
    path('submitData', PerevalAPIView.as_view()),
    # Спринт №2
    path('submitData/<int:pk>/', PerevalDetail.as_view({'get': 'retrieve', 'patch': 'partial_update'})),
]