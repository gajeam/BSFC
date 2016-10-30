from django.shortcuts import render
from django.http import HttpResponse
from .forms import RevenueForm
# Create your views here.


def index(request):
    return HttpResponse("Hello welcome to the revenue view")


def revenue(request):
    form_class = RevenueForm
    if request.method == 'POST':
        # print(request.POST)
        start_date_day = request.POST.get('start_date_day')
        end_date_day = request.POST.get('end_date_day')
        # print(start_date_day, end_date_day)
        return HttpResponse("nice")
    return render(request, 'revenue.html', {'form': form_class})

