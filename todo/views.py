from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from . models import todo
# Create your views here.
def mytodo(request):
    if request.method=='POST':
        TODO=request.POST.get('addtodo')
        addtodo=todo(content=TODO)
        addtodo.save()
    mydata = todo.objects.all()
    return render(request,'todo.html',{'mytodo':mydata})

def tododelete(request,todo_id):

    mydat = todo.objects.get(id=todo_id)

    mydat.delete()

    return HttpResponseRedirect('/')
