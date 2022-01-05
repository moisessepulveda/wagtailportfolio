from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

class HomePage(Page):
    # hero fields
    name = models.CharField("Nombre", max_length=100, null=True)
    profession = models.CharField("Profesión", max_length=100, null=True)
    age = models.IntegerField("Edad", default=18)
    phone = models.CharField("Teléfono", null=True, max_length=100)
    email = models.EmailField("Correo electrónico", null=True)
    address = models.CharField("Dirección", max_length=200, null=True)

    github_link = models.URLField("Enlace de github", null=True, blank=True)
    linkedin_link = models.URLField("Enlace linked IN", null=True, blank=True)
    facebook_link = models.URLField("Enlace de facebook", null=True, blank=True)
    
    hero_picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Foto",
        related_name='+'
    )
    # hero fields end

    # presentation fields

    presentation_title = models.CharField("Título", max_length=50, null=True)
    presentation_desc = models.TextField("Descripción", null=True)

    cv_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Archivo de curriculum",
        related_name='+'
    )
    # presentation fields end
    
    # resume fields
    resume_title = models.CharField("Título", max_length=50, default="")
    resume_body = RichTextField("Cuerpo", null=True)

    education = StreamField([
     ('item', blocks.StructBlock([
         ('university', blocks.CharBlock(label="Universidad/Instituto")),
         ('period', blocks.CharBlock(label="Periodo")),
         ('title', blocks.TextBlock(label="Descripción")),
     ])),
    ])

    job_history = StreamField([
     ('trabajo', blocks.StructBlock([
         ('enterprise', blocks.CharBlock(label="Empresa")),
         ('period', blocks.CharBlock(label="Periodo")),
         ('description', blocks.TextBlock(label="Descripción")),
     ])),
    ])

    skills = StreamField([
     ('habilidades', blocks.StructBlock([
         ('technology', blocks.CharBlock(label="Tecnología")),
         ('percentage', blocks.CharBlock(label="Porcentaje")),
     ])),
    ])

    # resume fields end

    # proyects fields
    project_title = models.CharField("Titulo", max_length=50, default="Mis Proyectos_")
    projects = StreamField([
     ('project', blocks.StructBlock([
        ('title', blocks.CharBlock(label="Título")),
        ('image', ImageChooserBlock(label="Imagen")),
        ('summary', blocks.TextBlock(label="Resumen")),
        ('descripcion', blocks.TextBlock(label="Descripción")),
     ])),
    ])


    # proyects field end

    # content panels

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('name', classname="title"),
            FieldPanel('profession', classname="full"),
            FieldPanel('age', classname="full"),
            FieldPanel('phone', classname="full"),
            FieldPanel('email', classname="full"),
            FieldPanel('address', classname="full"),
            ImageChooserPanel('hero_picture'),
        ], heading="Hero"),
        MultiFieldPanel([
            FieldPanel('presentation_title'),
            FieldPanel('presentation_desc'),
            DocumentChooserPanel("cv_file")
        ], heading="Presentación"),
        MultiFieldPanel([
            FieldPanel('resume_title', classname="title"),
            FieldPanel('resume_body', classname="full"),
            StreamFieldPanel("education"),
            StreamFieldPanel("job_history"),
            StreamFieldPanel("skills")
        ], heading="Curriculum", classname="collapsible collapsed"),
        MultiFieldPanel([
            FieldPanel('project_title', classname="title"),
            StreamFieldPanel("projects")
        ], heading="Proyectos", classname="collapsible collapsed")
        
    ]