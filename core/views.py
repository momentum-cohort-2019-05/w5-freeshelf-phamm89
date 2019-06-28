from django.shortcuts import render
from core.models import Category, Book, BookAuthor
from django.views import generic


# Created views

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_authors = BookAuthor.objects.all().count()
    num_categories = Category.objects.all().count()

    # Show most recently added books
    recently_added_books = Book.objects.order_by('-db_date_added')
    different_categories = Category.objects.all()
    
    
    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_categories': num_categories,
        'recently_added_books': recently_added_books,
        'different_categories': different_categories
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book
