from django.contrib import admin
from django.urls import path, include
from frontend.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api/', include('api.urls')),
    path('demo/', include(('frontend.urls', 'frontend'), namespace='frontend')),
]
