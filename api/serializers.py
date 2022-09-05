from rest_framework import serializers
from api.models import Photo


class PhotoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ["id", "title", "date_created", "image", "user"]
