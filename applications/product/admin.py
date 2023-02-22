from django.contrib import admin
from applications.product.models import Product, ProductImage
from django.contrib import admin
from .models import Product

class ImageAdmin(admin.TabularInline):
    model = ProductImage
    fields = ('image',)
    max_num = 5


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = (ImageAdmin,)
    list_display = ('name', 'slug', 'owner', 'price','tags')
    list_filter = ('owner', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('owner',)


