from django.shortcuts import render

from booking.models import Users


def main(request):
    return render(request, 'main.html')


def all_users(request):
    user = Users.objects.all().select_related('passport')
    context = {
        'userss': user,
    }
    return render(request, 'users.html', context=context)