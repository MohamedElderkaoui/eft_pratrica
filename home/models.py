from django.db import models

from wagtail.models import Page

from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    """The home page of the site."""
    
    intro = models.CharField(max_length=255, blank=True)  # Define the 'intro' field here
    tittle = models.CharField(max_length=255, blank=True)  # Define the 'intro' field here
    body = RichTextField(blank=True)
    
    
    template = "home/home_page.html"

    def get_tittle(self):
        return self.tittle

    def get_intro(self):
        return self.intro

    def get_context(self, request):
        # Update context to include only published sections
        context = super().get_context(request)
        context['sections'] = self.get_children().live()
        return context

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('intro'),  # Include the 'intro' field in the content panels
    ]

    class Meta:
        verbose_name = 'home page'
        verbose_name_plural = 'home pages'