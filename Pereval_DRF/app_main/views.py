from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import generics
from .models import *
from .serializers import PerevalAddSerializer, CoordsSerializer


class PerevalAPIView(generics.CreateAPIView):
    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalAddSerializer

    def post(self, request):
        """POST запрос для добавления модели"""
        pereval = PerevalAddSerializer(data=request.data)
        try:
            if pereval.is_valid(raise_exception=True):
                pereval.save()
                data = {
                    'status': '200',
                    'message': 'null',
                    'id': f'{pereval.instance.id}'
                }
                return JsonResponse(data, status=200, safe=False)
        except Exception as exc:
            data = {
                'status': '400',
                'message': f'Bad Request: {exc}',
                'id': 'null'
            }
        return JsonResponse(data, status=400, safe=False)
