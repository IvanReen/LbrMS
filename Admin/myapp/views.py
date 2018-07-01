from django.http import HttpResponseRedirect
from django.shortcuts import render

from myapp.models import *

# 出版社列表
def publisher_list(request):
    # 查询
    publisher = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publisher_list':publisher})

# 添加出版社
def add_publisher(request):
    # POST方式提交数据
    if request.method == 'POST':
        new_publisher_name = request.POST.get('name')
        Publisher.objects.create(name=new_publisher_name)
        return HttpResponseRedirect('/publisher_list/')
    return render(request, 'add_publisher.html')

# 删除出版社
def drop_publisher(request):
    # get方式拿到出版社id
    drop_id = request.GET.get('id')
    drop_obj = Publisher.objects.get(id=drop_id)
    drop_obj.delete()
    return HttpResponseRedirect('/publisher_list/')

# 编辑出版社
def edit_publisher(request):
    if request.method == 'POST':
        edit_id = request.GET.get('id')
        edit_obj = Publisher.objects.get(id=edit_id)
        new_name = request.POST.get('name')
        edit_obj.name = new_name
        edit_obj.save()
        return HttpResponseRedirect('/publisher_list/')
    edit_id = request.GET.get('id')
    edit_obj = Publisher.objects.get(id=edit_id)
    return render(request, 'edit_publisher.html', {'publisher':edit_obj})

# 书籍列表
def book_list(request):
    book = Book.objects.all()
    return render(request, 'book_list.html', {'book_lish':book})

# 添加书籍
def add_book(request):
    if request.method == 'POST':
        new_book_name = request.POST.get('name')
        publisher_id = request.POST.get('publisher_id')
        Book.objects.create(name=new_book_name, publisher_id=publisher_id)
        return HttpResponseRedirect('/book_list/')
    msg = Publisher.objects.all()
    return render(request, 'add_book.html', {'publisher_list':msg})

# 删除书籍
def drop_book(request):
    drop_id = request.GET.get('id')
    drop_obj = Book.objects.get(id=drop_id)
    drop_obj.delete()
    return HttpResponseRedirect('/book_list/')

# 编辑书籍
def edit_book(request):
    if request.method == 'POST':
        new_book_name = request.POST.get('name')
        new_publisher_id = request.POST.get('publisher_id')
        edit_id = request.GET.get('id')
        edit_obj = Book.objects.get(id=edit_id)
        edit_obj.name = new_book_name
        edit_obj.publisher_id = new_publisher_id
        edit_obj.save()
        return HttpResponseRedirect('/book_list/')
    edit_id = request.GET.get('id')
    edit_obj = Book.objects.get(id=edit_id)
    all_publisher = Publisher.objects.all()
    return render(request, 'edit_book.html', {'book':edit_obj, 'publisher_list':all_publisher})

def author_list(request):
    author = Author.objects.all()
    return render(request, 'author_list.html', {'author_list':author})

# 添加作者
def add_author(request):
    if request.method == 'POST':
        new_author_name = request.POST.get('name')
        Author.objects.create(name=new_author_name)
        return HttpResponseRedirect('/author_list/')
    return render(request, 'add_author.html')

# 删除作者
def drop_author(request):
    drop_id = request.GET.get('id')
    drop_obj = Author.objects.get(id=drop_id)
    drop_obj.delete()
    return HttpResponseRedirect('/author_list/')

# 编辑作者
def edit_author(request):
    if request.method == 'POST':
        edit_id = request.GET.get('id')
        edit_obj = Author.objects.get(id=edit_id)
        new_author_name = request.POST.get('name')
        new_book_id = request.POST.getlist('book_id')
        edit_obj.name = new_author_name
        edit_obj.book.set(new_book_id)
        edit_obj.save()
        return HttpResponseRedirect('/author_list/')
    edit_id = request.GET.get('id')
    edit_obj = Author.objects.get(id=edit_id)
    all_book = Book.objects.all()
    return render(request, 'edit_author.html', {'author':edit_obj, 'book_list':all_book})