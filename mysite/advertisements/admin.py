from django.contrib import admin
from .models import Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'created_date', 'auction']
    list_filter = ['auction', 'created_at']
    actions = ["mark_auction_as_true", "mark_auction_as_false"]
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description'),
            'classes': ['collapse']
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        }),
    )
    search_fields = ("title",)


    @admin.action(description="Добавить возможность торга")
    def mark_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.action(description="Убрать возможность торга")
    def mark_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

# admin.site.register(Advertisement, AdvertisementAdmin) # 2

