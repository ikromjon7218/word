from django.shortcuts import render, redirect
from mainapp.models import Soz, Word, Book
from userapp.models import Profil
from .models import *
from django.utils import timezone

language_1 = ("eng-uzb",)   # model qismi
unit_1 = (3, )
book_1 = (1, )
def query_memorization(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            global language_1, unit_1, book_1
            unit_1 = int(request.POST.get("unit")),
            book_1 = int(request.POST.get("book")),
            language_1 = str(request.POST.get("language")),

            # So'ngi (onlayn) ini yangilash uchun
            profil = Profil.objects.get(user=request.user)
            profil.last_activity = timezone.now()
            profil.save()

            if unit_1[0] < 1:
                return render(request, "query_essential.html",
                              {"success": False, "message": "Unit cannot be less than 1"})
            if unit_1[0] > 30:
                return render(request, "query_essential.html",
                              {"success": False, "message": "The number of unit should not exceed 30"})
            if book_1[0] > 6:
                return render(request, "query_essential.html",
                              {"success": False, "message": "The number of book should not exceed 6"})
            if book_1[0] < 1:
                return render(request, "query_essential.html",
                              {"success": False, "message": "Book cannot be less than 1"})
            Memorization.objects.filter(profil__user=request.user).update(unit=unit_1[0], question_lar="[]", book=book_1,  language=language_1[0])
            return redirect("/test_memorization/")
        try:
            Memorization.objects.get(profil__user=request.user)
        except:
            Memorization.objects.create(profil=Profil.objects.get(user=request.user))
        else:
            Memorization.objects.filter(profil__user=request.user).update(unit=1, question_lar="[]", book=1)
        return render(request, "query_memorization.html", {"success": True, "books": Book.objects.all()})
    return redirect("/")

def test_memorization(request):
    return render(request, "test_memorization.html")
