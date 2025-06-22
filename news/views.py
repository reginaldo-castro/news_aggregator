from django.shortcuts import render
import requests
from django.conf import settings
from datetime import datetime, timedelta
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def news_list(request):
    query = request.GET.get('q', '').strip()
    page_number = request.GET.get('page')
    from_date = request.GET.get('from')
    to_date = request.GET.get('to')
    source = request.GET.get('source', '').strip()

    is_search = bool(query) or bool(source)

    if is_search:
        url = 'https://newsapi.org/v2/everything'
        params = {
            'apiKey': settings.NEWS_API_KEY,
            'pageSize': 20,
            'page': page_number or 1,
        }
        if query:
            params['q'] = query
        if source:
            params['sources'] = source

        if from_date:
            params['from'] = from_date
        if to_date:
            params['to'] = to_date
    else:
        url = 'https://newsapi.org/v2/top-headlines'
        params = {
            'country': 'us',
            'apiKey': settings.NEWS_API_KEY,
            'pageSize': 20,
            'page': page_number or 1,
        }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get('status') != 'ok':
        articles = []
        error_message = data.get('message', 'Erro ao buscar dados')
    else:
        articles = data.get('articles', [])
        error_message = None

    for article in articles:
        published_at = article.get('publishedAt')
        if published_at:
            try:
                article['formatted_publishedAt'] = datetime.fromisoformat(published_at[:-1]).strftime('%d-%m-%Y %H:%M:%S')
            except Exception:
                article['formatted_publishedAt'] = published_at

    paginator = Paginator(articles, 5)
    page_obj = paginator.get_page(page_number)

    context = {
        'articles': articles,
        'query': query,
        'page_obj': page_obj,
        'from_date': from_date,
        'to_date': to_date,
        'source': source,
        'error_message': error_message,
    }

    return render(request, 'news/news_list.html', context)
