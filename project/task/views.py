from django.shortcuts import render,redirect
from . import forms
from task.models import TaskModel
def add_task(request):
    if  request.method == 'POST':
      task_form=forms.TaskForm(request.POST)
      if task_form.is_valid():
         task_form.save()
         return redirect("add_task")
    else:   
        task_form=forms.TaskForm()
    return render(request,'add_task.html',{'form':task_form})
def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)

    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect("homepage")
    else:
        task_form = forms.TaskForm(instance=task)

    return render(request, 'add_task.html', {'form': task_form})
def delete_task(request,id):
    task=TaskModel.objects.get(pk=id)
    task.delete()
   
    return redirect("homepage")
