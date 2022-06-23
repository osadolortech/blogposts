from rest_framework import routers
from .views import BlogpostsView

router = routers.DefaultRouter()
router.register('blogposts',BlogpostsView)