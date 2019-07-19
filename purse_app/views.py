from django.shortcuts import render


def purse_app_start(request):
    return render(request, 'purse_app/start.html', {})
