from django.shortcuts import render
from .models import Contact
# Create your views here.
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

def getdata(request):
    data = serializers.serialize("xml", Contact.objects.all())
    print(data)
    return render(request, "home.html",{"message":data})

def serializeToJSONdata(request):
    data = serializers.serialize('json', Contact.objects.all())
    print(data)
    return render(request, "home.html",{"message":data})

def serializeToJSONLdata(request):
    data = serializers.serialize('jsonl', Contact.objects.all())
    print(data)
    return render(request, "home.html",{"message":data})

def deserializedata(request):
    data = getdata(request)
    dedata = serializers.deserialize("xml", data, ignorenonexistent=True)
    print(dedata)
    return render(request, "home.html",{"message":dedata})

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, None):
            return str(obj)
        return super().default(obj)
        