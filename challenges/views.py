from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "January": "Eat no meat for the entire month!",
    "February": "Walk for at least 20 minutes every day!",
    "March": "Learn Django for at least 20 minutes every day!",
    "April": "Eat no meat for the entire month!",
    "May": "Walk for at least 20 minutes every day!",
    "June": "Learn Django for at least 20 minutes every day!",
    "July": "Eat no meat for the entire month!",
    "August": "Walk for at least 20 minutes every day!",
    "September": "Learn Django for at least 20 minutes every day!",
    "October": "Eat no meat for the entire month!",
    "November": "Walk for at least 20 minutes every day!",
    "December": None
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months) or month < 0:
        return HttpResponseNotFound("This month not supported")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    month = month.capitalize()
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month,
        })
    except IndexError:
        raise Http404()


def index(request):
    response_data = "<ul>"
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    })
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        response_data += f'<li><a href="{month_path}">{month}</a></li>'

    response_data += "</ul>"
    return HttpResponse(response_data)



