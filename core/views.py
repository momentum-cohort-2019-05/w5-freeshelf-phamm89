from django.shortcuts import render, get_object_or_404, redirect
from core.models import Category, Book, BookAuthor, Favorite
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect


# Created views

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_authors = BookAuthor.objects.all().count()
    num_categories = Category.objects.all().count()

    # Show most recently added books
    recently_added_books = Book.objects.order_by('-db_date_added')[:3]
    different_categories = Category.objects.all()

    
    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_categories': num_categories,
        'recently_added_books': recently_added_books,
        'different_categories': different_categories,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3

class BookDetailView(generic.DetailView):
    model = Book

class CategoriesListView(generic.ListView):
    model = Category

class CategoriesDetailView(generic.DetailView):
    model = Category


@login_required
def favorite_view(request, book_pk):
    """View function for user to favorite or unfavorite a book."""
    book = get_object_or_404(Book, pk=book_pk)