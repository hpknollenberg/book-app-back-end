from django.db import models
from django.contrib.auth.models import User






class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return self.user.username
    

class Book(models.Model):
    authors = models.TextField()
    profiles = models.ManyToManyField(Profile, related_name="profile_books")
    title = models.TextField()
    image_link = models.TextField()

    def __str__(self):
        return self.title
    

class Review(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="review")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="review")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile} - {self.book}" 