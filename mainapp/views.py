from django.shortcuts import render, redirect
from .models import *
from userapp.models import Profil
import random
from django.db.models import F

# def custom_404(request, exception):
#     # do something
#     return render(request, '404.html', status=404)
"""
1) Bitta chiqqan so'z qaytib chiqmasligi kerak agar to'g'ri javobini topgan bo'lsa,         LATER
    agar amount dan katta bo'lmasa                                                          LATER
2) javoblardagi so'zlar orasida bitta right_1 to'g'ri so'zi keyin tasodifiy so'zlarni                   OK
    orasida ham to'g'ri so'z qo'shilib qolib, to'g'ri so'z ikkita variantda bo'lib qolyapti.            OK
3) 3 marta yordam (lampochka) bo'lishi kerak.                                                LATER 
4) Resultda xato qilgan so'zlari chiqishi kerak.                                             LATER
5) about degan linkda 'bitta account egasi bir vaqtda faqat bitta qurilmadan test                       OK
    yechsa bo'ladi' deb yozish kerak                                                                    OK
6) Har oynani o'ng tomoniga settings linki bo'lishi kerak.                                              OK
7) /about/   Men haqimda chiqishi kerak.  <a> link ham qo'yib ketishim kerak.                           OK

amount_instance = Amount.objects.get(id=1)
amount_instance.error = [1, 2, 3] # ma'lumotni qo'shish
amount_instance.save() #

amount_instance = Amount.objects.get(id=1)
my_error_list = amount_instance.error
print(my_error_list[0])
"""


def error(request):
    return render(request, "error.html")
try:
    def home_page(request):
        if request.user.is_authenticated:
            return render(request, "home_page.html")
        return redirect('/')
    def essential_english_words(request):
        if request.user.is_authenticated:
            return render(request, "essential_english_words.html")
        return redirect('/')

    language_1 = ("eng-uzb", )  # model qismi
    from_unit_1 = (2, )         # model qismi
    to_unit_1 = (4, )           # model qismi
    amount_1 = (2, )            # model qismi
    # amount_model_id = 1     # model ID si

    def query_essential_1(request):
        if request.user.is_authenticated:
            if request.method == "POST":
                global from_unit_1, to_unit_1, amount_1, language_1     # amount_model_id
                from_unit_1 = int(request.POST.get("from_unit")),
                to_unit_1 = int(request.POST.get("to_unit")),
                amount_1 = int(request.POST.get("amount")),
                language_1 = str(request.POST.get("language")),
                if from_unit_1[0] < 0:
                    return render(request, "query_essential_1.html", {"success": False, "message": "Unit cannot be less than 0"})
                if to_unit_1[0] < 1:
                    return render(request, "query_essential_1.html", {"success": False, "message": "Unit cannot be less than 1"})
                elif from_unit_1[0] > to_unit_1[0]:
                    return render(request, "query_essential_1.html", {"success": False, "message": "There is no word between these numbers"})
                if amount_1[0] < 1:
                    return render(request, "query_essential_1.html", {"success": False, "message": "Number of tests cannot be less than 0"})
                Amount.objects.filter(profil__user=request.user).update(amount=amount_1[0], from_unit=from_unit_1[0],
                        to_unit=to_unit_1[0], language=language_1[0])


                return redirect("/test_1_essential/")
            try: Amount.objects.get(profil__user=request.user)
            except: Amount.objects.create(profil=Profil.objects.get(user=request.user))
            else: Amount.objects.filter(profil__user=request.user).update(amount_number=1, acceptance=0)
            return render(request, "query_essential_1.html", {"success": True})
        return redirect('/')

    def eng_uzb(request):
        from_u = Amount.objects.get(profil__user=request.user).from_unit
        to_u = Amount.objects.get(profil__user=request.user).to_unit

        q_s = Word.objects.filter(unit__range=(from_u, to_u), book=1).order_by('?').first().id
        Amount.objects.filter(profil__user=request.user).update(question_soz=q_s)

        respons = Soz.objects.filter(word__unit__range=(from_u, to_u), word__book=1).order_by('?')

        data = {"soz_1": respons[1],
                "soz_2": respons[2],
                "soz_3": respons[3], }
        if Soz.objects.filter(word=Word.objects.get(id=q_s))[0].name != respons[1] and Soz.objects.filter(word=Word.objects.get(id=q_s))[0].name != respons[2] and Soz.objects.filter(word=Word.objects.get(id=q_s))[0].name != respons[3]:
            keys = list(data.keys())
            right_1 = random.choice(keys)
            data[right_1] = Soz.objects.filter(word=Word.objects.get(id=q_s))[0].name

        data['word'] = Word.objects.get(id=q_s)
        data['amount'] = Amount.objects.get(profil__user=request.user).amount
        data['acceptance'] = Amount.objects.get(profil__user=request.user).acceptance
        data['amount_number'] = Amount.objects.get(profil__user=request.user).amount_number

        Amount.objects.filter(profil__user=request.user).update(amount_number=F('amount_number') + 0.5)
        return data

    def uzb_eng(request):
        from_u = Amount.objects.get(profil__user=request.user).from_unit
        to_u = Amount.objects.get(profil__user=request.user).to_unit

        q_s = Soz.objects.filter(word__unit__range=(from_u, to_u), word__book=1).order_by('?').first().id
        Amount.objects.filter(profil__user=request.user).update(question_soz=q_s)

        respons = Word.objects.filter(unit__range=(from_u, to_u), book=1).order_by('?')
        data = {"soz_1": respons[1],
                "soz_2": respons[2],
                "soz_3": respons[3], }
        keys = list(data.keys())
        right_1 = random.choice(keys)
        data[right_1] = Soz.objects.get(id=q_s).word
        data['word'] = Soz.objects.get(id=q_s)
        data['amount'] = Amount.objects.get(profil__user=request.user).amount
        data['acceptance'] = Amount.objects.get(profil__user=request.user).acceptance
        data['amount_number'] = Amount.objects.get(profil__user=request.user).amount_number

        Amount.objects.filter(profil__user=request.user).update(amount_number=F('amount_number') + 0.5)
        return data

    def test_1_essential(request):
        if request.user.is_authenticated:
            if request.method == "POST":
                if Amount.objects.get(profil__user=request.user).language == "eng-uzb":
                    soz = request.POST.get('soz')
                    if soz:
                        respons = Soz.objects.filter(name=soz)[0]
                        q_s = Amount.objects.get(profil__user=request.user).question_soz
                        if respons.word.name == Word.objects.get(id=q_s).name:
                            Amount.objects.filter(profil__user=request.user).update(acceptance=F('acceptance') + 1)
                        else: Profil.objects.filter(user=request.user).update(rejection=F('rejection') + 0.5)
                    # number = Amount.objects.get(id=amount_model_id).amount_number
                    # Amount.objects.get(id=amount_model_id).update(amount_number=number + 1)
                    # print(Soz.objects.get(name=request.POST.get("soz")).word.name, question_soz.name, "1_POST")
                    eng_uzb(request=request)

                elif Amount.objects.get(profil__user=request.user).language == "uzb-eng":
                    soz = request.POST.get('soz')
                    if soz:
                        q_s = Amount.objects.get(profil__user=request.user).question_soz
                        if soz == Soz.objects.get(id=q_s).word.name:
                            Amount.objects.filter(profil__user=request.user).update(acceptance=F('acceptance') + 1)
                        else: Profil.objects.filter(user=request.user).update(rejection=F('rejection') + 0.5)

                    # number = Amount.objects.get(id=amount_model_id).amount_number
                    # Amount.objects.get(id=amount_model_id).update(amount_number=number + 1)
                    # print(Soz.objects.get(name=request.POST.get("soz")).word.name, question_soz.name, "1_POST")
                    uzb_eng(request=request)
            if Amount.objects.get(profil__user=request.user).amount < Amount.objects.get(profil__user=request.user).amount_number:
                return redirect('/result/')
            if Amount.objects.get(profil__user=request.user).language == "eng-uzb":
                return render(request, "test_1_essential.html", eng_uzb(request=request))
            elif Amount.objects.get(profil__user=request.user).language == "uzb-eng":
                return render(request, "test_1_essential.html", uzb_eng(request=request))

            # return render(request, "test_1_essential.html", {"word": language, "soz": language})
        return redirect('/')

    def result(request):
        if request.user.is_authenticated:

            amo = Amount.objects.get(profil__user=request.user)
            pr = Profil.objects.get(user=request.user)
            pr.test += amo.amount
            pr.acceptance += amo.acceptance
            pr.save()
            data = {"amount": amo.amount,
                    "language": amo.language,
                    "acceptance": amo.acceptance,
                    "percentage": amo.acceptance * 100 / amo.amount * 1000 // 1000}
            return render(request, "result.html", data)
        return redirect('/')
    def settings(request):
        if request.user.is_authenticated:
            if request.method == "POST":
                Profil.objects.filter(user=request.user).update(
                    name=request.POST.get("name"),
                    tel_number=request.POST.get('tel_number'),
                    year_of_birth=request.POST.get('year_of_birth'))
                return redirect('/home_page/')
            pr = Profil.objects.get(user=request.user)
            if pr.test != 0 and pr.acceptance != 0:
                data = {"i": pr, "p": f"{pr.acceptance * 100 / pr.test * 1000 // 1000} %"}
                return render(request, "settings.html", data)
            data = {"i": pr, "p":  "You haven't taken the test yet"}
            return render(request, "settings.html", data)
        return redirect('/')
    def about(request):
        return render(request, "about.html")
except: redirect('/error/')
