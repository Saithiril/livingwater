from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from news.models import Topic, Comment
from news.forms import addTopic
from django.utils import timezone

def news(request):
	list_news = Topic.objects.all().order_by('-pub_date')[:5]
	return render_to_response('news/base_news.html', {'news':list_news}, context_instance = RequestContext(request))

def detail(request, news_id):
	news = get_object_or_404(Topic, pk=news_id)
	return render_to_response('news/detail.html', {'news':news}, context_instance = RequestContext(request))

def delete(request, news_id):
	news = get_object_or_404(Topic, pk=news_id)
	news.delete()
	return HttpResponseRedirect('/news')
	
def add(request):
	if request.user.is_authenticated() and request.user.has_perm('news.can_change'):
		form = addTopic()
		return render_to_response('news/add.html', {'form': form}, context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect("/home")

def addComplete(request):
	title = request.POST['title']
	text = request.POST['text']
	form = addTopic({'title': title, 'text': text})
	if form.is_valid():
		topic = Topic(title=form.cleaned_data['title'], text=form.cleaned_data['text'], pub_date=timezone.now(), author=request.user)
		topic.save()
	return HttpResponseRedirect('/news')