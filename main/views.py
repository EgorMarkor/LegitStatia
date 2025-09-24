from django.shortcuts import render

def index(request):
    if request.user_agent.is_mobile:  # телефон/планшет
        return render(request, "index_mobile.html")
    else:  # ПК
        return render(request, "index_desktop.html")
    
    
def list(request):
    if request.user_agent.is_mobile:  # телефон/планшет
        return render(request, "list_pc.html")
    else:  # ПК
        return render(request, "list_pc.html")
