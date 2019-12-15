"""virginiah URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$',views.home, name = 'home'),
    url(r'',include ('gallery.urls'))
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_images,name = 'pastImages'), 
    # url(r'^search/', views.search_results, name='search_results'),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
# 'document_root': settings.MEDIA_ROOT})

]
