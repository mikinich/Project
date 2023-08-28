from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()
class Advertisement(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    auction = models.BooleanField(help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    @admin.display
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M")
            return format_html(
                "<span style='color: green; font-weight: bold'>Сегодня в {}</span>", created_time
            )
        return self.created_at.strftime("%d.%m.%Y - %H:%M")

    def __str__(self):
        return f"Advertisement(id={self.id}, price={self.price})"

    class Meta:
        db_table = "advertisements"
