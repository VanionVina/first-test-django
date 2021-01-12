from django.contrib.auth.models import ContentType
from django.views.generic import View

from mainapp.models import GlobalCategory


class GetCategorysMixin(View):

    def dispatch(self, request, *args, **kwargs):
        self.g_categorys = GlobalCategory.objects.all()
        return super().dispatch(request, *args, **kwargs)

