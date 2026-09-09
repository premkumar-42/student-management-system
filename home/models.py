from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class StudentProfile(models.Model):
    student = models.OneToOneField(Students, on_delete=models.CASCADE, related_name="profile" )
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    profile_image = models.ImageField( upload_to="profile_images/", blank=True, null=True)


    def __str__(self):
        return self.student.name


class Teachers(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    age = models.IntegerField()
    experience = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Courses(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    fee = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Attendance(models.Model):

    student = models.ForeignKey(
        Students,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    status = models.BooleanField(default=True)

    def __str__(self):
        return self.student.name
    
class Marks(models.Model):

    student = models.ForeignKey(
        Students,
        on_delete=models.CASCADE
    )

    subject = models.CharField(max_length=100)

    marks = models.IntegerField()

    total_marks = models.IntegerField(default=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.subject}"
 
    
class StudentDocument(models.Model):
    student = models.ForeignKey(
        Students,
        on_delete=models.CASCADE
    )
    document = models.FileField(upload_to="documents/")

    def __str__(self):
        return self.student.name