from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')


@login_required
def logout(request):
    """To logout the user and redirect back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """To manage the login form"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None, "Your username or password is incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


def register(request):
    """To manage the registration form"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "Unable to log you in!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)


@login_required
def profile(request):
    """To display the profile page of a logged in user"""
    return render(request, 'profile.html')


@login_required
def edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('profile')
    else:
        form = UserRegistrationForm(instance=user)
    return render(request, 'editprofile.html', {'form': form})
