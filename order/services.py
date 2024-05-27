from django.conf import settings

from boat.models import Boat
from django.core.mail import send_mail

from order.models import Order
from boat.models import Boat


def send_order_email(order_item: Order):
    print(f'send_mail: {Order} ')
    print(settings.EMAIL_HOST)
    print(settings.EMAIL_PORT)
    print(settings.EMAIL_HOST_USER)
    print(settings.EMAIL_HOST_PASSWORD)
    print(settings.EMAIL_USE_SSL)





    send_mail(
        'Заявка на покупку лодки',
        f'{order_item.name} ({order_item.email}) хочет купить вашу лодку {order_item.boat.name}. Вам сообщение {order_item.message}',
        settings.EMAIL_HOST_USER,
        [order_item.boat.owner.email]
    )

    print(f'send_mail: {Order} ')
    print(settings.EMAIL_HOST)
    print(settings.EMAIL_PORT)
    print(settings.EMAIL_HOST_USER)
    print(settings.EMAIL_HOST_PASSWORD)
    print(settings.EMAIL_USE_SSL)
