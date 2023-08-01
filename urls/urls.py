from django.urls import include, path

from settings import settings

urlpatterns = [
                  path('api/v1', include('urls.api_v1')),
              ]
