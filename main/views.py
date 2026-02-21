from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from main.models import Game, Category, Company


# Create your views here.

def get_all_games(request: HttpRequest):
    games = Game.objects.all()

    context = {'games': games}
    return render(request, 'games.html', context=context)

def game_view(request: HttpRequest, game_id: int):
    game = get_object_or_404(Game, id=game_id)
    context = {'game': game}
    return render(request, "game_view.html", context=context)

def add_game(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        price = request.POST.get("price")
        icon_url = request.POST.get("icon_url")
        developer_id = request.POST.get("developer")
        publisher_id = request.POST.get("publisher")
        category_ids = request.POST.getlist("categories")

        developer = Company.objects.get(id=developer_id)
        publisher = Company.objects.get(id=publisher_id)

        user_name = request.POST.get("user_name")

        game = Game.objects.create(
            title=title,
            description=description,
            price=price,
            icon_url=icon_url,
            developer=developer,
            publisher=publisher,
            added_by=user_name,
        )

        game.categories.set(category_ids)
        game.save()

        return redirect("games")

    categories = Category.objects.all()
    companies = Company.objects.all()
    return render(request, "add_game_form.html", {"categories": categories, "companies": companies})

def add_category(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        category = Category(name=name, description=description)
        category.save()
        return redirect(get_all_games)
    return render(request, 'add_category_form.html')

def games_page_redirector(request: HttpRequest):
    return redirect(get_all_games)

def company_view(request, slug):
    company = get_object_or_404(Company, slug=slug)

    developed_games = company.developed_games.all()
    published_games = company.published_games.all()

    context = {
        'company': company,
        'developed_games': developed_games,
        'published_games': published_games
    }

    return render(request, "company_view.html", context)

def category_view(request: HttpRequest, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    games = Game.objects.all()
    category_games = []
    for game in games:
        if game.categories.contains(category):
            category_games.append(game)
    context = {'category': category, 'games': category_games}
    return render(request, "category_view.html", context=context)

def edit_game(request: HttpRequest, game_id):
    game = get_object_or_404(Game, id=game_id)
    categories = Category.objects.all()
    developers = Company.objects.all()
    publishers = Company.objects.all()

    if request.method == "POST":
        game.title = request.POST.get("title")
        game.description = request.POST.get("description")
        game.price = request.POST.get("price")

        game.developer_id = request.POST.get("developer")
        game.publisher_id = request.POST.get("publisher")

        selected_categories = request.POST.getlist("categories")
        game.categories.set(selected_categories)

        game.save()

        return redirect("home")

    return render(request, "edit_game.html", {
        "game": game,
        "categories": categories,
        "developers": developers,
        "publishers": publishers
    })