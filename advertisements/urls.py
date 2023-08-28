from django.urls import path
from .views import index, top_sellers, advertisement_post

urlpatterns = [
    path('', index, name="main-page"),
    path('top-sellers/', top_sellers, name='sellers'),
    path('advertisement/', advertisement_post, name='advert_post'),  # обьявления http://127.0.0.1:8000/advertisement/
]
