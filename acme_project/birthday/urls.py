from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'birthday'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BirthdayCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.BirthdayUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.BirthdayDeleteView.as_view(), name='delete'),
    path('list/', views.BirthdayListView.as_view(), name='list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
