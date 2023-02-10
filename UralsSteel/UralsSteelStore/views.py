from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.db.models import Count
from django.views.generic import ListView, DetailView
from django.views.generic.edit import BaseFormView

# Create your views here.
menu = [{'title': 'Услуги', 'url_name': 'services'},
        {'title': 'Каталог продукции', 'url_name': 'shop_catalog'},
        {'title': 'О компании', 'url_name': 'about_us'},
        {'title': 'Контакты', 'url_name': 'contacts'},
]

memory = {
    'good_id_to_basket': [],
    'basket_total_price': 0
}

# class IndexListView(ListView, ):
#     model = Products
#     context_object_name = 'products'
#     template_name = 'UralsSteelStore/index.html'
#     # form_c = {}
#     success_url = reverse_lazy('home')
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         category_id = 1
#         context['menu'] = menu
#         context['all_categories'] = Category_mp.objects.annotate(cnt=Count('products')).filter(cnt__gt=0)
#         context['products'] = Products.objects.filter(category=self.kwargs['category_id'] if 'category_id' in self.kwargs else category_id)
#         context['naw_cat'] = Category_mp.objects.get(pk=self.kwargs['category_id'] if 'category_id' in self.kwargs else category_id)
#         # if 'form' in self.form_c:
#         #     context['form'] = self.form_c['form']
#         # context['form'] = ModalRequestForm()
#         # print('POST', self.request.POST.get[''])
#
#         return context

    # def get_queryset(self, *args, **kwargs):
    #     if self.request.method == 'POST':
    #         form = ModalRequestForm(self.request.POST)
    #         if form.is_valid():
    #             # print('ka', form.cleaned_data)
    #             pass
    #     else:
    #         form = ModalRequestForm()
    #     self.form_c['form'] = form
    #     print('---------------',self.request.method)


        # Метод Index Замена классу IndexListView

def index(request, category_id=1):
    if request.method == 'POST':
        form = ModalRequestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ModalRequestForm()

    all_categories = Category_mp.objects.annotate(cnt=Count('products')).filter(cnt__gt=0)


    products = Products.objects.filter(category=category_id)
    naw_cat = Category_mp.objects.get(pk=category_id)

    context = {
        'products': products,
        'all_categories': all_categories,
        'menu': menu,
        'naw_cat': naw_cat,
        'form': form
    }
    if memory['basket_total_price']:
        context['basket_total_price'] = memory['basket_total_price']

    return render(request, 'UralsSteelStore/index.html', context=context)


def services(request):
    if request.method == 'POST':
        form = ModalRequestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ModalRequestForm()

    context = {'menu': menu, 'form': form}
    return render(request, 'UralsSteelStore/services.html', context=context)

def metal_cutting(request):

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = RequestForm()
    context = {'menu': menu, 'form': form}
    return render(request, 'UralsSteelStore/metal_cutting.html', context=context)

def shop_catalog(request, slug_cat=None,):

    select_items = [
        {'number': '0', 'title': 'По умолчанию', 'order': 'ordinary_price'},
        {'number': '1', 'title': 'По возр. цены', 'order': 'price'},
        {'number': '2', 'title': 'По убыв. цены', 'order': '-price'},

    ]

    cats = Category.objects.annotate(cnt=Count('goods')).order_by('id')
    current_select_item = request.POST.get('shop_goods_start_with')

    if slug_cat != None:
        if current_select_item == '0':
            goods = Goods.objects.filter(category__slug=slug_cat, is_published=True)
        elif current_select_item in ['1', '2',]:
            goods = Goods.objects.filter(category__slug=slug_cat, is_published=True).order_by(select_items[int(current_select_item)]['order'])
        else:
            goods = Goods.objects.filter(category__slug=slug_cat, is_published=True)
    else:
        if current_select_item in ['0', '', None]:
            goods = Goods.objects.filter(is_published=True)
        elif current_select_item == '1':
            goods = Goods.objects.filter(is_published=True).order_by('price')
        elif current_select_item == '2':
            goods = Goods.objects.filter(is_published=True).order_by('-price')
        else:
            goods = Goods.objects.filter(is_published=True)


    g = Goods.objects.values('title', 'is_published', 'images')
    images = Gallery.objects.all()
    sps = {}
    for i in images:
        sps[i.good.pk] = i.image.url
    print(sps)
    plh = 'https://via.placeholder.com/320x320'
    context = {
        'menu': menu,
        'cats': cats,
        'goods': goods,
        'select_items': select_items,
        'now_item': current_select_item,
        'sps': sps,
        'plh': plh
    }

    if len(memory['good_id_to_basket']) > 0:
        basket_items = []
        for i in memory['good_id_to_basket']:
            item = Goods.objects.get(pk=i)
            basket_items.append(item)
            print(basket_items)

        basket_total_price = 0
        for i in basket_items:
            basket_total_price += i.price
        context['basket_total_price'] = basket_total_price
        memory['basket_total_price'] = basket_total_price

    if request.POST.get('good_info_btn'):
        good_id_to_basket = request.POST.get('good_info_btn')
        print(good_id_to_basket)
        if good_id_to_basket not in memory['good_id_to_basket']:
            memory['good_id_to_basket'].append(good_id_to_basket)
    if memory['basket_total_price']:
        context['basket_total_price'] = memory['basket_total_price']


    return render(request, 'UralsSteelStore/shop_catalog.html', context=context)

def about_good(request, slug_cat=None, slug_good_name=None, current_img=None):
    context = {}
    context['menu'] = menu
    images = Gallery.objects.filter(good__slug=slug_good_name)[::-1]
    context['images'] = images


    if current_img != None:
        current_img = current_img.replace('-', '/').replace('_', '.')

        # first_img = images[0].image.url

        # context['first_img'] = first_img
        context['current_img'] = current_img
    else:

        if len(images) != 0:
            current_img = images[0].image.url
            context['current_img'] = current_img
        else:
            current_img_base = r'D:\MY DJANGO PROJECTS\SteelofhteUrals\UralsSteel\media\base_img.png'
            context['current_img_base'] = current_img_base

    good = Goods.objects.filter(slug=slug_good_name)
    context['good'] = good

    some_goods = Goods.objects.filter(category__title=good[0].category)[1:5]
    context['some_goods'] = some_goods

    images_for_some_goods = Gallery.objects.all()
    sps = {}
    for i in images_for_some_goods:
        sps[i.good.pk] = i.image.url
    context['sps'] = sps

    if request.POST.get('good_info_btn'):
        good_id_to_basket = request.POST.get('good_info_btn')
        print(good_id_to_basket)
        if good_id_to_basket not in memory['good_id_to_basket']:
            memory['good_id_to_basket'].append(good_id_to_basket)
    if memory['basket_total_price']:
        context['basket_total_price'] = memory['basket_total_price']


    return render(request, 'UralsSteelStore/about_good.html', context=context)


def basket(request):

    context = {
        'menu': menu
    }
    # if 'good_id_to_basket' in memory:
    #     context['good_id_to_basket'] = memory['good_id_to_basket']

    if len(memory['good_id_to_basket']) > 0:
        basket_items = []
        for i in memory['good_id_to_basket']:
            item = Goods.objects.get(pk=i)
            basket_items.append(item)
            print(basket_items)

        context['good_id_to_basket'] = basket_items
        context['basket_len'] = len(memory['good_id_to_basket'])

        basket_total_price = 0
        for i in basket_items:
            basket_total_price += i.price
        context['basket_total_price'] = basket_total_price
        memory['basket_total_price'] = basket_total_price
        context['good_id_to_basket_mes'] = 'basket_is_full'
    else:
        context['basket_total_price'] = '0'
        context['good_id_to_basket_mes'] = 'basket_is_empty'
        context['basket_len'] = 0
    print(context)

    if request.POST.get('basket_item_del_btn'):
        good_for_del = request.POST.get('basket_item_del_btn')
        print('good_for_del', good_for_del)
        begine = memory['good_id_to_basket']
        try:
            begine.remove(good_for_del)
        except ValueError:
            print('Item not in list')
        memory['good_id_to_basket'] = begine

    if request.POST.get('clean_basket'):
        begine = memory['good_id_to_basket']
        try:
            begine.clear()
        except:
            print('Item not in list')
        memory['good_id_to_basket'] = begine
    return render(request, 'UralsSteelStore/basket.html', context=context)




def about_us(request):
    context = {
        'menu': menu,
    }
    return render(request, 'UralsSteelStore/about_us.html', context=context)
def contacts(request):
    pass





