from django.shortcuts import render


from .models import Article

def year_archive(request, year):
    #this function filters articles published in a given year
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": a_list}
    return render(request, "news/year_archive.html", context)
def month_archive(request, year, month):
    #this function filters articles published in a given year and month
    a_list = Article.objects.filter(pub_date__year=year, pub_date__month=month)
    context = {"year": year, "month":month, "article_list": a_list}
    return render(request, "news/month_archive.html", context)
def article_detail(request, year, month, pk):
    #this function retrieves a specific article by its primary key (pk)
    article = Article.objects.get(pk=pk, pub_date__year=year, pub_date__month=month)
    context = {"year": year, "month": month, "article": article}
    return render(request, "news/article_detail.html", context)


#return HttpResponse("You're looking at question %s." % question_id)