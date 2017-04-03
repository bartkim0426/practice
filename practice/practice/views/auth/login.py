from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from IPython import embed;


def login(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.get(username=username)

        if user.is_authenticated():
            login(request, user)

            return redirect(
                    reverse(
                        "posts:list",
                        )
                    )

    return render(
            request,
            "auth/login.html",
            {},
            )