from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, SnippetForm, LoginForm
from .models import Snippet




def home(request):
    return render(request, 'home.html', {'home':home})

# Create your views here.
def register(request): #this one is handling the registration process
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():  
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  
            user = authenticate(username=username, password=password) 
            login(request, user) 
            return redirect('snippets_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})  
  



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):# This function handles logging out the user    
    logout(request)  
    return redirect('login')  

@login_required # ensures the user is logged in 
def snippets_list(request):
    query = request.GET.get('q','')
    if query: 
       snippets = Snippet.objects.filter(language__icontains = query) #search
    else :
       snippets = Snippet.objects.all()
    return render (request, 'snippets.html',{'snippets':snippets, 'query': query})

@login_required
def snippet_detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    return render(request, 'snippet_detail.html', {'snippet': snippet})



@login_required
def snippet_create(request):  # Creating a snippet
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)  # Create a Snippet object but don't save it yet
            snippet.user = request.user  # Associate the snippet with the current user
            snippet.save()  # Save the snippet to the database
            return redirect('snippets_list')  # Redirect to the list of snippets after saving
    else:
        form = SnippetForm()  # Create an empty form for GET requests

    return render(request, 'snippet_create.html', {'form': form})

def snippet_delete(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)     # Ensure that the user trying to delete the snippet is the one who created it   
    if snippet.author == request.user:
        snippet.delete()
        messages.success(request, "Snippet deleted successfully.")
        return redirect('snippets_list')
    else:
        messages.error(request, "You are not authorized to delete this snippet.")
        return redirect('snippets_list')  










    








