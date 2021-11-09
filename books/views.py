from django.shortcuts import render, redirect
from .models import *


def redirect_index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'

    context = {
        'books': Book.objects.all(),
    }
    return render(request, template, context)


def pub_date_view(request, value):
    template = 'books/books_filter.html'

    paginator = Book.objects.order_by('pub_date').distinct('pub_date')

    element_list = []
    for element in paginator:
        element_list.append(str(element.pub_date))

    for index, el_list in enumerate(element_list):
        if el_list == str(value):
            value_index = index

    pub_date_list = list(enumerate(element_list))

    if value_index == pub_date_list[-1][0]:
        next_date = pub_date_list[0]
    else:
        next_date = pub_date_list[value_index + 1]

    previous_date = pub_date_list[value_index - 1]

    context = {
        'books': Book.objects.filter(pub_date=value),
        'date': value,
        'pages': paginator,
        'prev_date': previous_date[1],
        'next_date': next_date[1]
    }

    return render(request, template, context)
