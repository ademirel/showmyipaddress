from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
import sablon

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ilkProjem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^merhaba/', views.merhaba_django),
    url(r'^sarkilar/(S[0-9]+)/', views.sarkilar_icerik),
    url(r'^$', views.ana_sayfa),
    url(r'^sablon/', sablon.takim),
    url(r'^universite/', views.universite),
)
