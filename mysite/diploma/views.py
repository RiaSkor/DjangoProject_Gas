from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChapterForm
from .models import Chapter

def add_chapter(request):
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chapter_list')
    else:
        form = ChapterForm()
    return render(request, 'diploma/add_chapter.html', {'form': form})

def chapter_list(request):
    chapters = Chapter.objects.all()
    return render(request, 'diploma/chapter_list.html', {'chapters': chapters})

def edit_chapter(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    if request.method == 'POST':
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect('chapter_list')
    else:
        form = ChapterForm(instance=chapter)
    return render(request, 'diploma/edit_chapter.html', {'form': form, 'chapter': chapter})

def delete_chapter(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    if request.method == 'POST':
        chapter.delete()
        return redirect('chapter_list')
    return render(request, 'diploma/confirm_delete.html', {'chapter': chapter})
