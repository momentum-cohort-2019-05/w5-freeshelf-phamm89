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
        reader = csv.reader(csv_file)
        # Iterate over header
        header = reader.next()

        # Create for loop to read through data

