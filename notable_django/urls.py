from api.resources import NoteResource
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

note_resource = NoteResource()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(note_resource.urls)),
]
