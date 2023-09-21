from django.contrib import admin
from .models import *


from django.contrib.auth.models import User
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
class CustomerInlne(admin.StackedInline):
    model=Customer

class UserAdmin(admin.ModelAdmin):
    model= User
    fields=["username"]
    inlines = [CustomerInlne]



admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(NewsletterUser)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)