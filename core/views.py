from django.shortcuts import render, get_object_or_404, redirect
from core.models import Category, Book, BookAuthor, Favorite
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


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
def favorite_book(request, pk):
    """View function for user to favorite or unfavorite a book."""
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'GET':
        if request.user in book.book_favorite.all():
            book.book_favorite.remove(request.user)
            messages.info(request, f"You have removed {book.book_title} from your favorites book list.")
        else:
            book.book_favorite.add(request.user)
            messages.success(request, f"You have added {book.book_title} from your favorites book list.")
            
    return HttpResponseRedirect(request.GET.get("next"))


@login_required
def favorite_view(request):
    """View function for user to view all books in favorite list."""
    favorites_list = Favorite.objects.filter(user=request.user)

    return render(request, 'core/favorites.html', {'favorites_list': favorites_list})