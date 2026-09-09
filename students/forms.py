from django import forms
from home.models import Students,Teachers,Courses,Attendance,Marks,StudentDocument
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):

    class Meta:
        model = Students
        fields = "__all__"

        labels = {
            "name": "Student Name",
            "age": "Student Age"
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your name"
                    
                }
            ),

            "age": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your age"
                }
            )
        }
        
    def clean_name(self):
       name = self.cleaned_data["name"]

       if name.isdigit():
          raise forms.ValidationError(
            "Name cannot contain only numbers."
        )

       return name

    # 👇 4 spaces — inside StudentForm
    def clean_age(self):
        age = self.cleaned_data["age"]

        if age < 18 or age > 60:
            raise forms.ValidationError(
                "Age must be between 18 and 60."
            )

        return age
    
class RegisterForm(UserCreationForm):
     class Meta:
         model=User
         fields=["username","password1","password2"]
         


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teachers
        fields = "__all__"
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = "__all__"
        


class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = ["student", "date", "status"]
        
class MarksForm(forms.ModelForm):

    class Meta:
        model = Marks
        fields = ["student", "subject", "marks", "total_marks"]

        widgets = {
            "student": forms.Select(attrs={"class": "form-control"}),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter subject"
            }),
            "marks": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter marks"
            }),
            "total_marks": forms.NumberInput(attrs={
                "class": "form-control"
            }),
        }


class StudentDocumentForm(forms.ModelForm):
    class Meta:
        model = StudentDocument
        fields = ["student", "document"]




# from django import forms

# class StudentForm(forms.ModelForm):

#     name = forms.CharField(
#       label="Student Name",
#       initial="prem kumar",
#         max_length=100,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Enter your name"
#             }
#         )
#     )

#     age = forms.IntegerField(
#         widget=forms.NumberInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Enter your age"
#             }
#         )
#     )

#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Enter your email"
#             }
#         )
#     )
    
# password = forms.CharField(
#     widget=forms.PasswordInput(
#         attrs={
#             "class": "form-control",
#             "placeholder": "Enter your password"
#         }
#     )
# )

# description = forms.CharField(
#     widget=forms.Textarea(
#         attrs={
#             "class": "form-control",
#             "placeholder": "Enter your description",
#             "rows": 4,
#             "cols": 40
#         }
#     )
# )