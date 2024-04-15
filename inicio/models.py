from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

# Create your models here.
class inicioPage(Page):
    '''
    The home page has a carousel of images and a list of services.
    '''
    imagenCarousel = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Imagen de Carousel",
    )
    body = RichTextField(blank=True)

    # modify your content_panels:
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("imagenCarousel"),
            ],
            heading="Carousel",
        ),
        FieldPanel("body"),
    ]
    
    
    
    # sglulr manager
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
    
    