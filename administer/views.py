from django.shortcuts import render

from main.models import Calender
from .forms import RequestListForm
from .models import RequestList


def administer(request):
    if request.user.is_authenticated:
        if request.user.username == "aa":
            return render(request, 'administer/home.html')
        else:
            return render(request, 'main/home.html', {'err_mssg_2': 'You do not have Administrative Rights'})
    else:
        return render(request, 'app/login.html')


def search(request):
    if request.user.is_authenticated:
        if request.user.username == "aa":
            if request.method == "POST":
                form = RequestListForm(request.POST or None)
                if form.is_valid():
                    form.save(commit=False)
                    sport = form.cleaned_data['sport1']

                    if str(sport) == "--":
                        return render(request, 'administer/home.html', {'err_mssg': 'Select The Field'})
                    else:
                        user_list = RequestList.objects.filter(sport1=sport, status="None")
                        return render(request, 'administer/search.html', {'user_list': user_list})
                context = {
                    "form": form,
                }
                return render(request, 'administer/home.html', context)
        else:
            return render(request, 'main/home.html')
    else:
        return render(request, 'app/login.html')


def reject(request, user_id):
    if request.user.is_authenticated:
        if request.user.username == "aa":
            obj = RequestList.objects.get(pk=user_id)
            user_list = RequestList.objects.filter(sport1=obj.sport1, status="None")
            obj.status = "Rejected"
            obj.save()
            return render(request, 'administer/search.html', {'user_list': user_list})
        else:
            return render(request, 'main/home.html')
    else:
        return render(request, 'app/login.html')


def approve(request, user_id):
    if request.user.is_authenticated:
        if request.user.username == "aa":
            obj = RequestList.objects.get(pk=user_id)
            obj.status = "Approved"
            obj.save()
            calender = Calender.objects.get(sport=obj.sport1, month=obj.month1, date=obj.date1)

            if obj.check_1 == "1":
                calender.check_1 = "2"
                calender.total_bookings = calender.total_bookings - 1
            if obj.check_2 == "1":
                calender.check_2 = "2"
                calender.total_bookings = calender.total_bookings - 1
            if obj.check_3 == "1":
                calender.check_3 = "2"
                calender.total_bookings = calender.total_bookings - 1
            if obj.check_4 == "1":
                calender.check_4 = "2"
                calender.total_bookings = calender.total_bookings - 1
            if obj.check_5 == "1":
                calender.check_5 = "2"
                calender.total_bookings = calender.total_bookings - 1
            if obj.check_6 == "1":
                calender.check_6 = "2"
                calender.total_bookings = calender.total_bookings - 1
            if obj.check_7 == "1":
                calender.check_7 = "2"
                calender.total_bookings = calender.total_bookings - 1
            if obj.check_8 == "1":
                calender.check_8 = "2"
                calender.total_bookings = calender.total_bookings - 1
            if obj.check_9 == "1":
                calender.check_9 = "2"
                calender.total_bookings = calender.total_bookings - 1
            if obj.check_10 == "1":
                calender.check_10 = "2"
                calender.total_bookings = calender.total_bookings - 1
            if obj.check_11 == "1":
                calender.check_11 = "2"
                calender.total_bookings = calender.total_bookings - 1
            if obj.check_12 == "1":
                calender.check_12 = "2"
                calender.total_bookings = calender.total_bookings - 1
            if obj.check_13 == "1":
                calender.check_13 = "2"
                calender.total_bookings = calender.total_bookings - 1
            if obj.check_14 == "1":
                calender.check_14 = "2"
                calender.total_bookings = calender.total_bookings - 1
            if obj.check_15 == "1":
                calender.check_15 = "2"
                calender.total_bookings = calender.total_bookings - 1
            if obj.check_16 == "1":
                calender.check_16 = "2"
                calender.total_bookings = calender.total_bookings - 1

            calender.save()

            list1 = RequestList.objects.filter(sport1=obj.sport1, status="None", month1=obj.month1, date1=obj.date1)
            for user in list1:
                if user.check_1 == "1" and calender.check_1 == "2":
                    func(user, calender)
                    user.status = "Rejected"
                elif user.check_2 == "1" and calender.check_2 == "2":
                    func(user, calender)
                    user.status = "Rejected"
                elif user.check_3 == "1" and calender.check_3 == "2":
                    func(user, calender)
                    user.status = "Rejected"
                elif user.check_4 == "1" and calender.check_4 == "2":
                    func(user, calender)
                    user.status = "Rejected"
                elif user.check_5 == "1" and calender.check_5 == "2":
                    func(user, calender)
                    user.status = "Rejected"
                elif user.check_6 == "1" and calender.check_6 == "2":
                    func(user, calender)
                    user.status = "Rejected"
                elif user.check_7 == "1" and calender.check_7 == "2":
                    func(user, calender)
                    user.status = "Rejected"
                elif user.check_8 == "1" and calender.check_8 == "2":
                    func(user, calender)
                    user.status = "Rejected"
                elif user.check_9 == "1" and calender.check_9 == "2":
                    func(user, calender)
                    user.status = "Rejected"
                elif user.check_10 == "1" and calender.check_10 == "2":
                    func(user, calender)
                    user.status = "Rejected"
                elif user.check_11 == "1" and calender.check_11 == "2":
                    func(user, calender)
                    user.status = "Rejected"
                elif user.check_12 == "1" and calender.check_12 == "2":
                    func(user, calender)
                    user.status = "Rejected"
                elif user.check_13 == "1" and calender.check_13 == "2":
                    func(user, calender)
                    user.status = "Rejected"
                elif user.check_14 == "1" and calender.check_14 == "2":
                    func(user, calender)
                    user.status = "Rejected"
                elif user.check_15 == "1" and calender.check_15 == "2":
                    func(user, calender)
                    user.status = "Rejected"
                elif user.check_16 == "1" and calender.check_16 == "2":
                    func(user, calender)
                    user.status = "Rejected"
                user.save()

            user_list = RequestList.objects.filter(sport1=obj.sport1, status="None")
            return render(request, 'administer/search.html', {'user_list': user_list})
        else:
            return render(request, 'main/home.html')
    else:
        return render(request, 'app/login.html')


def func(user, calender):
    if user.check_1 == "1" and calender.check_1 == "1":
        calender.check_1 = "0"
    if user.check_2 == "1" and calender.check_2 == "1":
        calender.check_2 = "0"
    if user.check_3 == "1" and calender.check_3 == "1":
        calender.check_3 = "0"
    if user.check_4 == "1" and calender.check_4 == "1":
        calender.check_4 = "0"
    if user.check_5 == "1" and calender.check_5 == "1":
        calender.check_5 = "0"
    if user.check_6 == "1" and calender.check_6 == "1":
        calender.check_6 = "0"
    if user.check_7 == "1" and calender.check_7 == "1":
        calender.check_7 = "0"
    if user.check_8 == "1" and calender.check_8 == "1":
        calender.check_8 = "0"
    if user.check_9 == "1" and calender.check_9 == "1":
        calender.check_9 = "0"
    if user.check_10 == "1" and calender.check_10 == "1":
        calender.check_10 = "0"
    if user.check_11 == "1" and calender.check_11 == "1":
        calender.check_11 = "0"
    if user.check_12 == "1" and calender.check_12 == "1":
        calender.check_12 = "0"
    if user.check_13 == "1" and calender.check_13 == "1":
        calender.check_13 = "0"
    if user.check_14 == "1" and calender.check_14 == "1":
        calender.check_14 = "0"
    if user.check_15 == "1" and calender.check_15 == "1":
        calender.check_15 = "0"
    if user.check_16 == "1" and calender.check_16 == "1":
        calender.check_16 = "0"
    calender.save()
    return


def history(request):
    if request.user.is_authenticated:
        if request.user.username == "aa":
            combined_queryset = RequestList.objects.filter(status="Approved") | RequestList.objects.filter(
                status="Rejected")
            ordered_queryset = combined_queryset
            return render(request, 'administer/history.html', {'user_list': ordered_queryset})
        else:
            return render(request, 'main/home.html')
    else:
        return render(request, 'app/login.html')


def reset_calender(request):
    if request.user.is_authenticated:
        if request.user.username == "aa":
            list1 = Calender.objects.all()
            for each in list1:
                each.check_1 = "0"
                each.check_2 = "0"
                each.check_3 = "0"
                each.check_4 = "0"
                each.check_5 = "0"
                each.check_6 = "0"
                each.check_7 = "0"
                each.check_8 = "0"
                each.check_9 = "0"
                each.check_10 = "0"
                each.check_11 = "0"
                each.check_12 = "0"
                each.check_13 = "0"
                each.check_14 = "0"
                each.check_15 = "0"
                each.check_16 = "0"
                each.purpose = "Not Provided"
                each.total_bookings = 16
                each.save()
            return render(request, 'administer/home.html')
        else:
            return render(request, 'main/home.html')
    else:
        return render(request, 'app/login.html')
