from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home.views import HomeView, ImagesListAPIView, ImagesRetrieveAPIView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),

    # API URLs
    url(r'^api/images/$', ImagesListAPIView.as_view(), name="images_api"),
    url(r'^api/images/(?P<pk>\d+)/$', ImagesRetrieveAPIView.as_view(), name="image_detail_api"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
