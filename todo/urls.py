
from django.urls import path
from . import views
urlpatterns = [
    path('',views.mytodo, name='mytodo'),
    path('<int:todo_id>',views.tododelete, name='tododelete'),
]
