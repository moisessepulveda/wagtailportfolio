from django.db import models

# Create your models here.
from wagtail.admin import blocks
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField


class SimpleListPage(Page):
    hero_title = models.CharField(max_length=50, verbose_name="Título", default="Simple list", )
    hero_changing_words = models.CharField(
        max_length=100,
        verbose_name="Secuencia de palabras",
        help_text="Separadas por ','",
        default="útil, todo terreno",
    )
    hero_subtitle = models.CharField(
        max_length=100,
        verbose_name="Subtítulo",
        default="Simple list te permitirá llevar el calculo de tu compra en todo momento",
    )

    app_store_url = models.URLField(null=True, blank=True, verbose_name="URL App store")
    gplay_url = models.URLField(null=True, blank=True, verbose_name="URL de Google Play")

    title_section1 = models.CharField(max_length=50, default="", verbose_name="Titulo sección 1")
    description_section1 = RichTextField(default='', verbose_name="Descripción sección 1")

    title_section2 = models.CharField(max_length=50, default="", verbose_name="Titulo sección 2")
    description_section2 = RichTextField(default='', verbose_name="Descripción sección 2")

    title_section3 = models.CharField(max_length=50, default="", verbose_name="Titulo sección 3")
    subtitle_section3 = models.CharField(max_length=50, default="", verbose_name="Subtítulo sección 3")
    description_section3 = RichTextField(default='', verbose_name="Descripción sección 3")

    download_caption = models.CharField(
        max_length=80,
        verbose_name="Descripción descarga",
        default='',
        null=True,
        blank=True,
    )

    footer_title = models.CharField(max_length=20, default='', verbose_name='Título del footer')
    footer_desc = models.TextField(default='', verbose_name='Descripción del footer')
    footer_link_label = models.CharField(max_length=20, verbose_name='Etiqueta enlace', default='Enlaces')

    footer_urls = StreamField([
        ('url', blocks.StructBlock([
            ('label', blocks.CharBlock(max_length=50, label="Etiqueta")),
            ('urls', blocks.URLBlock(label="URL")),
        ], label="URL"))
    ], default='', null=True, blank=True, )

    footer_copyright = models.CharField(max_length=50, default='', null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_title'),
            FieldPanel('hero_changing_words'),
            FieldPanel('hero_subtitle'),
            MultiFieldPanel([
                FieldPanel('app_store_url'),
                FieldPanel('gplay_url'),
            ], heading='Enlaces', classname="collapsible collapsed")
        ], heading="Sección principal"),
        MultiFieldPanel([
            MultiFieldPanel([
                FieldPanel('title_section1'),
                FieldPanel('description_section1'),
            ]),
            MultiFieldPanel([
                FieldPanel('title_section2'),
                FieldPanel('description_section2')
            ]),
            MultiFieldPanel([
                FieldPanel('title_section3'),
                FieldPanel('subtitle_section3'),
                FieldPanel('description_section3')
            ]),
            MultiFieldPanel([
                FieldPanel('download_caption'),
            ]),
        ], heading="características"),
        MultiFieldPanel([
            FieldPanel('footer_title'),
            FieldPanel('footer_desc'),
            FieldPanel('footer_link_label'),
            StreamFieldPanel('footer_urls'),
            FieldPanel('footer_copyright'),
        ], heading='Pie de página'),
    ]

    subpage_types = ['simplelist.TermsPage']

    def hero_changing_words_as_list(self):
        return self.hero_changing_words.split(',')


class TermsPage(Page):
    content = RichTextField(verbose_name='Contenido')

    class Meta:
        verbose_name = 'Página de terminos'

    parent_page_types = ['simplelist.SimpleListPage']

    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]
