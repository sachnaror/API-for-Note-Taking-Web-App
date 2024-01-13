
# Rest API for a Google Keep-like note-taking web app (along with Python Webpack Boilerplate). 

---------------------------------
If we do not need React or Vue, we can still use Webpack to help us compile ES6, SCSS, and do many other things (Many people do not know that!)
---------------------------------


With a proper config, Webpack can save time and let us quickly build modern web applications.

Django lets us more or less create them all in one fell swoop.

During API-ification, i used Authorization class with TastyPie is, in their words, great for development — but not suitable for actual deployment. The magic of TastyPie is that PUT, DELETE is already done. Try updating or deleting my first note by ending PUT or DELETE to http://localhost:8000/api/note/1/. It just works! That means, just like that: I created a working RESTful API.


## Lessons Learned


Limiting Fields : If I want to only send specific information about a resource, I can limit fields like so:

```
from tastypie.resources import ModelResource
from api.models import Note
from tastypie.authorization import Authorization
class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization = Authorization()
        fields = ['title', 'body']
```

Make sure to send the request to http://localhost:8000/api/note/, not http://localhost:8000/api/note. That trailing slash is important, since otherwise Django has to redirect me, losing the POST data.

Send that request and… it fails. We get back a 401, AKA Unauthorized. Yay!

TastyPie is protective of its models out of the box, and only allows reading, not modifying, the data. It’s an easy fix, though — import their basic Authorization class, and add it to our resource.

# api/resources.py

```
from tastypie.resources import ModelResource
from api.models import Note
from tastypie.authorization import Authorization
class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization = Authorization()
```
Now it works! Try the request, and we get back 201, AKA success! Yay!

---------------------
For Webpack
---------------------


## Available Scripts

In the project directory, you can run:

### `npm run start`

`npm run start` will launch a server process, which makes `live reloading` possible.

If you change JS or SCSS files, the web page would auto refresh after the change. Now the server is working on port 9091 by default, but you can change it in `webpack/webpack.config.dev.js`

### `npm run watch`

run webpack in `watch` mode.

### `npm run build`

Webpack would focus on minified bundles, lighter weight source maps, and optimized assets to improve load time.





<img width="1673" alt="image" src="https://github.com/sachnaror/API-for-Note-Taking-Web-App/assets/9551754/fed7c391-aa1c-45c1-a598-65fcc829d6ea">




