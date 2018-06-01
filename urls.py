from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from basket import views as basketViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basket/', include('basket.urls'), name='basket'),
    path('', basketViews.login, name='login')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
