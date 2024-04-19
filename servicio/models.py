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
class Card(Pg):
    tittle=models.CharField(max_length=100)
    body=RichTextField(
        
    )
    template='cards/card.html'
    panels = [
        FieldPanel('tittle'),
        FieldPanel('body'),
    ]
    
    def __str__(self):
        return self.tittle

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


class CardPage(Page):
    """
    A Page that features a single card.
    """
    card = models.ForeignKey(
        'servicio.Card',
        on_delete=models.PROTECT,
        related_name='+',
        help_text='The card to display on this page.',
    )

    content_panels = Page.content_panels + [
        PageChooserPanel('card', [Card])
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
        context['card'] = self.card
        return context

""" class subapartados (set of  card) """
class subapartados(Page):
    """
    subapartados(cardlist) 
    """
    tittle = models.CharField(max_length=100)
    cardlist = StreamField([('card', blocks.PageChooserBlock(target_model='servicio.CardPage'))], blank=True)
  
    
#    template
    template='servicio/subapartados.html'

    panels = [
        FieldPanel('tittle'),
        FieldPanel('cardlist'),
    ]

    def __str__(self):
        return self.tittle

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
    
"""
Class servicio(subapartadoslist) 
"""
class servicio(Page):
    """
    servicio(subapartadoslist) 
    """
    tittle = models.CharField(max_length=100)
    subapartadoslist = StreamField([('subapartados', blocks.PageChooserBlock(target_model='servicio.subapartados'))], blank=True)
    
    template = 'servicio/servicio.html'
    
    content_panels = Page.content_panels + [
        FieldPanel('tittle'),
        FieldPanel('subapartadoslist'),
    ]

    def __str__(self):
        return self.tittle


