from django.shortcuts import render, redirect
from .models import *
from userapp.models import Profil
from .eng_uzb import eng_uzb
from .uzb_eng import uzb_eng
from django.db.models import F
from django.utils import timezone

def test_essential(request):
    if request.user.is_authenticated:
        profil = Profil.objects.get(user=request.user)
        profil.last_activity = timezone.now()
        profil.save()

        if request.method == "POST":
            amount = Amount.objects.filter(profil__user=request.user)
            if amount[0].language == "eng-uzb":
                soz = request.POST.get('soz')
                if soz:
                    respons = Soz.objects.filter(name=soz)[0]
                    q_s = amount[0].question_soz

                    question_lar_1 = eval(amount[0].question_lar)

                    if respons.word.name == Word.objects.get(id=q_s).name:
                        amount.update(acceptance=F('acceptance') + 1)

                        # Har bir testni {q_s: "t") ya'ni qaysi so'zni topgan topmaganini yozib ketadi
                        question_lar_1.append(q_s)
                        question_lar_1.append("t")
                        amount.update(question_lar=question_lar_1)
                    else:
                        Profil.objects.filter(user=request.user).update(rejection=F('rejection') + 0.5)

                        # Har bir testni {q_s: "f") ya'ni qaysi so'zni topgan topmaganini yozib ketadi
                        question_lar_1.append(q_s)
                        question_lar_1.append("f")
                        amount.update(question_lar=question_lar_1)
                eng_uzb(request=request)

            elif amount[0].language == "uzb-eng":
                soz = request.POST.get('soz')
                if soz:
                    q_s = amount[0].question_soz

                    question_lar_1 = eval(amount[0].question_lar)

                    if soz == Soz.objects.get(id=q_s).word.name:
                        amount.update(acceptance=F('acceptance') + 1)

                        # Har bir testni {q_s: "t") ya'ni qaysi so'zni topgan topmaganini yozib ketadi
                        question_lar_1.append(q_s)
                        question_lar_1.append("t")
                        amount.update(question_lar=question_lar_1)
                    else:
                        Profil.objects.filter(user=request.user).update(rejection=F('rejection') + 0.5)

                        # Har bir testni {q_s: "f") ya'ni qaysi so'zni topgan topmaganini yozib ketadi
                        question_lar_1.append(q_s)
                        question_lar_1.append("f")
                        amount.update(question_lar=question_lar_1)
                uzb_eng(request=request)

        # Agar testlar soni marta test yechib bo'lgan bo'lsa o'yinni tugatish uchun:
        amount = Amount.objects.filter(profil__user=request.user)
        if amount[0].amount < amount[0].amount_number:
            return redirect('/result/')

        if amount[0].language == "eng-uzb":
            return render(request, "test_essential.html", eng_uzb(request=request))

        elif amount[0].language == "uzb-eng":
            return render(request, "test_essential.html", uzb_eng(request=request))

    return redirect('/')


"""
number = Amount.objects.get(id=amount_model_id).amount_number
Amount.objects.get(id=amount_model_id).update(amount_number=number + 1)
print(Soz.objects.get(name=request.POST.get("soz")).word.name, question_soz.name, "1_POST")

return render(request, "test_essential.html", {"word": language, "soz": language})

number = Amount.objects.get(id=amount_model_id).amount_number
Amount.objects.get(id=amount_model_id).update(amount_number=number + 1)
print(Soz.objects.get(name=request.POST.get("soz")).word.name, question_soz.name, "1_POST")
"""