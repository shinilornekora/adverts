from rest_framework import fields, serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("title", "description", "link", "imgLink", "isForAdults", "isForeignNews", "tags",)