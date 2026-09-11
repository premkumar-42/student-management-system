from django.urls import path
from . import views
from home import views as home_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path("demo_form/", views.demo_form, name="demo_form"),
    
  path("add_students/",home_views.add_students, name="add_students"),
  path("students_list/",home_views.students_list,name="students_list"),
  path("edit_student/<int:id>/", home_views.edit_student, name="edit_student"),
  path("delete_student/<int:id>/",  home_views.delete_student, name="delete_student"),
  path("student_detail/<int:id>/",home_views.student_detail,name="student_detail"),
        
  path("add_teacher/", home_views.add_teacher, name="add_teacher"),
  path("teachers_list/",home_views.teachers_list,name="teachers_list"),
  path( "edit_teacher/<int:id>/",home_views.edit_teacher,name="edit_teacher"),
  path("delete_teacher/<int:id>/",home_views.delete_teacher,name="delete_teacher"),
  path("teacher_detail/<int:id>/",home_views.teacher_detail,name="teacher_detail"),
   
  path("add_course/", home_views.add_course, name="add_course"),
  path("course_list/", home_views.course_list, name="course_list"),
  path("edit_course/<int:id>/", home_views.edit_course, name="edit_course"),
  path("delete_course/<int:id>/", home_views.delete_course, name="delete_course"),
  
  path("add_attendance/",home_views.add_attendance,name="add_attendance"),
  path("attendance_list/",home_views.attendance_list,name="attendance_list"),
  
  path("add-marks/",home_views.add_marks,name="add_marks"),
  path("marks-list/",home_views.marks_list,name="marks_list"),
  path("marks-detail/<int:id>/",home_views.marks_detail,name="marks_detail"),
  path("edit-marks/<int:id>/",home_views.edit_marks,name="edit_marks"),
  path("delete-marks/<int:id>/",home_views.delete_marks,name="delete_marks"),
  
  path("upload-document/", home_views.upload_document, name="upload_document"),
  
]