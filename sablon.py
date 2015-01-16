# -*- coding: utf-8 -*-
 
from django.http import *
from django import template
from django.conf import settings
 
#settings.configure(DEBUG=True,Template_DEBUG=True)
 
def takim(request):
    takimlar = ["Galatasaray","Fenerbahçe","Beşiktaş"]
    
    s = template.Template(u'''<table border="1">
     <tr>  <th>Takım Adı</th></tr> 
     {% for i in takimlar %}  
     <tr>   <td>{{i}}</td>  </tr> 
     {% endfor %}</table> ''')
    b = template.Context({'takimlar':takimlar}) 
    return HttpResponse(s.render(b))
