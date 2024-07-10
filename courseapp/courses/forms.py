from django import forms

from courses.models import Course

# class CourseCreateForm(forms.Form):
#     title = forms.CharField(label ="kurs başlığı",
#                             required = True, error_messages = {
#                             "required" : "Kurs başlığı giriniz."},
#                             widget = forms.TextInput(attrs={"class": "form-control"}))
#     description = forms.CharField(widget = forms.Textarea(attrs={"class": "form-control"}))
#     imageUrl = forms.CharField(widget = forms.TextInput(attrs={"class": "form-control"}))
#     slug = forms.CharField(widget = forms.TextInput(attrs={"class": "form-control"}))

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'image' , 'slug']
        labels = {
            'title' : "Kurs başlığı",
            'description' : "Açıklama",
             }

        widgets = {
            "title" : forms.TextInput(attrs= { "class" : "form-control"}),
            "description" : forms.Textarea(attrs= { "class" : "form-control"}),
            }
        error_messages = {
            "title" : {
                "required" : "Kurs başlığı girmelisiniz.",
                "max_length" : "Maksimum 50 karakter"
            },
            "description" : {
                "required" : "Açıklama giriniz."
            }
        }


class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'image' , 'slug', 'categories','isActive']
        labels = {
            'title' : "Kurs başlığı",
            'description' : "Açıklama"
        }
 
        widgets = {
            "title" : forms.TextInput(attrs= { "class" : "form-control"}),
            "description" : forms.Textarea(attrs= { "class" : "form-control"}),
            "slug" : forms.TextInput(attrs= { "class" : "form-control"}),
            "categories" : forms.SelectMultiple(attrs= {"class" : "form.control"})
        }
        error_messages = {
            "title" : {
                "required" : "Kurs başlığı girmelisiniz.",
                "max_length" : "Maksimum 50 karakter"
            },
            "description" : {
                "required" : "Açıklama giriniz."
            }
        }

class UploadForm(forms.Form):
    image = forms.ImageField()