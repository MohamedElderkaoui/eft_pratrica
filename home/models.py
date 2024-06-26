from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel,InlinePanel


class HomePage(Page):
    # add the Hero section of HomePage:
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    hero_text = models.CharField(
        blank=True,
        max_length=255, help_text="Write an introduction for the site"
    )
    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=255,
        help_text="Text to display on Call to Action",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link to for the Call to Action",
    )
    # imagenes para carrusel en home:
    carousel_images = models.ManyToManyField(
        "wagtailimages.Image",
        related_name="+",
        blank=True,
        help_text="Immagini per il carousel in homepage",
    )
    body = RichTextField(blank=True)

    # modify your content_panels:
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("hero_text"),
                FieldPanel("hero_cta"),
                FieldPanel("hero_cta_link"),
                FieldPanel("carousel_images"),
            ],
            heading="Hero section",
        ),
        FieldPanel('body'),
        MultiFieldPanel(
            [
                InlinePanel("carousel_images", label="Carousel images"),
            ],
            heading="Carousel images",
        ),
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
    
    