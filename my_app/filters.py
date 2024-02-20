from my_app.models import Blog

import django_filters


class BlogFilter(django_filters.FilterSet):
    class Meta:
        model = Blog
        fields = ('blog_category', )