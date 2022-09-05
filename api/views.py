from django.shortcuts import render

from rest_framework import generics, permissions, viewsets
from api.serializers import PhotoDetailSerializer
from api.models import Photo
from api.permissions import IsOwnerOrReadOnly, IsAdmin
from rest_framework import permissions, response, status
from rest_framework.decorators import action


class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoDetailSerializer
    queryset = Photo.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def update(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @action(methods=["POST", "DELETE"], detail=False, permission_classes=[IsAdmin])
    def delete_all(self, *args, **kwargs):
        self.get_queryset().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

