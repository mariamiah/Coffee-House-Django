from django.urls import path
from .views import detail, stores

app_name="stores"
urlpatterns = [
    path('', stores, name="index"),
    path('<int:store_id>', detail, name="detail"),
]
