from . models import *

def company(request):
    cprofile = CompanyProfile.objects.get(pk=2)

    context = {
        'cprofile': cprofile,
    }


    return context

def dropdown(request):
    category = Type.objects.all()


    context = {
        'category': category
    }
    
    return context
