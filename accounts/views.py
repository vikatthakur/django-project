from django.shortcuts import redirect, render

def login(request):
    if request.method == 'POST':
        #Login user
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect(request, 'pages/index.html')

def register(request):
    if request.method == 'POST':
        #Register user
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
