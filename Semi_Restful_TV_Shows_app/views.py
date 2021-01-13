from django.shortcuts import render,redirect
from .models import Show, ShowManager
from django.contrib import messages
# from .model import #

# Create your views here.
def index(request):
    print("******"*15)
    print("🤣🤣🤣 we are in the index 🤣🤣🤣")

    return render(request, 'create.html')


def display_show(request, show_id):
    print("******"*15)
    print("🤣🤣🤣 we are in the display_show 🤣🤣🤣")
    context = {
        'this_show': Show.objects.get(id=show_id)
    }
    return render(request,"read-one.html", context)


def all_show(request):
    print("******"*15)
    print("🤣🤣🤣 we are in the all_show 🤣🤣🤣")
    context = {
    'show_all': Show.objects.all()
    }
    return render(request,"read-all.html", context)

def update_page(request, show_id):
    print("******"*15)
    print("🤣🤣🤣 we are in the update_page 🤣🤣🤣")
    context = {
        'this_show': Show.objects.get(id=show_id)
                                        # show id in the URL
    }
    return render(request, "update.html", context)


def update_show(request, show_id):
    print("******"*15)
    print("🤣🤣🤣 we are in the update_show 🤣🤣🤣")
    # after each function print(request.POST)
    # any function comming from a form
    errors = Show.objects.validateShow(request.POST)

    print(errors)

    if errors:
    # if len(errors) == 0:
        print("try again...")

        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect(f'/shows/{show_id}/edit')

    this_show = Show.objects.get(id=show_id)
    this_show.title =  request.POST['show_title']
    this_show.network =  request.POST['show_network']
    this_show.release_date =  request.POST['show_release_date']
    this_show.description =  request.POST['show_description']
    this_show.save()

    return redirect("/shows")



def create_show(request):
    print("******"*15)
    print("🤣🤣🤣 we are in the create_show 🤣🤣🤣")
    print(request.POST)


    # test if request.post is all good

    # errors = validateShow(request.POST)
    errors = Show.objects.validateShow(request.POST)
    
    # errors = True

    print(errors)

    if errors:
    # if len(errors) == 0:
        print("try again...")

        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/shows/new')

    
    new_show = Show.objects.create(
        title=request.POST['show_title'],
        network=request.POST['show_network'],
        release_date=request.POST['show_release_date'],
        description=request.POST['show_description']
        )
    print(Show.objects.all())

    return redirect(f'/shows/{new_show.id}') #may change new_show to str()

def delete_show(request, show_id):
    print("******"*15)
    print("🤣🤣🤣 we are in the delete_show 🤣🤣🤣")

    this_show = Show.objects.get(id=show_id)
    this_show.delete()
    # deleting so we dont pass back in (no context required)
    return redirect('/shows')