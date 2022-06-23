from pyexpat import model
from rest_framework import viewsets
from .models import BlogpostModel
from .serialization import BlogpostSerializer


class BlogpostsView(viewsets.ModelViewSet):
    queryset = BlogpostModel.objects.all()
    serializer_class = BlogpostSerializer