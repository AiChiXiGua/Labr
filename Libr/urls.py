"""Libr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin


from tushuguanli import views as tushuguanli_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add_book', tushuguanli_views.add_book),
    url(r'^add_author', tushuguanli_views.add_author),
    url(r'^view_books', tushuguanli_views.view_books),
    url(r'^renew_book', tushuguanli_views.renew_book),
    url(r'^delete_book', tushuguanli_views.delete_book),
    url(r'^find_book', tushuguanli_views.find_book),
    url(r'^view_authors', tushuguanli_views.view_authors),
]
