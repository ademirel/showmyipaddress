# -*- coding: utf-8 -*-
from django.http import *
###views.py dosyasına bu satırı ekliyoruz.
from django.template.loader import get_template
##render_to_response()fonksiyonunu içe aktarıyoruz
from django.shortcuts import render_to_response

def merhaba_django(request):
    return HttpResponse(u'Merhaba Django')  

def sarkilar_icerik(request,sarki_kod):
    Sarkilar = {
        u"S01" : (u"Eminem",u"The Monster"),
        u"S02" : (u"Adele", u"Set Fire To The Rain"),
        u"S03" : (u"Enrique Iglesias", u"Heartbeat")
    }
    if sarki_kod in Sarkilar:
        html = u"Şarkı Adı: %s Şarkıcı: %s" %(Sarkilar[sarki_kod][1],Sarkilar[sarki_kod][0])
    else:
        html = Http404(u"Aradığınız şarkı bulunamadı")
 
    return HttpResponse(html)

def ana_sayfa(request):
    return HttpResponse("<h1>Ana Sayfa</h1>")

def universite(request):
 universiteler = (
     ['Sakarya','Sakarya',13,70000,],
    ['Yıldız Teknik','İstanbul',10,30000],
    ['Anadolu','Eskişehir',17,22000],
 )
 baslik = "Universiteler Nerde"
 return render_to_response('universiteler2.html',locals())
