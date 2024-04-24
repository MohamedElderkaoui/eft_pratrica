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
from wagtail.models import Page# Your models.py file
from django.db import models

from modelcluster.fields import ParentalKey

class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactPage(AbstractEmailForm):

    template = "contact/contact_page.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "contact/contact_page_landing.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]
