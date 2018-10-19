from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render( 
        request,
        "controle_cadastral/index.html",
        {
            'title': 'Mocidade Secreta',
        }
    )

