from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from .models import Cards
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from apps.users.models import UserProfile

# Create your views here.

# @login_required(login_url="/users/login")
def all_cards(request):
    """This, function show all cards."""
    context = {}
    cards = Cards.objects.all()
    context = {
        'cards': cards
    }
    context.update(csrf(request))

    return render(request, "allcards.html", context)


@login_required(login_url="/users/login")
def view_card(request, card_id):
    """For displaying single card."""
    # import ipdb; ipdb.set_trace()

    context = {}
    card = Cards.objects.get(id=card_id)
    if card.v_type == "public":
        context = {
            'card': card,
            'message': "public",

        }
        context.update(csrf(request))
        return render(request, 'viewcard.html', context)
    else:
        if str(card.user) == str(request.user):
            context = {'message': "private", 'card': card}
            context.update(csrf(request))
            return render(request, 'viewcard.html', context)
        else:
            context = {'message': "private. You can not see it."}
            context.update(csrf(request))
            return render(request, 'viewcard.html', context)


@login_required(login_url="/users/login")
def new_card(request):
    context = {}
    # import ipdb; ipdb.set_trace()
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            image = request.FILES.get('image')
            desc = request.POST.get('desc')
            v_type = request.POST.get('v_type')
            created_by = request.user
            created_by = UserProfile.objects.get(user=created_by)
            new_card = Cards(name=name, image=image, desc=desc, user=created_by, v_type=v_type)
            new_card.save()
            context = {'success': True, 'message': "card saved"}
            context.update(csrf(request))

        except:
            context = {'success': False, 'message': "card not saved"}
            context.update(csrf(request))
    return render(request, "newcard.html", context)


@login_required(login_url="/users/login")
def likes(request, card_id):
    # import ipdb; ipdb.set_trace()

    context = {}
    if request.method == "POST":

        card = Cards.objects.get(id=card_id)
        card.likes += 1
        card.save()
        context = {
            'likes': card.likes
        }

    context.update(csrf(request))
    return HttpResponseRedirect("/cards/all/%s/" % card_id, context)
