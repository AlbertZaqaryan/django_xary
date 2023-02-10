from django.shortcuts import render
from .models import HomeCarusel, HomeTopic, HomeCategory
from django.views.generic import ListView, DetailView
# Create your views here.


class IndexListView(ListView):
    template_name = 'pages/index.html'

    def get(self, request):

        home_carusel_list = HomeCarusel.objects.all()
        home_category_list = HomeCategory.objects.all()
        return render(request, self.template_name, context={'home_carusel_list':home_carusel_list,
    
                                                    'home_category_list':home_category_list})


class IndexCategory(ListView):
    template_name = 'pages/listing-page.html'

    def get(self, request, id):
        home_category = HomeCategory.objects.filter(pk=id)
        return render(request, self.template_name, context={'home_category':home_category})



class IndexDetailView(DetailView):
    template_name = 'pages/detail-page.html'

    def get(self, request, slug):
        topic_detail = HomeTopic.objects.get(slug=slug)
        return render(request, self.template_name, context={'topic_detail':topic_detail})




def about(request):
    return render(request, 'pages/about.html')


