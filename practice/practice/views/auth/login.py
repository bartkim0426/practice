from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login


def login(request):
    
    if (request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_page = request.POST.get("next_page") or "home"

        user = User.objects.get(username=username)

        if user.is_authenticated():
            auth_login(request, user)

            return redirect(next_page)

    return render(
            request,
            "auth/login.html",
            {},
            )
