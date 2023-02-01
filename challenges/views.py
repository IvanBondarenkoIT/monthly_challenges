from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
    "December": "Learn Django for at least 20 minutes every day!"
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]
    return HttpResponseRedirect(redirect_month)


def monthly_challenge(request, month):
    month = month.capitalize()
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except IndexError:
        return HttpResponseNotFound("This month not supported")

