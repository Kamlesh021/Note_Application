from django.contrib import admin
from django.urls import include,path


urlpatters=[
	path("admin/",admin.site.urls), 
	path("tasks/",include("notes_app.urls")),
]