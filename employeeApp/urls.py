from django.urls import include, re_path, path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html')),
    re_path(r'^department$', views.departmentAPI),
    re_path(r'^department/([0-9]+)$', views.departmentAPI), 
    re_path(r'^employee$', views.employeesAPI),
    re_path(r'^employee/([0-9]+)$', views.employeesAPI),
    re_path(r'^employee/savefile$', views.SaveFile), 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)