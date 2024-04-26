from django.db import models

# Create your models here.

from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class abouta_usPage(Page):

    body = RichTextField(blank=True)
    template = 'about_us/about_us.html'

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    def get_context(self, request):
        """
        A method to retrieve the context with respect to the given request.
        Parameters:
            request: The request object to retrieve context for.
        Returns:
            The context obtained after calling the superclass's get_context method.
        """
        context = super().get_context(request)
        return context
    class ourteamMember(models.Model):
        name = models.CharField(max_length=255)
        role = models.CharField(max_length=255)
        image = models.ForeignKey(
            "wagtailimages.Image",
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name="+",
        )

        panels = [
            FieldPanel('name'),
            FieldPanel('role'),
            FieldPanel('image'),
        ]

        def __str__(self):
            return self.name
        