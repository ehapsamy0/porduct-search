from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Product, ProductPrices, SearchHistory

from .resource_import_export import ProductResource


class ProductPricesInline(admin.TabularInline):
    model = ProductPrices
    extra = 0


class PrductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # resource_class = ProductResource
    list_display = ("pk", "part_number")
    resource_class = ProductResource
    list_filter = ("status",)
    search_fields = [
        "part_number",
        "part_number_new",
        "part_number_description",
        "description",
    ]  # Add this line
    # actions = ['mark_active', 'mark_not_active', 'mark_tweeted', 'export_csv']
    inlines = [ProductPricesInline]

admin.site.register(ProductPrices)
admin.site.register(Product, PrductAdmin)
class SearchHistoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # resource_class = ProductResource
    list_display = ("pk", "query")

admin.site.register(SearchHistory,SearchHistoryAdmin)
