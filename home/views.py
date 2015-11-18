import json

from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from rest_framework.generics import ListAPIView, RetrieveAPIView

from home.serializers import ImageSerializer
from .models import Images
from .webapis import movie_search


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def post(self, request, *args, **kwargs):

        # Api Ajax response
        if request.is_ajax() and request.POST.get("movieTitle") is not None:
            try:
                movie_title = request.POST.get("movieTitle")
            except ValueError:
                movie_title = None

            if movie_title:
                movie_info = movie_search(movie_title)
                # print(json.dumps(movie_info, indent=4))
            else:
                return print("User did not enter a title.")

            if movie_info:
                data = {
                    "movie_info": movie_info
                }
                return JsonResponse(data)
            else:
                return print("API response is null")
        else:
            pass


class ImagesListAPIView(ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer


class ImagesRetrieveAPIView(RetrieveAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
