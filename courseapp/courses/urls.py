from django.http import HttpResponse
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('create-course', views.create_course, name="create_course"),
    path('search', views.search, name="search"),
    path('course-edit/<int:id>' , views.course_edit, name = "course_edit"), 
    path('upload', views.upload, name= "upload_image"),
    path('course-list', views.course_list, name = "course_list"),
    path('<slug:slug>', views.details, name= "course_details"),
    path('course-delete/<int:id>' , views.course_delete, name = "course_delete"),
   
    path('kategori/<slug:slug>', views.getCoursesByCategory, name='courses_by_category'),  
]
