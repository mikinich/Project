from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Advertisement(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    auction = models.BooleanField(help_text="Торг")
    create_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="advertisements")

    @admin.display
    def create_date(self):
        from django.utils import timezone
        if self.create_ad.date() == timezone.now().date():
            create_time = self.create_ad.time().strftime("%H:%M")
            return format_html("<span style='color: green'>Сегодня в {}</span>", create_time)
        return self.create_ad.strftime("%d.%m.%Y - %H:%M")

    @admin.display
    def update_date(self):
        from django.utils import timezone
        if self.updated_ad.date() == timezone.now().date():
            update_time = self.updated_ad.time().strftime("%H:%M")
            return format_html("<span style='color: blue'>Сегодня в {}</span>", update_time)
        return self.updated_ad.strftime("%d.%m.%Y - %H:%M")

    @admin.display
    def view_image(self):
        if self.image != "":
            return format_html("<img src={} width='50'>", self.image.url)
        return "Нет изображения!"

    def __str__(self):
        return f'id={self.id} title={self.title}, price={self.price}'

    class Meta:
        db_table = 'advertisement'
