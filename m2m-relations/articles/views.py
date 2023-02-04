from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {"object_list": Article.objects.all()}

    for article in context["object_list"]:
        print(vars(article))
        print("---")
        print(article.scopes)
        print("===")
        for scope in article.scopes.all():
            print(scope.tag)
            print("+++")



    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = '-published_at'

    return render(request, template, context)