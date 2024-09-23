from .models import Category

def categories_name(request):
    return {"categories":Category.objects.all()}