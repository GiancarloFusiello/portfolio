from django.views.generic import TemplateView
from rest_framework.generics import ListAPIView, RetrieveAPIView

from home.serializers import ImageSerializer
from .models import Images


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def post(self):

        return


class ImagesListAPIView(ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer


class ImagesRetrieveAPIView(RetrieveAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
