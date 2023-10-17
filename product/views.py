from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Product,SearchHistory
# Create your views here.





class HomeScreen(TemplateView):
    template_name = "home/index.html"




class AllProducts(ListView):
    queryset = Product.objects.all().prefetch_related("prices")
    model = Product
    template_name = "products/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(AllProducts, self).get_context_data(*args, **kwargs)
        list_object = context['object_list']
        page = self.request.GET.get('page', 1)
        paginator = Paginator(list_object, 24)
        try:
            list_object = paginator.page(page)
        except PageNotAnInteger:
            list_object = paginator.page(1)
        except EmptyPage:
            list_object = paginator.page(paginator.num_pages)
        context['object_list'] = list_object
        return context





class ProductDetails(DetailView):
    queryset = Product.objects.all().prefetch_related("prices")
    template_name = "products/details.html"






class SearchProductListView(ListView):
    template_name = "products/index.html"

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(SearchProductListView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('name')
        context['query'] = query
        return context

    def get_queryset(self):
        request = self.request
        method_dict = request.GET
        name = method_dict.get('name', None)
        queryset = Product.objects.filter(part_number=name).prefetch_related("prices")
        if queryset:
            SearchHistory.objects.create(query=name)
        page = self.request.GET.get('page', 1)
        paginator = Paginator(queryset, 24)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        return queryset


