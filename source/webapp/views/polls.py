from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PollForm, SearchForm, PollDeleteForm

from webapp.views.base import SearchView

from webapp.models import Poll


class IndexView(SearchView):
     model = Poll
     context_object_name = "polls"
     template_name = "polls/index.html"
     paginate_by = 5
     paginate_orphans = 0
     search_fields = ["title__icontains"]


class PollCreateView(CreateView):
     model = Poll
     form_class = PollForm
     template_name = "polls/create.html"


class PollView(DetailView):
     template_name = 'polls/view.html'
     model = Poll
     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         choices = self.object.choices.order_by("-answer")
         context['choices'] = choices
         return context


class PollUpdateView(UpdateView):
     form_class = PollForm
     template_name = "polls/update.html"
     model = Poll


class PollDeleteView(DeleteView):
    model = Poll
    template_name = "polls/delete.html"
    success_url = reverse_lazy('index')
    form_class = PollDeleteForm

    def get_form_kwargs(self):
         kwargs = super().get_form_kwargs()
         if self.request.method == "POST":
             kwargs['instance'] = self.object
         return kwargs