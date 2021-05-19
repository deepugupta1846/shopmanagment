import math

from django.shortcuts import render, redirect
from .forms import *
# Create your views here.


def index(request):
    return render(request, 'base.html')


def additem(request):
    msg = ""
    if request.method == 'POST':
        f = Additem(request.POST)
        f.save()
        msg = "Data Added Successfully"
    f = Additem()
    return render(request, 'Additem.html', {'form':f, 'msg':msg})


def showall(request, pn=1):
    # get total number of record from cookie tr
    tr = int(request.COOKIES.get('tr', 5))

    f = ShopManagment.objects.all()
    if tr > len(f):
        tr = len(f)
    tp = math.ceil(len(f)/tr)
    pages = []
    for i in range(1, tp+1):
        pages.append({"href": "/showitem/"+str(i)+"/", "content": i})
    f = f[(pn-1)*tr:(pn-1)*tr+tr]
    response = render(request, 'showitem.html', {'allitem': f, 'pages':pages})
    #response.set_cookie('tr', '10')
    response.set_cookie('name', 'deepu')
    response.set_cookie('fname', 'rajesh_prasad')
    return response


def delete(request, id):
    f = ShopManagment.objects.get(id=id)
    f.delete()
    return redirect('/showitem/')


def update(request, id):
        f = ShopManagment.objects.get(id=id)
        if request.method == 'POST':
            form = Additem(request.POST, instance=f)
            form.save()
            return redirect('/showitem/')
        form = Additem(instance=f)
        return render(request, 'update.html',{'updateform':form})

