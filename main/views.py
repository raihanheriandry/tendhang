from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'Tendhang',
        'name': 'Raihan Maulana Heriandry',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)