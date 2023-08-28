from django.contrib import admin
from .models import Advertisement


# Register your models here.

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'create_date', 'update_date', 'auction', 'view_image']
    list_filter = ['auction']
    actions = ["mark_auction_as_true", "mark_auction_as_false"]
    fieldsets = (
        ("Общее", {'fields': ('title', 'description', 'user', 'image'), 'classes': ['collapse']}),
        ("Финансы", {'fields': ('price', 'auction'), 'classes': ['collapse']})
    )

    @admin.action(description='Добавить возможность торга')
    def mark_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.action(description='Убрать возможность торга')
    def mark_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
