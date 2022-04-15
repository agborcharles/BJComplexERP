"""bjcomplexerp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('configurations/', include('configurations.urls', namespace='configurations')),
    path('task/', include('task.urls', namespace='task')),
    path('purchase/', include('purchase.urls', namespace='purchase')),
    path('bakerycustomersinvoices/', include('bakerycustomersinvoices.urls', namespace='bakerycustomersinvoices')),
    path('bank/', include('bank.urls', namespace='bank')),
    path('payroll/', include('payroll.urls', namespace='payroll')),
    path('bakery_accounting/', include('bakery_accounting.urls', namespace='bakery_accounting')),
    path('general_ledger/', include('general_ledger.urls', namespace='general_ledger')),
    path('procurement/', include('procurement.urls', namespace='procurement')),
    path('contact_list/', include('contact_list.urls', namespace='contact_list')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
