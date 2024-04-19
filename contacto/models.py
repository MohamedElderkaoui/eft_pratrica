# Your models.py file
from django import forms
from django.conf import settings
from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel, HelpPanel, FieldRowPanel

from wagtail.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)


class ContactPageMapSettings(models.Model):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='map_settings',
    )
    address_line_1 = models.CharField(max_length=255, blank=True)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=255, blank=True)

    content_panels = [
        FieldPanel('address_line_1'),
        FieldPanel('address_line_2'),
        FieldPanel('city'),
        FieldPanel('state'),
        FieldPanel('postal_code'),
    ]



class ContactForm(AbstractEmailForm):
    subject = 'Contact message from website'

    # form fields
    name = AbstractFormField(max_length=255)
    email = AbstractFormField(max_length=255)
    message = AbstractFormField(widget=forms.Textarea)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('name'),
        FieldPanel('email'),
        FieldPanel('message', classname="full"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['email_subject'] = "Contact message from website"
        return context

    def send_email(self, data):
        email_address = data['email']
        contact_name = data['name']
        message = data['message']

        mail_subject = self.subject
        message = (
            f"Name: {contact_name}\n"
            f"Email: {email_address}\n"
            f"Message: {message}"
        )

        self.send_mail(
            subject=mail_subject,
            message=message,
            from_email=self.get_from_address(),
            recipient_list=[settings.CONTACT_FORM_RECIPIENT]
        )


    class Meta:
        abstract = True

