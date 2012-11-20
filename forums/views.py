from django.views.generic import ListView, DetailView, FormView

from forms import TopicCreateForm, PostCreateForm
from models import Category, Topic, Forum


class CategoryListView(ListView):
    model = Category

class ForumDetailView(DetailView):
    model = Forum

class TopicDetailView(DetailView):
    model = Topic

class TopicCreateView(FormView):
    template_name = 'forums/topic_create.html'
    form_class = TopicCreateForm

    def get_context_data(self, **kwargs):
        context = super(TopicCreateView, self).get_context_data(**kwargs)
        context['forum'] = Forum.objects.get(id=self.kwargs.get('forum_id', None))
        return context


class PostCreateView(FormView):
    template_name = 'forums/post_create.html'
    form_class = PostCreateForm
