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
        reader = csv.DictReader(file)

        # Create for loop to read through data
        for row in reader:
                # Retrieve author or create one if necessary
                book_author, created = BookAuthor.objects.get_or_create(name=row['author'])
                book_author.save()

                # Retrieve category or create one if necessary
                book_category, created = Category.objects.get_or_create(name=row['category'])
                book_category.save()

                # Retrieve book fields
                book = Book(
                        book_title = row['title'],
                        book_author = book_author,
                        book_url = row['url'],
                        book_description = row['description'],
                        book_category = book_category,
                        db_date_added = datetime.datetime.now()
                )
                book.save()


# Migrations are not reversible; create function to reverse migration
def reverse_load(apps, schema_editor):
    Book = apps.get_model('core', 'Book')
    BookAuthor = apps.get_model('core', 'BookAuthor')
    Category = apps.get_model('core', 'Category')

    Category.objects.all().delete()
    BookAuthor.objects.all().delete()
    Book.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial.'),
    ]

    operations = [migrations.RunPython(load_books, reverse_load)]
