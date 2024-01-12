from api.models import Note
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource


class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization = Authorization()
        fields = ['title', 'body']
