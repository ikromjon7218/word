from django.shortcuts import render, redirect
from userapp.models import Profil
from django.utils import timezone
from .models import Amount
def error(request):
    return render(request, "error.html")


def play_again(request):
    if request.user.is_authenticated:
        if Amount.objects.get(profil__user=request.user).book == 1:
            return redirect("/query_essential_1/")
        if Amount.objects.get(profil__user=request.user).book == 2:
            return redirect("/query_essential_2/")
        if Amount.objects.get(profil__user=request.user).book == 3:
            return redirect("/query_essential_3/")
try:
    def home_page(request):
        if request.user.is_authenticated:

            profil = Profil.objects.get(user=request.user)
            profil.last_activity = timezone.now()
            profil.save()

            return render(request, "home_page.html", {"name": profil.name})
        return redirect('/')

    def essential_english_words(request):
        if request.user.is_authenticated:

            profil = Profil.objects.get(user=request.user)
            profil.last_activity = timezone.now()
            profil.save()

            return render(request, "essential_english_words.html")
        return redirect('/')

    def settings(request):
        if request.user.is_authenticated:

            profil = Profil.objects.get(user=request.user)
            profil.last_activity = timezone.now()
            profil.save()

            if request.method == "POST":
                Profil.objects.filter(user=request.user).update(
                    name=request.POST.get("name"),
                    tel_number=request.POST.get('tel_number'),
                    year_of_birth=request.POST.get('year_of_birth'))
                return redirect('/home_page/')

            pr = Profil.objects.get(user=request.user)
            if pr.test != 0:
                data = {"i": pr}
                return render(request, "settings.html", data)
            data = {"i": pr, "p":  "You haven't taken the test yet"}
            return render(request, "settings.html", data)
        return redirect('/')

    def about(request):

        profil = Profil.objects.get(user=request.user)
        profil.last_activity = timezone.now()
        profil.save()

        return render(request, "about.html")
except:
    redirect('/error/')

