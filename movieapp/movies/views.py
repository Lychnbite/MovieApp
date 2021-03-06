from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.

data = {
    "movies":[
        {
            "title":"film adı 1",
            "description": "film açıklama 1",
            "imageUrl":"m1.jpg",
            "slug":"film-adi-1",
            "language":"english",
            "date": date(2021,10,10)
        },
         {
            "title":"film adı 2",
            "description": "film açıklama 2",
            "imageUrl":"m2.jpg",
            "slug":"film-adi-2",
            "language":"english",
            "date": date(2021,5,10)
        },
         {
            "title":"film adı 3",
            "description": "film açıklama 3",
            "imageUrl":"m3.jpg",
            "slug":"film-adi-3",
            "language":"english",
            "date": date(2021,10,5)
        },
        {
            "title":"film adı 4",
            "description": "film açıklama 4",
            "imageUrl":"m4.jpg",
            "slug":"film-adi-4",
            "language":"english",
            "date": date(2021,10,10)
        },
        {
            "title":"film adı 5",
            "description": "film açıklama 5",
            "imageUrl":"m5.jpg",
            "slug":"film-adi-5",
            "language":"english",
            "date": date(2021,10,10)
        },
        {
            "title":"film adı 6",
            "description": "film açıklama 6",
            "imageUrl":"m6.jpg",
            "slug":"film-adi-6",
            "language":"english",
            "date": date(2021,10,10)
        },

    ],
    "sliders":[]
}



def index(request):
    movies = data["movies"]
    return render(request,"index.html",{
        "movies":movies
    })


def movies(request):

    movies = data["movies"]
    return render(request,"movies.html",{
         "movies":movies,
     })

def movie_details(request,slug):
     return render(request,"movie_details.html",{
         "slug" : slug
     })
