from django.db.models import Q
from django.http import HttpResponse
from .models import Students,Teachers,Courses,Attendance,Marks,StudentDocument
from django.shortcuts import redirect
from django.shortcuts import render, redirect,get_object_or_404
from students.forms import StudentForm,TeacherForm,CourseForm,AttendanceForm,MarksForm,StudentDocumentForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from students.forms import RegisterForm
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.utils import timezone


def about(request):
   return render(request,"about.html")

def contact(request):
   return render(request,'contact.html')


def user_login(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                "Login successful!"
            )

            return redirect("students_list")

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

    return render(request, "login.html")
 
 
def user_logout(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out."
    )

    return redirect("login")


def home(request):
    
    # --------------------------DAY 1---------------------------
    # print("Hello Prem")
    # return HttpResponse("Welcome to Django")
    # return render(request, "home.html")

   #------------------------------DAY 2----------------------
   
#    name="prem"
   # age=19
   # return render(request,"home.html",{"age":age})
   
   # --------------------------day 3 -------------------------
   
   # students=["prem","rahul","rohit","msd","kane"]
   # return render(request,'home.html',{"students":students})
   
   # name="prem kumar"
   # return render(request,'home.html',{"name":name})
   
   #  students=["prem","rahul","rohit","msd","kane"]
   #  return render(request,'home.html',{"students":students})
   
   username="prem kumar"
   return render(request,'home.html',{"username":username})

@login_required
@permission_required("home.add_students",raise_exception=True)
def add_students(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"student added succesfully")
            return redirect("students_list")

    else:
        form = StudentForm()

    return render(
        request,
        "add_students.html",
        {"form": form}
    )
    
@login_required
@permission_required("home.view_students", raise_exception=True)
def students_list(request):
    search = request.GET.get("search")

    if search:
        if search.isdigit():
            students = Students.objects.filter(
                Q(name__icontains=search) |
                Q(age=int(search))
            )
        else:
            students = Students.objects.filter(
                name__icontains=search
            )
    else:
        students = Students.objects.all()

    paginator = Paginator(students, 5)

    page_number = request.GET.get("page")

    students = paginator.get_page(page_number)

    return render(request, "list_students.html", {
        "students": students,
        "search": search
    })

@login_required
@permission_required("home.change_students", raise_exception=True)
def edit_student(request,id):
   students=Students.objects.get(id=id)
   
   if request.method == "POST":
      students.name = request.POST["name"]
      students.age = request.POST["age"]
      students.save()
      return redirect("students_list")
   
   return render(request,"edit_student.html",{"students":students})


@login_required
@permission_required("home.delete_students", raise_exception=True)
def delete_student(request, id):

    student = Students.objects.get(id=id)

    student.delete()

    return redirect("students_list")
 
 
 
 
@login_required
def student_detail(request,id):
   student = Students.objects.get(id=id)
   
   return render(request,"student_detail.html",{"student":student})



def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("students_list")

    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


@login_required
def add_teacher(request):

    if request.method == "POST":
        form = TeacherForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Teacher added successfully")
            return redirect("teachers_list")

    else:
        form = TeacherForm()

    return render(
        request,
        "add_teacher.html",
        {"form": form}
    )
 
@login_required
def teachers_list(request):
    subject = request.GET.get("subject")
    min_experience = request.GET.get("min_experience")

    teachers = Teachers.objects.all()

    if subject:
        teachers = teachers.filter(subject__iexact=subject)

    if min_experience:
        teachers = teachers.filter(experience__gte=min_experience)

    return render(request, "teachers_list.html", {
        "teachers": teachers,
        "subject": subject,
        "min_experience": min_experience
    })

@login_required
def dashboard(request):

    today = timezone.localdate()

    total_students = Students.objects.count()
    total_teachers = Teachers.objects.count()
    total_courses = Courses.objects.count()
    total_marks = Marks.objects.count()

    present_today = Attendance.objects.filter(
        date=today,
        status=True
    ).count()

    absent_today = Attendance.objects.filter(
        date=today,
        status=False
    ).count()

    recent_students = Students.objects.order_by("-created_at")[:5]

    return render(request, "dashboard.html", {
        "total_students": total_students,
        "total_teachers": total_teachers,
        "total_courses": total_courses,
        "total_marks": total_marks,
        "present_today": present_today,
        "absent_today": absent_today,
        "recent_students": recent_students,
    })
    
@login_required
def edit_teacher(request, id):

    teacher = Teachers.objects.get(id=id)

    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)

        if form.is_valid():
            form.save()
            return redirect("teachers_list")

    else:
        form = TeacherForm(instance=teacher)

    return render(
        request,
        "edit_teacher.html",
        {"form": form}
    )
    
@login_required
def delete_teacher(request, id):

    teacher = Teachers.objects.get(id=id)

    teacher.delete()

    return redirect("teachers_list")


@login_required
def teacher_detail(request, id):

    teacher = Teachers.objects.get(id=id)

    return render(
        request,
        "teacher_detail.html",
        {"teacher": teacher}
    )

@login_required 
def add_course(request):

    if request.method == "POST":
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("course_list")

    else:
        form = CourseForm()

    return render(request, "add_course.html", {"form": form})

@login_required
def course_list(request):

    courses = Courses.objects.all()

    return render(
        request,
        "course_list.html",
        {"courses": courses}
    )

@login_required
def edit_course(request, id):

    course = get_object_or_404(Courses, id=id)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)

        if form.is_valid():
            form.save()
            return redirect("course_list")

    else:
        form = CourseForm(instance=course)

    return render(
        request,
        "edit_course.html",
        {"form": form}
    )

@login_required
def delete_course(request, id):

    course = get_object_or_404(Courses, id=id)

    if request.method == "POST":
        course.delete()
        return redirect("course_list")

    return render(
        request,
        "delete_course.html",
        {"course": course}
    )
    
@login_required
def add_attendance(request):

    if request.method == "POST":

        form = AttendanceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("attendance_list")

    else:
        form = AttendanceForm()

    return render(
        request,
        "add_attendance.html",
        {"form": form}
    )

@login_required
def attendance_list(request):

    attendances = Attendance.objects.all().order_by("-date")

    return render(
        request,
        "attendance_list.html",
        {
            "attendances": attendances
        }
    )
 
@login_required   
def add_marks(request):

    if request.method == "POST":

        form = MarksForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Marks added successfully")
            return redirect("marks_list")

    else:
        form = MarksForm()

    return render(request, "add_marks.html", {"form": form})


@login_required
def marks_list(request):

    marks = Marks.objects.select_related("student").all()

    return render(
        request,
        "marks_list.html",
        {"marks": marks}
    )


@login_required    
def marks_detail(request, id):

    mark = get_object_or_404(Marks, id=id)

    return render(
        request,
        "marks_detail.html",
        {"mark": mark}
    )

@login_required
def edit_marks(request, id):

    mark = get_object_or_404(Marks, id=id)

    if request.method == "POST":

        form = MarksForm(request.POST, instance=mark)

        if form.is_valid():
            form.save()
            messages.success(request, "Marks updated successfully")
            return redirect("marks_list")

    else:
        form = MarksForm(instance=mark)

    return render(
        request,
        "edit_marks.html",
        {"form": form}
    )

@login_required
def delete_marks(request, id):

    mark = get_object_or_404(Marks, id=id)

    if request.method == "POST":
        mark.delete()
        messages.success(request, "Marks deleted successfully")
        return redirect("marks_list")

    return render(
        request,
        "delete_marks.html",
        {"mark": mark}
    )


@login_required
def upload_document(request):
    if request.method == "POST":
        form = StudentDocumentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Document uploaded successfully")
            return redirect("upload_document")

    else:
        form = StudentDocumentForm()

    return render(
        request,
        "upload_document.html",
        {"form": form}
    )