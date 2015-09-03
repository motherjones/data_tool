from django.views.generic.base import TemplateView


class IndexPage(TemplateView):
    template_name = 'data_server/index-page.html'
