# chat/views.py

from django.shortcuts import render, redirect

def chat_home(request):
    return render(request, 'chat/chatbot.html')

def redirect_to_chat(request):
    return redirect('chat/')

def login_view(request):
    # If the request method is POST, it means that the form has been submitted
    if request.method == 'POST':
        # if needed here we can handle the submitted data and perform the login logic
        pass

    # If it's a GET request, just render the login page
    return render(request, 'chat/login.html')