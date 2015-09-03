from django.views.generic.base import TemplateView
from braces.views import LoginRequiredMixin

class IndexPage(LoginRequiredMixin,TemplateView):
    template_name = 'data_server/index-page.html'
