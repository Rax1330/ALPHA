from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer
from django.http import JsonResponse
from rest_framework.response import Response

class CreateOrRetrieveView(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def get(self, request, *args, **kwargs):
        # Extract the last part of the URL to set the message
        message = self.kwargs.get('msg')
        if message not in ['high', 'low']:
            return Response({"error": "Invalid URL parameter, use 'high' or 'low'."}, status=400)

        # Automatically create a new entry with each GET request
        id_status = MyModel.objects.count() + 1
        MyModel.objects.create(id_status=id_status, message=message)
        print(f"Created new entry with id_status: {id_status}, message: {message}")  # Debugging line

        return super().get(request, *args, **kwargs)

    def perform_create(self, serializer):
        id_status = MyModel.objects.count() + 1  # Incremental ID status
        message = self.kwargs.get('msg', 'default message')
        serializer.save(id_status=id_status, message=message)
