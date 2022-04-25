from django.db import models


# Create your models here.


class Tutor(models.Model):
    class Meta:
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutors'
    url = models.URLField(max_length=300, default="")
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    info = models.TextField(max_length=1024)
    image_url = models.URLField(max_length=300, default="")

    def __str__(self):
        return self.name


class TutorPhoneNumbers(models.Model):
    class Meta:
        verbose_name = 'Phone number of some tutor'
        verbose_name_plural = 'Phone numbers of some tutors'
    tutor = models.ForeignKey(Tutor, related_name="phones", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.phone


class Course(models.Model):
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    price = models.IntegerField(default=0)
    info = models.TextField(max_length=300)
    url = models.URLField(max_length=300, default="")
    tutors = models.ManyToManyField(Tutor, related_name="courses", through="CourseTutor")

    def __str__(self):
        return self.title


class CourseTutor(models.Model):
    class Meta:
        verbose_name = 'Course-Tutor'
        verbose_name_plural = 'Courses-Tutors'
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, blank=True, null=True)
    tutor = models.ForeignKey(
        Tutor, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=300)
    time = models.CharField(max_length=300)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.course.title} | {self.time} | {self.tutor.name}"


class Student(models.Model):
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=300)
    cash = models.FloatField(default=0)
    courses = models.ManyToManyField(CourseTutor, related_name="students", through="StudentCourseTutor")

    def __str__(self):
        return self.name


class StudentPhoneNumbers(models.Model):
    class Meta:
        verbose_name = 'Student and his phone number'
        verbose_name_plural = 'Students and their phone numbers'
    student = models.ForeignKey(Student, related_name="phones", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.phone


class StudentCourseTutor(models.Model):
    class Meta:
        verbose_name = 'Student and Course-Tutors'
        verbose_name_plural = 'Student and Course-Tutors'
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, null=True)
    course_tutor = models.ForeignKey(
        CourseTutor, on_delete=models.CASCADE, blank=True, null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} | {self.course_tutor}"


class Money(models.Model):
    class Meta:
        verbose_name = 'Money'
        verbose_name_plural = 'Money'
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    type = models.BooleanField(default=False)
    message = models.TextField(max_length=300)
    status = models.CharField(max_length=300)

    def __str__(self):
        return self.student, self.time
