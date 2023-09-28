from django.contrib import admin
from .models import *

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def formatted_description(self, obj):
        return f'<pre>{obj.description}</pre>'

    formatted_description.allow_tags = True
    formatted_description.short_description = 'Description'

    def formatted_care_instructions(self, obj):
        return f'<pre>{obj.care_instructions}</pre>'

    formatted_care_instructions.allow_tags = True
    formatted_care_instructions.short_description = 'Care Instructions'

class CustomerInline(admin.StackedInline):
    model = Customer

class UserAdmin(admin.ModelAdmin):
    fields = ["username"]
    inlines = [CustomerInline]

# Unregister the default User admin
admin.site.unregister(User)

# Register your custom User admin
admin.site.register(User, UserAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(NewsletterUser)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ItemVariant)
