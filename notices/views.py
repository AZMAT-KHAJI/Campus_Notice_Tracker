# notices/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Notice, Category
from .forms import NoticeForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from .user_roles import get_user_role


# Dashboard: show all notices
@login_required
def dashboard(request):
    notices = Notice.objects.all().order_by('-created_at')
    query = request.GET.get('q')
    category = request.GET.get('category')

    if query:
        notices = notices.filter(Q(title__icontains=query) | Q(content__icontains=query))
    if category:
        notices = notices.filter(category__id=category)

    categories = Category.objects.all()
    return render(request, 'notices/dashboard.html', {'notices': notices, 'categories': categories})

'''@login_required
def create_notice(request):

    if not request.user.is_staff:
        raise PermissionDenied

    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)

        if form.is_valid():
            notice = form.save(commit=False)
            notice.created_by = request.user
            notice.save()

            return redirect('dashboard')

    else:
        form = NoticeForm()

    return render(request, 'notices/create_notice.html', {'form': form}) '''

@login_required
def create_notice(request):

    role = get_user_role(request.user)

    # OOP Permission Check
    if not role.can_create_notice():
        return redirect('dashboard')

    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)

        if form.is_valid():
            notice = form.save(commit=False)
            notice.created_by = request.user
            notice.save()
            return redirect('dashboard')

    else:
        form = NoticeForm()

    return render(request, 'notices/create_notice.html', {'form': form})




# Update notice
@login_required
def update_notice(request, pk):

    if not request.user.is_staff:
        raise PermissionDenied

    notice = get_object_or_404(Notice, pk=pk)

    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES, instance=notice)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = NoticeForm(instance=notice)

    return render(request, 'notices/update_notice.html', {'form': form})


# Delete notice
@login_required
def delete_notice(request, pk):

    if not request.user.is_staff:
        raise PermissionDenied

    notice = get_object_or_404(Notice, pk=pk)
    notice.delete()

    return redirect('dashboard')


# Detail view
@login_required
def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    notice.is_read = True
    notice.save()
    return render(request, 'notices/notice_detail.html', {'notice': notice})

def about(request):
    return render(request, 'notices/about.html')


def contact(request):
    return render(request, 'notices/contact.html')
