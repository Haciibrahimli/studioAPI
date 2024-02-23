from modeltranslation.translator import TranslationOptions, register
from my_app.models import About,Team,OurServices,BlogCategory,Blog,Projects
                          

@register(About)
class AboutTranslation(TranslationOptions):
    fields = ("subject1","subject2", )

@register(Team)
class TeamTranslation(TranslationOptions):
    fields = ("name","profession", )

@register(OurServices)
class OurServicesTranslation(TranslationOptions):
    fields = ("name","text",)

@register(BlogCategory)
class BlogCategoryTranslation(TranslationOptions):
    fields = ("name", )

@register(Blog)
class BlogTranslation(TranslationOptions):
    fields = ("title", "information", "blog_category", )

@register(Projects)
class ProjectsTranslation(TranslationOptions):
    fields = ("name", "project_category", "text", )


