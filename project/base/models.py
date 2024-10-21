from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.


class Book(models.Model):
    book_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=100,null=True,blank=True)
    author = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    cover_img = models.ImageField(upload_to="",blank=True,null=True,default="cover_book.png")
    publish_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
    def __str__(self):
        return f"{self.title} by {self.author}"

class Category(models.Model):
    category_id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"
    def __str__(self):
        return f"{self.name} "

class BookCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category")
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="Book")
  
    def __str__(self):
        return f"{self.book} in {self.category} "

class Tag(models.Model):
    tag_id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=255,null=True,blank=True)
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
    def __str__(self) :
        return f"{self.name}"
class BookTag(models.Model):
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE,related_name="Tag")
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="book")
    def __str__(self):
        return f"{self.book} have a {self.tog}"
    

class Review(models.Model):
    review_id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Reviewer")
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name = "book_review")
    text_review = models.TextField(null=True,blank=True)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
    def __str__(self):
        return f"{self.user} to {self.book}"
    