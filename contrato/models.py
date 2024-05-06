
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
class contratPage(Page):
    tittle = models.CharField(max_length=100)
    body=RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('tittle'),
        FieldPanel('body'),
    ]
    
    template = 'contrato/contratPage.html'

    