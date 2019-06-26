from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


# Created Models
class Category(models.Model):
    """Model representing a book category."""
    book_category = models.CharField(max_length=200, help_text='Enter a book category (e.g. CSS, HTML, Javascript, Python, R)')
    
    class Meta:
        verbose_plural_name = "categories"

    def __str__(self):
        """String for representing the Model object."""
        return self.book_category
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for a book category."""
        return reverse('category-detail', args=[str(self.id)])