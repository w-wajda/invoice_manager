import calendar
import logging
from datetime import datetime, timedelta

from django.core.mail import send_mail

from base.celery import app
from base.settings import EMAIL_SENDER
from invoices.models import Invoice

logger = logging.getLogger(__name__)


@app.task(name="create_invoices_for_recurring")
def create_invoices_for_recurring():
    logger.info("Trying to create invoices recurring")

    invoices = Invoice.objects.filter(is_recurring=True)

    date = datetime.today()

    month_range = calendar.monthrange(date.year, date.month)
    last_day = month_range[1]

    if last_day != date.day:
        return

    for invoice in invoices:
        payment_date = date + timedelta(days=invoice.payment_date - invoice.sale_date)
        new_invoice = Invoice.objects.create(
            invoice_number=f"{date.month}/{date.year}",
            create_date=date,
            sale_date=date,
            payment_date=payment_date,
        )

        for item in invoice.items.all():
            item.pk = None
            item.invoice = new_invoice
            item.save()

        if invoice.user.email:
            subject = _("New recurring invoice")
            content = _(
                "A new recurring invoice has been created\n"
                "Best regards,\n"
                "Invoice Manager"
            )
            send_mail(
                subject,
                content,
                from_email=EMAIL_SENDER,
                recipient_list=[invoice.user.email],
            )