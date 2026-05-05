from django.shortcuts import render

def timer_page(request):
    # Just use the filename. Django will find it inside the 'templates' folder.
    return render(request, 'wheel_timer.html')