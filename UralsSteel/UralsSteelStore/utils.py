menu = [{'title': 'Услуги', 'url_name': 'services'},
        {'title': 'Каталог продукции', 'url_name': 'shop_catalog'},
        {'title': 'О компании', 'url_name': 'about_us'},
        {'title': 'Контакты', 'url_name': 'contacts_ways'},
]
memory = {
    'good_id_to_basket': [],
    'basket_total_price': 0
}

class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        if memory['basket_total_price']:
            context['basket_total_price'] = memory['basket_total_price']
        return context