from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Welcome to the User Module!")


from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully registered.")  # 👈 Message added
            return redirect('login')
        else:
            messages.error(request, "Registration failed. Please check the form.")  # 👈 Error message
    else:
        form = UserCreationForm()
    return render(request, 'usermodule/register.html', {'form': form})


from django.contrib.auth.views import LoginView
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = 'usermodule/login.html'

    def form_valid(self, form):
        messages.success(self.request, "✅ Logged in successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "❌ Invalid username or password.")
        return super().form_invalid(form)
