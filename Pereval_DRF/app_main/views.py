from rest_framework.response import Response

from .models import *
from rest_framework.views import APIView

from .serializers import PerevalAddSerializer


class PerevalListView(APIView):
   """Список всех перевалов"""

   def get(self, request):
      perevals = PerevalAdd.objects.all()
      serializer = PerevalAddSerializer(perevals, many=True)
      return Response(serializer.data)

   def post(self, request):
      pereval = PerevalAddSerializer(data=request.data)
      if pereval.is_valid():
         pereval.save()
         return Response(status=201)
      else:
         print("Ошибка валидизации данных")
         return Response(status=400)
