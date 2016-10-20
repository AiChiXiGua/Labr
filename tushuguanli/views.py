from django.shortcuts import render
from tushuguanli.models import Author, Book


def add_book(request):
    state = None
    book_list = None
    if request.method == 'POST':
        newbook = Book(
            ISBN=request.POST.get('ISBN', ''),
            Title=request.POST.get('Title', ''),
            Publisher=request.POST.get('Publisher', ''),
            PublishDate=request.POST.get('PublishDate', ''),
            Price=request.POST.get('Price', ''),
        )
        newbook.save()
        book_list = Book.objects.all().order_by('Title')
        author_ids = request.POST.getlist('author_ID')
        for author_id in author_ids:
            newbook.AuthorID.add(author_id)
        state = 'add success'
    add_book_state = {
        'state': state,
        'book_list': book_list,
    }
    return render(request, 'tushu/add_book.html', add_book_state)


def view_books(request):
    all_books = Book.objects.all().order_by('Title')
    state = {
        'all_books': all_books,
    }
    return render(request, 'tushu/view_books.html', state)


def add_author(request):
    state = None
    if request.method == 'POST':
        new_author = Author(
            AuthorID=request.POST.get('Author', ''),
            Name=request.POST.get('Name', ''),
            Age=request.POST.get('Age', ''),
            Country=request.POST.get('Country', ''),
        )
        new_author.save()
        state = 'add success'
    add_author_state = {
        'state': state
    }
    return render(request, 'tushu/add_author.html', add_author_state)


def view_authors(request):
    all_authors = Author.objects.all().order_by('AuthorID')
    state = {
        'all_authors': all_authors,
    }
    return render(request, 'tushu/view_authors.html', state)


def find_book(request):
    state = None
    his_or_her_book = None
    book_search_result = None
    if request.method == 'POST':
        if request.POST['search_name']:
            search_name = request.POST.get('search_name', '')
            if Author.objects.filter(Name__iexact=search_name):
                state = 'search_name_exist'
                author = Author.objects.filter(Name__iexact=search_name)
                his_or_her_book = {
                    'book_message': author.book_set.all()
                }
            else:
                state = 'Not find search name'
        elif request.POST['search_book']:
            search_title = request.POST.get('search_book', '')
            if Book.objects.filter(Title__iexact=search_title):
                book_search = Book.objects.filter(Title__iexact=search_title)
                book_search_result = {
                    'book_message': book_search,
                    'author_message': Author.objects.filter(author__Title=Book.Title)
                }
                state = 'Find this book'
            else:
                state = 'Not find this book'

    this_book = {
        'state': state,
        'These_Books': his_or_her_book,
        'book_search_result': book_search_result,
    }

    return render(request, 'tushu/find_book.html', this_book)


def renew_book(request):
    state = None
    the_book = None
    if request.method == 'GET':
        isbn = request.GET.get('ISBN', '')
        if Book.objects.filter(ISBN__iexact=isbn):
            book = Book.objects.filter(ISBN__iexact=isbn)
            state = 'Find this book!'
            if request.GET.get('new_publisher', ''):
                the_book = book.update(publisher=request.GET.get('new_publisher'))
            elif request.GET.get('new_PublishDate', ''):
                the_book = book.update(PublishDate=request.GET.get('new_PublishDate'))
            elif request.GET.get('new_Price'):
                the_book = book.update(Price=request.GET.get('new_Price'))
        else:
            state = 'Not find this book'

    this_new_book = {
        'state': state,
        'the_renew_book': the_book,
    }
    return render(request, 'tushu/renew_book.html', this_new_book)


def delete_book(request):
    state = None
    or_delete_state = None
    if request.method == 'GET':
        item = request.GET.get('item', '')
        isbn = request.GET.get('ISBN', '')
        the_book = Book.objects.get(ISBN__exact=isbn)

        if item == 'delete':
            the_book.delete()
            state = 'Delete succcess'
            if Book.objects.filter(ISBN__contains=isbn):
                or_delete_state = 'Delete Error'
            else:
                or_delete_state = 'This book has been deleted'

    this_book = {
        'state': state,
        'the_delete_result': or_delete_state,
    }
    return render(request, 'tushu/delete_book.html', this_book)

