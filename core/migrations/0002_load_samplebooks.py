from django.db import migrations, models
from django.conf import settings
import os
import csv
import datetime

def load_books(apps, schema_editor):
    # Import books, authors, and categories
    Book = apps.get_model('core', 'Book')
    BookAuthor = apps.get_model('core', 'BookAuthor')
    Category = apps.get_model('core', 'Category')

    # Delete initial books, authors, and categories
    Category.objects.all().delete()
    BookAuthor.objects.all().delete()
    Book.objects.all().delete()

    # Set filename to sample_books.csv
    filename = os.path.join(settings.BASE_DIR, 'sample_books_added_categories.csv')

    with open(filename) as file:
        # Read CSV
        reader = csv.DictReader(csv_file)

        # Create for loop to read through data
        for row in reader:
                # Retrieve author or create one if necessary
                author, _ = BookAuthor.objects.get_or_create(name=row['author'])
                author.save()

                # Retrieve category or create one if necessary
                category, _ = Category.objects.get_or_create(name=row['category'])
                category.save()

                # Retrieve book fields
                book = Book(
                        book_title = row['title'],
                        book_author = author,
                        book_url = row['url'],
                        book_description = row['description'],
                        book_category = category,
                        db_date_added = 
                        

                )

