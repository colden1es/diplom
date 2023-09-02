from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', include('payment.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('shop/', include('shop.urls')),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

