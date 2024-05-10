from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
""" 

card(block) o calculadora
↡
subapartados(cardlist)
↡
servicio(subapartadoslist)
↡
lista de servicio
"""

from django.db import models

from wagtail.models import Page as pg
#import slug


from wagtail.models import Page, GroupPagePermission, PageViewRestriction
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel, HelpPanel

from wagtail.models import Page as Pg
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock
""" class card """
class Card(Page):
    tittle=models.CharField(max_length=100)
    body=RichTextField(blank=True)
    template='cards/card.html'
    panels = [
        FieldPanel('tittle'),
        FieldPanel('body'),
    ]
    
    def __str__(self):
        return self.tittle




""" class subapartados (set of  card) """
class subapartados(Page):
   
    tittle = models.CharField(max_length=100)
    cardlist = StreamField([('card', blocks.PageChooserBlock(target_model='servicio.Card'))], blank=True, use_json_field=True)
  
    
#    template
    template='servicio/subapartados.html'

    content_panels = Page.content_panels +[
        FieldPanel('tittle'),
        FieldPanel('cardlist'),
    ]

    def __str__(self):
        return self.tittle

    class meta:
        verbose_name = 'Subapartado'
        verbose_name_plural = 'Subapartados'
"""
Class servicio(subapartadoslist) 
"""

class servicio(Page):
    tittle = models.CharField(max_length=100)
    body=RichTextField(blank=True)
    subapartadoslist = StreamField([('subapartados', blocks.PageChooserBlock(target_model='servicio.subapartados'))], blank=True, use_json_field=True, null=True)
    
    template = 'servicio/servicio.html'
    
    content_panels = Page.content_panels + [
        FieldPanel('tittle'),
        
        FieldPanel('body'),
        FieldPanel('subapartadoslist'),
    ]

    def __str__(self):
        return self.tittle

    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'



class servicioListaPage(Page):
    
    tittle = models.CharField(max_length=100)
    body=RichTextField(blank=True)
    servicioList = StreamField(
        [('servicio', blocks.PageChooserBlock(target_model='servicio.servicio'))],
        blank=True, 
        use_json_field=True
    )
    template = 'servicio/servicioList.html'
    
    content_panels = Page.content_panels + [
        FieldPanel('tittle'),
        
        FieldPanel('body'),
        FieldPanel('servicioList'),
    ]

    def __str__(self): 
        return self.tittle
    
    class  meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        