from django.shortcuts import render,HttpResponseRedirect
from django.views import generic
from .models import Hotel
from django.db.models import Q
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'hotel/search.html')
#
# class IndexView(generic.ListView):
#     template_name='hotel/show_hotel.html'
#     context_object_name='all_hotels'
#
#     def get_queryset(self):
#         return Hotel.objects.all()
#

def search(request):
    if request.method=='POST':
        value = request.POST['search_value']

        if value:

            match = Hotel.objects.filter(Q(name__icontains=value) |
                                        Q(city__icontains=value)
                                        )
            if match:
                return render(request,'hotel/show_hotel.html',{'sr':match})
            else:
                return render(request,'hotel/no_result.html')
        else:
            return render(request,'hotel/search.html')

    return render(request,'hotel/search.html')
