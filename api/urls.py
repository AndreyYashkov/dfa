from django.contrib import admin
from django.urls import path, include
from api.views import PhotoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("Photos", PhotoViewSet)


urlpatterns = router.urls


#    [
#    path('photo/create',PhotoCreateView.as_view()),
#    path('photolist/',PhotoListView.as_view()),
#    path('photo/detail/<int:pk>/', CrudlistView.as_view()),
# ]
