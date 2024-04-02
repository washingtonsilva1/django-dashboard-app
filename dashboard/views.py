from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


# class DashboardGenericView(View):
#     login_url = reverse_lazy('')

class DashboardHomeView(TemplateView):
    template_name = 'dashboard/dashboard_index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx
