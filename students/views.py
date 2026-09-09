from django.shortcuts import render,redirect
from .forms import StudentForm
from django.http import HttpResponse
from home.models import Students

def home(request):
    return HttpResponse("Welcome to Student Management System")



def demo_form(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            
            form = StudentForm()
           

    else:
        form = StudentForm()

    return render(request, "demo_form.html", {"form": form})


# def demo_form(request):

#     if request.method == "POST":

#         form = StudentForm(request.POST)

#         if form.is_valid():

#             name = form.cleaned_data["name"]
#             age = form.cleaned_data["age"]

#             Students.objects.create(
#                 name=name,
#                 age=age
#             )

#             print("Student Saved Successfully")

#             form = StudentForm()

#     else:
#         form = StudentForm()

#     return render(request, "demo_form.html", {"form": form})


def student_edit(request, id):

    student = Students.objects.get(id=id)

    if request.method == "POST":

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("students_list")

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "student_edit.html",
        {"form": form}
    )