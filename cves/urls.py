from django.urls import path
from cves import views

urlpatterns = [
    path("cves/", views.cves, name="cves"),
]
