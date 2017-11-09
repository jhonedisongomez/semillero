from .serializers import SemillaSerializer
from .models import Semilla
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class ApiSemillaList(APIView):

    def get(self, request, format=None):
        semillas = Semilla.objects.all()
        serializer = SemillaSerializer(semillas, many=True)

        return Response(serializer.data)

    def post(selfm ,request, format=None):
        serializer = SemillaSerializer(data=request.query_params)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


