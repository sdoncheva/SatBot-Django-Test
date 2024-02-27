from django.shortcuts import render

# View for the login page
def login_view(request):
    return render(request, 'login.html')

# View for the chatbot page
def chat_view(request):
    return render(request, 'chatbot.html')
