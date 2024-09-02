from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework_sim

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth.urls')),
    path('api/', include('blog_api.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
