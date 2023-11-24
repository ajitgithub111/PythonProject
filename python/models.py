from django.db import models
# Create your models here.


class pythonmodel(models.Model):
    student_id=models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender_choices = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = models.CharField(max_length=1, choices=gender_choices)

    # Contact Information
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    # Academic Information
    high_school_name = models.CharField(max_length=200)
    graduation_year = models.IntegerField()
    major = models.CharField(max_length=100)

    # Admission Details
    is_admitted = models.BooleanField(default=False)
    admission_date = models.DateField(blank=True, null=True)


    def get_absolute_url(self):
        return "/wcem/form/"