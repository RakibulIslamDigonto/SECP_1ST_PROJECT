
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_profile.urls', namespace='my_profile')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('album/', include('my_album.urls', namespace='my_album'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
