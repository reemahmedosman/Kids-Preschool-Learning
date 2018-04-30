
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^imageUpload$', views.ImageDetailsView.as_view())
]
