from django import template

register = template.Library()

@register.filter(name='get_cart_total')
def get_cart_total(cart):
    """
    Accepts a list of dicts: [{'product':…, 'quantity':…, 'total':…}, …]
    Returns the sum of each item['total'].
    """
    return sum(item.get('total', 0) for item in cart)
