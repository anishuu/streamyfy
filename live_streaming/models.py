from django.db import models

class Plan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    plan_price = models.DecimalField(max_digits=10, decimal_places=2)
    plan_duration = models.PositiveIntegerField()  # Duration in days or months
    plan_type = models.CharField(max_length=50)


class UserAccount(models.Model):
    User_id = models.AutoField(primary_key=True)
    Password = models.CharField(max_length=100)
    Email_id = models.EmailField(unique=True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Address = models.TextField()
    Phone_number = models.CharField(max_length=15)
    Plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='users')  # Renamed to Plan

class Payment(models.Model):  # Renamed to Payment
    Transaction_id = models.CharField(primary_key=True, max_length=32)
    Payment_time = models.DateTimeField(auto_now_add=True)
    Payment_date = models.DateField()
    Payment_method = models.CharField(max_length=50)
    Amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    Plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='payments')  # Renamed to Plan
    User = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='payments')  # Renamed to User

class MovieTVShow(models.Model):
    Show_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Release_date = models.DateField()
    Description = models.TextField()
    Duration = models.PositiveIntegerField()  # Duration in minutes
    Views = models.PositiveIntegerField(default=0)
    Country = models.CharField(max_length=50)
    Rating = models.DecimalField(max_digits=3, decimal_places=1)
    Genre = models.CharField(max_length=50)
    Actor = models.CharField(max_length=100)
    Actress = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='movie_images/', null=True, blank=True)
    Video = models.FileField(upload_to='movie_videos/', null=True, blank=True)  # Field for video file

    # Add other fields as needed

class Watches(models.Model):
    User = models.ForeignKey(UserAccount, on_delete=models.CASCADE)  # Renamed to User
    Show = models.ForeignKey(MovieTVShow, on_delete=models.CASCADE)  # Renamed to Show
    Date = models.DateField()
 # Ensure no duplicate entries
    @classmethod
    def get_watch_history(cls, user):
        return cls.objects.filter(User=user)