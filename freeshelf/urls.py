"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from core import views as core_views

urlpatterns = [
    path('', core_views.index, name='index'),
    path('', RedirectView.as_view(url='/index/', permanent=True)),
    path('books/', core_views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', core_views.BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/favorite/', core_views.favorite_book, name='favorite-book'),
    path('category/<int:pk>', core_views.CategoriesDetailView.as_view(), name='category-detail'),
    path('favorites/', core_views.favorite_view, name='favorites'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

# Use static() to add url mapping to serve static files during development (only)
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
