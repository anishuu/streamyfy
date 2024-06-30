from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import UserAccount
from .models import Plan
import stripe
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Plan

from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Plan

from django.http import JsonResponse
from django.shortcuts import render
from .models import Payment, Plan
from django.contrib.auth.models import User


from .models import UserAccount  # Import the UserAccount model
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .models import Plan

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import UserAccount, Plan, Payment,MovieTVShow
from datetime import datetime
# Create your views here.
def IndexPage(request):
    return render(request, 'index.html')

def receipt(request):
    return render(request, 'receipt.html')

def profile(request):
    return render(request, 'profile.html')



def payment(request):
    # return render (request,'payment.html')

    plans = Plan.objects.all()
    return render(request, 'payment.html', {'plans': plans})









from datetime import datetime
from .models import Watches


import random

from django.contrib.auth.decorators import login_required
from .models import Watches

@login_required(login_url='login')
def movie(request, Show_id):
    # Get the requested movie
    movie = get_object_or_404(MovieTVShow, pk=Show_id)

    # Get all movies with the same genre (excluding the requested movie)
    similar_movies = MovieTVShow.objects.filter(Genre__icontains=movie.Genre).exclude(pk=Show_id)

    # Randomly select 5 movies from similar_movies
    recommended_movies = random.sample(list(similar_movies), min(len(similar_movies), 5))

    # Store user's watch history
    if request.user.is_authenticated:  # Check if the user is authenticated
        user_account = UserAccount.objects.get(Email_id=request.user.email)  # Fetch UserAccount instance
        Watches.objects.create(User=user_account, Show=movie, Date=datetime.now().date())

    return render(request, 'moviepage.html', {'movie': movie, 'recommended_movies': recommended_movies})


stripe.api_key = settings.STRIPE_SECRET_KEY


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import UserAccount, Plan, Payment
from datetime import datetime
import uuid  # Import the UUID module to generate unique IDs
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserAccount, Plan, Payment
from datetime import datetime
import uuid  


# @login_required(login_url='login')
def paymentpic(request, plan_id, user_id):
    if request.method == 'POST':
        user_account = UserAccount.objects.get(pk=user_id)
        plan = Plan.objects.get(pk=plan_id)
        amount = int(plan.plan_price * 100)  
        
        # Assume payment processing here (Stripe or any other payment gateway)
        # If payment is successful, save payment details to the database
        try:
            # Create a payment intent
            # Assuming payment is successful if no exceptions are raised
            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
                payment_method_types=['card'],
                metadata={'plan_id': plan_id}
            )
            
            # Generate a unique transaction ID
            transaction_id = str(uuid.uuid4())[:8]  
            
            # Save payment data to the database
            payment_date = datetime.now().date()  
            payment = Payment.objects.create(
                Transaction_id=transaction_id,
                Payment_time=datetime.now(),  
                Payment_date=payment_date,  
                Payment_method='Card',  
                Amount_paid=plan.plan_price,
                Plan=plan,
                User=user_account
            )
            
            # Render receipt template after successful payment
            return render(request, 'receipt.html', {'payment': payment})
        
        except Exception as e:
            # Handle payment failure
            return HttpResponse("Payment Failed: " + str(e))
    
    else:
        plan = Plan.objects.get(pk=plan_id)
        return render(request, 'paymentpicker.html', {'plan': plan})



def payment_success(request):
    return render(request, 'paymentsucess.html')

from .models import MovieTVShow
from django.shortcuts import render
from .models import MovieTVShow

@login_required(login_url='login')
def HomePage(request):
    movies = MovieTVShow.objects.all()
    kids_movies = MovieTVShow.objects.filter(Genre__icontains='kids')
    horror_movies = MovieTVShow.objects.filter(Genre__icontains='horror')
    romantic_movies = MovieTVShow.objects.filter(Genre__icontains='romantic')
    context = {
        'movies': movies,
        'kids_movies': kids_movies,
        'horror_movies': horror_movies,
        'romantic_movies': romantic_movies
    }
    return render(request, 'home2.html', context)








from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import UserAccount, Plan
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import UserAccount, Plan

def SignupPage(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        plan_id = request.POST.get('plan_id')

        if User.objects.filter(email=email).exists():
            return HttpResponse("User already exists!")  # Return an appropriate message if the user already exists

        if password1 != password2:
            return HttpResponse("Your password and confirm password do not match!")

        user = User.objects.create_user(username=email, email=email, password=password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        user_account = UserAccount.objects.create(
            Email_id=email,
            First_name=first_name,
            Last_name=last_name,
            Address=address,
            Phone_number=phone_number,
            Plan_id=plan_id
        )

        user_id = user_account.User_id  # Use User_id directly from the UserAccount model

        user = authenticate(request, username=email, password=password1)
        if user is not None:
            login(request, user)
            return redirect('paymentpic', user_id=user_id, plan_id=plan_id)
        else:
            return HttpResponse("Failed to authenticate user!")

    plan_id = request.GET.get('plan_id')
    return render(request, 'registration.html', {'plan_id': plan_id})




from django.contrib import messages

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is incorrect!')
            return render(request, 'login.html', {'login_failed': True})

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def error_404_view(request, exception):
    return render(request, '404.html')


from django.contrib.auth.decorators import login_required
from .models import UserAccount

from django.contrib.auth.decorators import login_required
from .models import UserAccount

@login_required(login_url='login')
def userprofile(request):
    # Retrieve the UserAccount instance associated with the logged-in user
    user_account = UserAccount.objects.get(Email_id=request.user.email)

    # Access the plan type associated with the user
    plan_type = user_account.Plan.plan_type
    plan_price = user_account.Plan.plan_price
    # Pass the user_account and plan_type to the template
    return render(request, 'userprofile.html', {'user_account': user_account, 'plan_type': plan_type,'plan_price':plan_price})
