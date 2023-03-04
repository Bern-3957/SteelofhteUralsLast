from django.db.models import Count
from .helpers import *
from UralsSteelStore.models import Category, Gallery


menu = [{'title': 'Услуги', 'url_name': 'services'},
        {'title': 'Каталог продукции', 'url_name': 'shop_catalog'},
        {'title': 'О компании', 'url_name': 'about_us'},
        {'title': 'Контакты', 'url_name': 'contacts_ways'},
]
# memory = {
#     'good_id_to_basket': [],
#     'basket_total_price': 0
# }
select_items = [
    {'number': '0', 'title': 'По умолчанию', 'order': 'ordinary_price'},
    {'number': '1', 'title': 'По возр. цены', 'order': 'price'},
    {'number': '2', 'title': 'По убыв. цены', 'order': '-price'},

]

class ShopCatalogDataMixin:
    def get_user_context(self, current_select_item=None, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['cats'] = Category.objects.annotate(cnt=Count('goods')).order_by('id')
        context['select_items'] = select_items
        if 'slug_cat' in self.kwargs:
            context['goods'] = get_good(self.kwargs['slug_cat'], current_select_item)
        else:
            slug_cat = None
            context['goods'] = get_good(slug_cat, current_select_item)
        context['sps'] = self.get_images()

        return context

    # Загружает картинки на гланую страницу shop_catalog: одна картинка на один товар
    @classmethod
    def get_images(cls):
        images = Gallery.objects.all()
        sps = {}
        for i in images:
            sps[i.good.pk] = i.image.url
        return sps

    # Ответ при post запросах с shop_catalog: товары по умолчанию, по возростанию и убыванию
    def post_response(self, request, *args, **kwargs):
        if self.request.POST.get('shop_goods_start_with'):
            context = self.get_user_context(self.request.POST.get('shop_goods_start_with'), **kwargs)
            context['now_item'] = self.request.POST.get('shop_goods_start_with')
        else:
            context = self.get_user_context(**kwargs)
        return context
