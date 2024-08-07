from datetime import date, datetime, timezone
import os
import random
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required , user_passes_test
from courses.forms import CourseCreateForm, CourseEditForm, UploadForm
from .models import Course, Category, UploadModel
from django.core.paginator import Paginator




def index(request):
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Category.objects.all()


    return render(request, 'courses/index.html', {
         'categories': kategoriler,
         'courses': kurslar
     })

def isAdmin(user):
    return user.is_superuser


def upload(request):
    if request.method == "POST" :
        form = UploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            model = UploadModel(image = request.FILES["image"])
            model.save()
            return render(request, "courses/success.html")
    else:
        form = UploadForm()
    return render(request, "courses/upload.html" , {"form" : form})

@login_required()
def course_list(request):
    kurslar = Course.objects.all()

    return render(request, 'courses/course-list.html', {
         'courses': kurslar
     })

def course_edit(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        form = CourseEditForm(request.POST ,  request.FILES, instance = course )
        form.save()
        return redirect("course_list")
    else:
        form = CourseEditForm(instance=course)
    return render(request, "courses/course-edit.html", {"form": form})


def course_delete(request,id):
    course= get_object_or_404(Course, pk=id)

    if request.method == "POST":
        course.delete()
        return redirect("course_list")


    return render(request, "courses/course-delete.html", {"course":course})


def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q= request.GET["q"]
        kurslar = Course.objects.filter(isActive= True, title__contains = q ).order_by("date")
        kategoriler = Category.objects.all()

    else:
        return redirect("/search")
    
    paginator= Paginator(kurslar,5)
    page = request.GET.get('page',1)
    page_obj =paginator.page(page)

    return render(request, 'courses/list.html',{
        'categories': kategoriler,
        'page_obj': page_obj ,
    })



def details(request, slug):
    try: 
        course = Course.objects.get(slug= slug)
    except:
        raise Http404()
    context= {
        'course': course
    }
    return render(request, 'courses/details.html', context)

def getCoursesByCategory(request, slug):
    kurslar = Course.objects.filter(categories__slug = slug, isActive= True)
    kategoriler = Category.objects.all()

    

    return render(request, 'courses/index.html',{
        'categories': kategoriler,
        'courses': kurslar ,
        'secilikategori': slug
    })

@user_passes_test(isAdmin)
def create_course(request):
       
        if request.method == "POST":
            form = CourseCreateForm(request.POST , request.FILES)

            if form.is_valid():
                form.save()
                
                return redirect("/kurs")
        else:
            form = CourseCreateForm()

        return render(request, "courses/create-course.html", {"form": form})
   