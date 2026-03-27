from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_http_methods

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')

    q = request.GET.get('q')
    if q:
        todos = todos.filter(Q(title__icontains=q) | Q(description__icontains=q))

    paginator = Paginator(todos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todo_list.html', {'page_obj': page_obj})

@login_required
def todo_info(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo_info.html', todo.__dict__)


@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_info', pk=todo.pk)
    else:
        form = TodoForm()
    return render(request, 'todo_create.html', {'form': form})


@login_required
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_info', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    context = {'form': form, 'todo': todo}
    return render(request, 'todo_update.html', context)


@login_required
@require_http_methods(["POST"])
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    return redirect('todo_list')