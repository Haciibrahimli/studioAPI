from django.contrib import admin
from my_app.models import *
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline


# class AboutAdmin(admin.StackedInline):
#     model = About
#     extra = 1

# @admin.register(About)
# class AboutAdmin(TranslationAdmin):
#     inlines = [AboutAdmin]

#     class Media:
#         js = (

#             'modeltranslation/js/tabbed_translation_fields.js',
#             'modeltranslation/js/force_jquery.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
#         )

#         css = {
#             'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#         }

# @admin.register(BlogCategory)
# class BlogCategoryAdmin(TranslationAdmin):
#      class Media:
#         js = (

#             'modeltranslation/js/tabbed_translation_fields.js',
#             'modeltranslation/js/force_jquery.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
#         )

#         css = {
#             'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#         }



# class BlogCategory(TranslationAdmin):
#     inlines = [BlogCategory]






admin.site.register(Blog)
admin.site.register(BlogCategory)
admin.site.register(About)
admin.site.register(OurServices)
admin.site.register(MainDetails)
admin.site.register(Contact)
admin.site.register(Partniors)
admin.site.register(Projects)
admin.site.register(Team)
admin.site.register(SosialMedia)
