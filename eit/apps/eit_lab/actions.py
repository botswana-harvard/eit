from datetime import datetime

from django.contrib import messages

from lis.labeling.exceptions import LabelPrinterError

from .classes import EitAliquotLabeling
from .models import Order, OrderItem


def create_order(modeladmin, request, queryset):
    order_datetime = datetime.today()
    order = Order.objects.create(order_datetime=order_datetime)
    for aliquot in queryset:
        OrderItem.objects.create(order=order, aliquot=aliquot, order_datetime=order_datetime)
create_order.short_description = "Create order from selected aliquots"


def print_aliquot_label(modeladmin, request, aliquots):
    """ Prints an aliquot label."""
    aliquot_label = EitAliquotLabeling()
    try:
        for aliquot in aliquots:
            aliquot_label.print_label(request, aliquot)
    except LabelPrinterError as label_printer_error:
        messages.add_message(request, messages.ERROR, str(label_printer_error))
print_aliquot_label.short_description = "LABEL: print aliquot label"
