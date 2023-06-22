from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpRequest
from todo_app.models import Todo

# Create your views here.
def index_view(request):
    # return HttpResponse("<h1>Todo List</h1>")
    searchStr = request.GET.get('todoSearch', "")
    statusStr = request.GET.get('status', "")
    todo_list = Todo.objects.all().order_by("-created_at")
    print(type(todo_list))
    print("Search Term - {}".format(searchStr))
    
    if searchStr != '':                  
        todo_list = todo_list.filter(title__icontains=searchStr)

    if statusStr != '':
        todo_list = todo_list.filter(completed=statusStr)
        
    data = {
        "todo_list" : todo_list
    }
    return render(request,"list.html", context=data)

def update_view(request, todo_id):
    if request.method != 'POST':
        return HttpResponse('Error - Method not allowed')    
    else:
        todo = Todo.objects.get(id=todo_id)
        todo.completed = 1
        todo.save()
        return redirect("todo_list_view")

def delete_view(request, todo_id):
    if request.method != 'POST':
        return HttpResponse('Error - Method not allowed')    
    else:
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect("todo_list_view")

def create_view(request):
    print("Inside Create View")
    todoTitle = request.POST['todoTitle']
    todoDesc  = request.POST['todoDescription']
    if(todoTitle != ' '):
        print("Todo Title: {} Todo Description: {}".format(todoTitle, todoDesc))
        Todo.objects.create(
            title=todoTitle,
            description=todoDesc,
            completed=False
        )
    return redirect("todo_list_view")
