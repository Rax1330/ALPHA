from django.contrib import admin
from django.urls import path
from TWO.views import CreateOrRetrieveView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/data/<str:msg>/', CreateOrRetrieveView.as_view(), name='create_or_retrieve'),
]
