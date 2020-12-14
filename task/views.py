from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from .models import *
from .forms import *


# HTMLを表示させる
def index(request):
    todo_items = Todo.objects.all()
    context = {'todo_items': todo_items}
    return render(request, 'index.html', context)

# 新しいtodoタスクが入力されたら保存
def todo_post(request):
    content = request.POST['content']
    # 空の要素が送られた場合、リストに追加しない
    if len(content):
        todo_task = Todo(content=content)
        todo_task.complete = False
        todo_task.save()
    return redirect("/")


def delete(request, task_id):
    delete_task = Todo.objects.get(id=task_id)
    delete_task.delete()
    return redirect("/")


def update(request, task_id):
    complete_task = Todo.objects.get(id=task_id)
    complete_task.complete = not complete_task.complete
    complete_task.save()
    return redirect("/")




def edit(request, task_id): # dynamic url path
    task = Todo.objects.get(id=task_id)
    
    form = TodoForm(instance=task)

    if request.method == 'POST':
        # form = TodoForm(request.POST, instance=task)
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'form': form}

    return render(request, 'edit.html', context)