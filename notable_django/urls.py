from api.resources import NoteResource
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

note_resource = NoteResource()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(note_resource.urls)),
    path('', TemplateView.as_view(template_name="index.html")),
]
