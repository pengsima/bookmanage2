from django.shortcuts import render,HttpResponse,redirect,reverse
from app01 import models

# Create your views here.
def home(request):
 return render(request,'home.html')


def show_book(request):
    # 先查询所有的书籍
    book_list = models.Book.objects.all()
    return render(request,'book_list.html',locals())


def add_book(request):
    if request.method == 'POST':
        # print(request.POST)

        title = request.POST.get("title")
        price = request.POST.get("price")
        publish_date = request.POST.get("date")
        publish_id = request.POST.get("publish")
        authors = request.POST.getlist("authors")
        # 数据库新增数据
        book_obj = models.Book.objects.create(title=title,price=price,publish_time=publish_date,publish_id=publish_id)
        # 可以尝试用**request.POST来新增数据

        # 去书籍与作者的第三表手动创建关系
        book_obj.authors.add(*authors)
        # 跳转到图书的展示页面
        return redirect(reverse('book_list'))
    # 将出版社和作者数据全部传递给添加页面
    publish_list = models.Publish.objects.all()
    author_list = models.Author.objects.all()
    # get请求返回一个添加页面
    return render(request,'add_book.html',locals())


def delete_book(request,delete_id):
    # 获取用户想要删除的数据的id
    # print(delete_id)
    models.Book.objects.filter(pk=delete_id).delete()
    return redirect(reverse('book_list'))

def edit_book(request,edit_id):
    # 返回一个编辑页面，但是你这个编辑页面需要将原来数据的信息展示出来
    edit_obj = models.Book.objects.filter(pk=edit_id).first()
    if request.method == 'POST':
        # print(request.POST)
        title = request.POST.get("title")
        price = request.POST.get("price")
        publish_date = request.POST.get("date")
        publish_id = request.POST.get("publish")
        authors = request.POST.getlist("authors")
        models.Book.objects.filter(pk=edit_id).update(title=title,price=price,publish_time=publish_date,publish_id=publish_id)
        edit_obj.authors.set(authors)
        return redirect(reverse('book_list'))

    publish_list = models.Publish.objects.all()
    author_list = models.Author.objects.all()
    return render(request,'edit.html',locals())



def show_publish(request):
    # 先查询所有的书籍
    publish_list = models.Publish.objects.all()
    return render(request,'publish_list.html',locals())


def add_publish(request):
    if request.method == 'POST':
        # print(request.POST)

        name = request.POST.get("name")
        addr = request.POST.get("addr")
        email = request.POST.get("email")

        # 数据库新增数据
        publish_obj = models.Publish.objects.create(name=name,addr=addr,email=email)

        return redirect(reverse('publish_list'))
    # 将出版社和作者数据全部传递给添加页面
    publish_list = models.Publish.objects.all()

    # get请求返回一个添加页面
    return render(request,'add_publish.html',locals())

def delete_publish(request,delete_id):
    # 获取想要删除的数据的id
    # print(delete_id)
    models.Publish.objects.filter(pk=delete_id).delete()
    return redirect(reverse('publish_list'))


def edit_publish(request,edit_id):
    # 返回一个编辑页面，但是你这个编辑页面需要将原来数据的信息展示出来
    edit_obj = models.Publish.objects.filter(pk=edit_id).first()
    if request.method == 'POST':
        # print(request.POST)
        name = request.POST.get("name")
        addr = request.POST.get("addr")
        email = request.POST.get("email")

        models.Publish.objects.filter(pk=edit_id).update(name=name,addr=addr,email=email)

        return redirect(reverse('publish_list'))

    publish_list = models.Publish.objects.all()

    return render(request,'edit2.html',locals())


def show_author(request):
    # 先查询所有的书籍
    author_list = models.Author.objects.all()
    return render(request,'author_list.html',locals())

def add_author(request):
    if request.method == 'POST':
        # print(request.POST)

        name = request.POST.get("name")
        age = request.POST.get("age")

        phone = request.POST.get("phone")
        addr = request.POST.get("addr")
        # 数据库新增数据
        authordetail_obj = models.AuthorDetail.objects.create(phone=phone, addr=addr)
        author_obj = models.Author.objects.create(name=name,age=age,authordetail=authordetail_obj)

        # 你可以尝试用**request.POST来新增数据


        # 跳转到作者的展示页面
        return redirect(reverse('author_list'))
    # 将作者数据传递给添加页面

    author_list = models.Author.objects.all()
    # get请求返回一个添加页面
    return render(request,'add_author.html',locals())

def delete_author(request,authordetail_id):
    # 获取用户想要删除的数据的id
    # print(delete_id)
    models.AuthorDetail.objects.filter(pk=authordetail_id).delete()
    return redirect(reverse('author_list'))

def edit_author(request,edit_id):
    # 返回一个编辑页面，但是你这个编辑页面需要将原来数据的信息展示出来
    edit_obj = models.Author.objects.filter(pk=edit_id).first()
    edit_obj2 = models.AuthorDetail.objects.filter(pk=edit_obj.authordetail_id).first()
    if request.method == 'POST':
        # print(request.POST)

        name = request.POST.get("name")
        age = request.POST.get("age")

        phone = request.POST.get("phone")
        addr = request.POST.get("addr")

        models.AuthorDetail.objects.filter(pk=edit_obj.authordetail_id).update(phone=phone,addr=addr)
        authordetail_obj=models.AuthorDetail.objects.filter(pk=edit_id).first()
        models.Author.objects.filter(pk=edit_id).update(name=name,age=age,authordetail=authordetail_obj)

        return redirect(reverse('author_list'))

    author_list = models.Author.objects.all()

    return render(request,'edit3.html',locals())
