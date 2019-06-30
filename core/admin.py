from django.contrib import admin
from core.models import Book, BookAuthor, Category, Favorite

# Register models

# Register the Admin classes for BookAuthor using the decorator
@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    pass


# Register the Admin classes for Category using the decorator
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    


# Register the Admin classes for Book using the decorator
    @admin.register(Book)
    class BookAdmin(admin.ModelAdmin):
        list_display = ('book_title', 'book_author', 'book_url', 'book_description', 'db_date_added')


# Register the Admin classes for Favorite using the decorator
@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'book')







