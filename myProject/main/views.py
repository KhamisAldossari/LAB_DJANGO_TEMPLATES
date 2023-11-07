from django.shortcuts import render
from django.shortcuts import render
from django.utils.crypto import get_random_string
from datetime import date

def home(request):
    return render(request, 'main/home.html')

def today(request):
    today_date = date.today()
    return render(request, 'main/today.html', {'today_date': today_date})

def random_password(request):
    random_password = get_random_string(length=12)
    return render(request, 'main/random_password.html', {'random_password': random_password})

def favorite_games(request):
    favorite_games_list = [
        {'title': 'Overwatch 2', 'image_url': 'https://fs-prod-cdn.nintendo-europe.com/media/images/10_share_images/games_15/nintendo_switch_download_software_1/2x1_NSwitchDS_Overwatch2_Season6.png'},
        {'title': 'Fortnite', 'image_url': 'https://cdn2.unrealengine.com/social-image-chapter4-s3-3840x2160-d35912cc25ad.jpg'},
    ]
    return render(request, 'main/favorite_games.html', {'favorite_games_list': favorite_games_list})