# aa/urls.py
from django.contrib import admin
from django.urls import path
from notes_app.views import add_task, view_tasks, home,update_tasks,delete_tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Set home view as root URL
    path('add/', add_task, name="add_task"),
    path('view/', view_tasks, name="view_tasks"),
    path('update/<int:id>/', update_tasks,name="update_tasks"),
    path("delete/<int:id>/", delete_tasks,name="delete_tasks"),
]
