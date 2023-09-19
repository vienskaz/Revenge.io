from django.contrib import admin
from .models import Item

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
admin.site.register(Item,ItemAdmin)
