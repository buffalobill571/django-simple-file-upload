from django.conf.urls import url
from generate_qrcode import views


urlpatterns = [
    url(r'^upload/', views.upload_file),
    url(r'^success/', views.success),
]
