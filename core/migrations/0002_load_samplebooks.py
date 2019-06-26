from django.db import migrations, models
from django.conf import settings
import os
import csv

def load_books(apps, schema_editor):
    # Import books and authors
    Book = apps.get_model('core', 'Book')
    BookAuthor = apps.get_model('core', 'BookAuthor')

    # Delete initial books and authors
    BookAuthor.objects.all().delete()
    Book.objects.all().delete()

    # Set filename to sample_books.csv
    filename = os.path.join(settings.BASE_DIR, 'sample_books.csv')

    with open(filename) as file:
        # Read CSV
        reader = csv.DictReader(csv_file)

        # Create for loop to read through data
        for row in reader:
                # Look up author or create one if necessary
                book_author, _ = BookAuthor.objects.get_or_create(name=row['author'])
                book_author.save()

                book = Book(

                )

