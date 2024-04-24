from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.fields import StreamField
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalManyToManyField#
# ImageChooserBlock
from wagtail.images.blocks import ImageChooserBlock
# PageChooserBlock
from wagtail.blocks import PageChooserBlock
# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
#how to make an image carousel?
# Create your models here.
class inicioPage(Page):
    
    carouselImages =     StreamField([('carouselImage', ImageChooserBlock())], blank=True, use_json_field=True)
    servicios = StreamField([('servicio', PageChooserBlock(target_model='servicio.servicio'))], blank=True, use_json_field=True)
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('carouselImages'),
        ], heading="Carousel"),
        MultiFieldPanel([
            FieldPanel('servicios'),
        ], heading="Services"),
    ]
    template= "inicio/inicio_page.html"

