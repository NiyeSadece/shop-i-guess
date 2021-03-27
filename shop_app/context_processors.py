from .models import Category


def menu_categories(request):
    """Filter for getting categories on the main view."""
    categories = Category.objects.all()
    return {'menu_categories': categories}
