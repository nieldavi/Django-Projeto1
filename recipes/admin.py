from django.contrib import admin

from .models import Category, Recipe

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass


class RecipesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipesAdmin)
admin.site.register(Category, CategoryAdmin)
