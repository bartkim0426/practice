from django.shortcuts import render


def terms(request):
    return render(
            request,
            "policy/terms.html",
            {},
            )
