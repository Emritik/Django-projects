# importing api
from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def index(request):
	
	newsapi = NewsApiClient(api_key ='9069c23c66fb4c9380bd6251d34a29e2')
	top = newsapi.get_top_headlines(sources ='techcrunch, the-verge')

	l = top['articles']
	desc =[]
	news =[]
	img =[]

	for i in range(len(l)):
		f = l[i]
		news.append(f['title'])
		desc.append(f['description'])
		img.append(f['urlToImage'])
	mylist = zip(news, desc, img)

	return render(request, 'index.html', context ={"mylist":mylist})
