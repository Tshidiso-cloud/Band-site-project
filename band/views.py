from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create views here.
# Home page view.
def home(request):
    """
    Displays the home page.

    This view function renders the home page template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the home page template.
    """
    # Renders the home page template
    return render(request, 'band/home.html')


# About page view.
def about(request):
    """
    Displays the about page.

    This view function renders the about page template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the about page template.
    """
    # Renders about page template.
    return render(request, 'band/about.html')


# Events listing view.
def events(request):
    """
    Displays a list of all events.

    This view function retrieves all event objects from the database and 
    renders the events page template with the list of events.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the events page template with a list of events.
        """
    
    # Retrieves all event objects from the database.
    events_list = Event.objects.all()
    # Renders the events page template with the list of events.
    return render(request, 'band/events.html', {'events': events_list})


def register(request):
    """
    Handles user registration.

    This view function processes the user registration form. 
    If the request method is POST, it validates the form data 
    and creates a new user.
    If the request method is GET, it displays the registration form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the login page after 
        successful registration.
        HttpResponse: Renders the registration template with the form.

    Raises:
        None
    """

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login-in page after registration
    else:
        form = UserCreationForm()

    return render(request, 'band/register.html', {'form': form}) # Ensures correct template path.


# View to create a new event, requires user to be logged in.
@login_required
def create_event(request):
    """
    Creates a new event.

    This view function handles the creation of new events. 
    It processes the form data from the POST request, validates it, 
    and creates a new event object which is then saved to the database.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the events page after 
        successful event creation.
        HttpResponse: Renders the create event template if the 
        request is not POST.

    Raises:
        KeyError: If 'title', 'date', or 'description' keys are 
        missing from the POST request.
    """

    if request.method == 'POST':
        title = request.POST['title']

        # Retrieves form data from the POST request.
        date = request.POST['date']
        description = request.POST['description']
        
        # Creates a new event object and saves it to the database.
        Event.objects.create(title=title, date=date, description=description, created_by=request.user)
        
        # Redirects to the events page after successfully creating an event.
        return redirect('events')
    
    # Renders the create event page template if the request is not POST.
    return render(request, 'band/create_event.html')


# Login view.
def login_view(request):
    """
    Handles user login.

    This view function processes the login form data, 
    authenticates the user, and logs them in if 
    credentials are valid.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the home page after successful login.
        HttpResponse: Renders the login template with an error 
        message if authentication fails.
        HttpResponse: Renders the login template if the 
        request is not POST.

    Raises:
        KeyError: If 'username' or 'password' keys 
        are missing from the POST request.
    """

    if request.method == 'POST':
        
        # Retrieves login credentials from the POST request.
        username = request.POST['username']
        password = request.POST['password']

        # Authenticates the user with the provided credentials.
        user = authenticate(request, username=username, password=password)
        if user is not None:
        
            # Logs in the user and redirects to the home page 
            # if authentication is succsessful.
            login(request, user)
            return redirect('home')
        else:
            
            # Renders the login page template with an error message 
            # if authentication fails.
            return render(request, 'band/login.html', {'error': 'Invalid login'})
    
    # Renders the login page template if the request is not POST.
    return render(request, 'band/login.html')

