from django.shortcuts import render,redirect
from Todo_App.models import Todo
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        details = request.POST.get('details')
        
        Todo.objects.create(
            title = title,
            details = details
        )
        messages.success(request, "Your item is susseccfully added")
        return redirect('/')
    
    data = Todo.objects.all()
    context = {'datas':data}
        
    return render(request, 'index.html',context)

def delete(request, id):
    data = Todo.objects.filter(id=id)
    data.delete()
    messages.warning(request, "Your item is  deleted!!")
    return redirect('/')

def edit(request, id):
    
    data = Todo.objects.get(id = id)
    
    if request.method == "POST":
        title = request.POST.get('title')
        details = request.POST.get('details')
        
        data.title = title
        data.details = details
        
        data.save()
        return redirect('/')
    messages.success(request, "Your item is susseccfully edited!!")
    context = {'datas':data}
    
    return render(request, 'edit.html', context)
        