from django.shortcuts import render
from django.contrib.auth import logout
from .forms import QueryForm,UpdateForm
from .models import Calender
from administer.models import RequestList
from django.http import HttpResponse
import datetime
import re


def search(request):
    if request.method == "POST":
        form = QueryForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False)
            sport = form.cleaned_data['sport']
            month = form.cleaned_data['month']
            if str(sport) == "--" or str(month) == "--":
                return render(request, 'main/home.html', {'err_mssg': 'Select Both Fields'})
            else:
                calenders = Calender.objects.filter(sport=sport, month=month)
                s = str(datetime.datetime.now().date())
                print(s)
                result = re.findall('([0-9]+)-([0-9]+)-([0-9]+)', s)
                a, b, c = result[0]
                present_month = int(b)
                present_date = int(c)

                return render(request, 'main/search.html', {'calenders': calenders, 'present_month': present_month,
                                                            'present_date': present_date})
        context = {
            "form": form,
        }
        return render(request, 'main/home.html', context)
    else:
        return render(request, 'main/home.html')


def select_date(request, date_id):
    selected_date = Calender.objects.get(pk=date_id)
    return render(request, 'main/slot_booking.html', {'selected_date': selected_date})


def update(request, object_id):
    if request.method == "POST":
        form = UpdateForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False)
            check_1 = form.cleaned_data['check_1']
            check_2 = form.cleaned_data['check_2']
            check_3 = form.cleaned_data['check_3']
            check_4 = form.cleaned_data['check_4']
            check_5 = form.cleaned_data['check_5']
            check_6 = form.cleaned_data['check_6']
            check_7 = form.cleaned_data['check_7']
            check_8 = form.cleaned_data['check_8']
            check_9 = form.cleaned_data['check_9']
            check_10 = form.cleaned_data['check_10']
            check_11 = form.cleaned_data['check_11']
            check_12 = form.cleaned_data['check_12']
            check_13 = form.cleaned_data['check_13']
            check_14 = form.cleaned_data['check_14']
            check_15 = form.cleaned_data['check_15']
            check_16 = form.cleaned_data['check_16']
            purpose = form.cleaned_data['purpose']

            object1 = Calender.objects.get(pk=object_id)
            object2 = RequestList.objects.create(username=request.user.username, sport1=object1.sport,
                                                 month1=object1.month, date1=object1.date, purpose=purpose,
                                                 date2=datetime.datetime.now())
            counter = 0
            if check_1 == "Select":
                if object1.check_1 == "2":
                    object2.delete()
                    return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg_1': 'Slot Already Booked'})
                else:
                    object1.check_1 = "1"
                    object2.check_1 = "1"
                    counter = 1

            if check_2 == "Select":
                if object1.check_2 == "2":
                    object2.delete()
                    return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg_1': 'Slot Already Booked'})
                else:
                    object1.check_2 = "1"
                    object2.check_2 = "1"
                    counter = 1
            if check_3 == "Select":
                if object1.check_3 == "2":
                    object2.delete()
                    return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg_1': 'Slot Already Booked'})
                else:
                    object1.check_3 = "1"
                    object2.check_3 = "1"
                    counter = 1
            if check_4 == "Select":
                if object1.check_4 == "2":
                    object2.delete()
                    return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg_1': 'Slot Already Booked'})
                else:
                    object1.check_4 = "1"
                    object2.check_4 = "1"
                    counter = 1
            if check_5 == "Select":
                if object1.check_5 == "2":
                    object2.delete()
                    return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg_1': 'Slot Already Booked'})
                else:
                    object1.check_5 = "1"
                    object2.check_5 = "1"
                    counter = 1
            if check_6 == "Select":
                if object1.check_6 == "2":
                    object2.delete()
                    return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg_1': 'Slot Already Booked'})
                else:
                    object1.check_6 = "1"
                    object2.check_6 = "1"
                    counter = 1
            if check_7 == "Select":
                if object1.check_7 == "2":
                    object2.delete()
                    return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg_1': 'Slot Already Booked'})
                else:
                    object1.check_7 = "1"
                    object2.check_7 = "1"
                    counter = 1
            if check_8 == "Select":
                if object1.check_8 == "2":
                    object2.delete()
                    return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg_1': 'Slot Already Booked'})
                else:
                    object1.check_8 = "1"
                    object2.check_8 = "1"
                    counter = 1
            if check_9 == "Select":
                if object1.check_9 == "2":
                    object2.delete()
                    return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg_1': 'Slot Already Booked'})
                else:
                    object1.check_9 = "1"
                    object2.check_9 = "1"
                    counter = 1
            if check_10 == "Select":
                if object1.check_10 == "2":
                    object2.delete()
                    return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg_1': 'Slot Already Booked'})
                else:
                    object1.check_10 = "1"
                    object2.check_10 = "1"
                    counter = 1
            if check_11 == "Select":
                if object1.check_11 == "2":
                    object2.delete()
                    return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg_1': 'Slot Already Booked'})
                else:
                    object1.check_11 = "1"
                    object2.check_11 = "1"
                    counter = 1
            if check_12 == "Select":
                if object1.check_12 == "2":
                    object2.delete()
                    return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg_1': 'Slot Already Booked'})
                else:
                    object1.check_12 = "1"
                    object2.check_12 = "1"
                    counter = 1
            if check_13 == "Select":
                if object1.check_13 == "2":
                    object2.delete()
                    return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg': 'Slot Already Booked'})
                else:
                    object1.check_13 = "1"
                    object2.check_13 = "1"
                    counter = 1
            if check_14 == "Select":
                if object1.check_14 == "2":
                    object2.delete()
                    return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg_1': 'Slot Already Booked'})
                else:
                    object1.check_14 = "1"
                    object2.check_14 = "1"
                    counter = 1
            if check_15 == "Select":
                if object1.check_15 == "2":
                    object2.delete()
                    return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg_1': 'Slot Already Booked'})
                else:
                    object1.check_15 = "1"
                    object2.check_15 = "1"
                    counter = 1
            if check_16 == "Select":
                if object1.check_16 == "2":
                    object2.delete()
                    return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg_1': 'Slot Already Booked'})
                else:
                    object1.check_16 = "1"
                    object2.check_16 = "1"
                    counter = 1

            if counter == 1:
                # print("hii")
                object1.save()
                object2.save()
                return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg': 'Request Sent'})
            else:
                object2.delete()
                return render(request, 'main/slot_booking.html', {'selected_date': object1, 'mssg_1': 'Please select atleast one slot'})

        else:
            print(form.errors)
        selected_date = Calender.objects.get(pk=object_id)
        context = {
            "form": form,
            "selected_date": selected_date
        }
        return render(request, 'main/slot_booking.html', context)


# def calender(request):
#     n = 12
#     for i in range(1, n+1, 1):
#         if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
#             m = 31
#         elif i == 4 or i == 6 or i == 9 or i == 11:
#             m = 30
#         else:
#             m = 28
#         for j in range(1, m + 1, 1):
#             Calender.objects.create(sport="Cricket", month=str(i), date=str(j))
#             Calender.objects.create(sport="Tennis", month=str(i), date=str(j))
#             Calender.objects.create(sport="Badminton", month=str(i), date=str(j))
#             Calender.objects.create(sport="Basketball", month=str(i), date=str(j))
#             Calender.objects.create(sport="Athletic Ground", month=str(i), date=str(j))
#             Calender.objects.create(sport="Volleyball", month=str(i), date=str(j))
#             Calender.objects.create(sport="Hockey", month=str(i), date=str(j))
#             Calender.objects.create(sport="Football", month=str(i), date=str(j))
#
#     return render(request, 'main/home.html')
#
#
# def delete_calender(request):
#     Calender.objects.all().delete()
#     return render(request, 'main/home.html')


def notify(request):
    combined_queryset = RequestList.objects.filter(username=request.user.username, status="Approved") | RequestList.objects.filter(username=request.user.username, status="Rejected") | RequestList.objects.filter(username=request.user.username, status="None")
    ordered_queryset = combined_queryset
    return render(request, 'main/notify.html', {'user_list': ordered_queryset})
