from .models import *
select_items = [
    {'number': '0', 'title': 'По умолчанию', 'order': 'ordinary_price'},
    {'number': '1', 'title': 'По возр. цены', 'order': 'price'},
    {'number': '2', 'title': 'По убыв. цены', 'order': '-price'},

]

def get_good(slug_cat, current_select_item):

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
    return goods

