from django.shortcuts import render, redirect
from .models import *
from userapp.models import Profil
from django.utils import timezone

language_1 = ("eng-uzb",)   # model qismi
from_unit_1 = (2,)          # model qismi
to_unit_1 = (4,)            # model qismi
amount_1 = (2,)             # model qismi

def query_post(request):
    global from_unit_1, to_unit_1, amount_1, language_1  # amount_model_id
    from_unit_1 = int(request.POST.get("from_unit")),
    to_unit_1 = int(request.POST.get("to_unit")),
    amount_1 = int(request.POST.get("amount")),
    language_1 = str(request.POST.get("language")),

    # So'ngi (onlayn) ini yangilash uchun
    profil = Profil.objects.get(user=request.user)
    profil.last_activity = timezone.now()
    profil.save()

    if from_unit_1[0] < 0:
        return render(request, "query_essential.html",
                      {"success": False, "message": "Unit cannot be less than 0"})
    if to_unit_1[0] < 1:
        return render(request, "query_essential.html",
                      {"success": False, "message": "Unit cannot be less than 1"})
    elif from_unit_1[0] > to_unit_1[0]:
        return render(request, "query_essential.html",
                      {"success": False, "message": "There is no word between these numbers"})
    if amount_1[0] < 1:
        return render(request, "query_essential.html",
                      {"success": False, "message": "Number of tests cannot be less than 0"})

    # question_lar = models.CharField(max_length=2010)
    # Shuning uchun amount ya'ni testlar soni aniq 250 tadan oshmasligi kerak
    elif amount_1[0] > 250:
        return render(request, "query_essential.html",
                      {"success": False, "message": "The number of tests should not exceed 250"})
    Amount.objects.filter(profil__user=request.user).update(amount=amount_1[0], from_unit=from_unit_1[0],
                                                            to_unit=to_unit_1[0], language=language_1[0],
                                                            question_lar="[]")
    return redirect("/test_essential/")


def query_essential_1(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            return query_post(request=request)
        try:
            Amount.objects.get(profil__user=request.user)
        except:
            Amount.objects.create(profil=Profil.objects.get(user=request.user), book=1)
        else:
            Amount.objects.filter(profil__user=request.user).update(amount_number=1, acceptance=0, question_lar="[]", book=1)
        return render(request, "query_essential.html", {"success": True})
    return redirect('/')

def query_essential_2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            return query_post(request=request)
        try:
            Amount.objects.get(profil__user=request.user)
        except:
            Amount.objects.create(profil=Profil.objects.get(user=request.user), book=1)
        else:
            Amount.objects.filter(profil__user=request.user).update(amount_number=1, acceptance=0, question_lar="[]", book=2)
        return render(request, "query_essential.html", {"success": True})
    return redirect('/')

def query_essential_3(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            return query_post(request=request)
        try:
            Amount.objects.get(profil__user=request.user)
        except:
            Amount.objects.create(profil=Profil.objects.get(user=request.user), book=1)
        else:
            Amount.objects.filter(profil__user=request.user).update(amount_number=1, acceptance=0, question_lar="[]", book=3)
        return render(request, "query_essential.html", {"success": True})
    return redirect('/')
"""
amount_model_id = 1     # model ID si


"""