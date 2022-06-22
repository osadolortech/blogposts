
from rest_framework import serializers
from .models import BlogpostModel

class BlogpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogpostModel
        fields =(
            'id','title','author','content','created_date'
        )