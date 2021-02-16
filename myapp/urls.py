from django.urls import path, include

app_name = 'myapp'

urlpatterns = [
    path('', Index, name='index'),
]
