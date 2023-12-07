from django.shortcuts import render , redirect , get_object_or_404
from .models import Profile, Meep, Reply
from django.contrib import messages
from .forms import MeepForm, SignUpForm, ProfilePicForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse



def home(request):
    if request.user.is_authenticated:
        form = MeepForm(request.POST or None, request.FILES or None)
        if request.method == "POST":
            if form.is_valid():
                meep = form.save(commit=False)
                meep.user = request.user
                meep.save()
                messages.success(request, "Your post was sent.")
                return redirect('home')
            # If form is not valid, reach here and render the page with the form and errors
        else:
            # If it's a GET request or the form is not submitted yet, just render the page with the form
            form = MeepForm()
            
        meeps = Meep.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"meeps": meeps, "form": form})
    else:
        meeps = Meep.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"meeps": meeps})



def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles":profiles})

    else:
        messages.success(request,("You must be Logged In To View This Page"))
    return redirect('home')

        
def unfollow(request, pk):
	if request.user.is_authenticated:
		# Get the profile to unfollow
		profile = Profile.objects.get(user_id=pk)
		# Unfollow the user
		request.user.profile.follows.remove(profile)
		# Save our profile
		request.user.profile.save()

		# Return message
		messages.success(request, (f"You Have Successfully Unfollowed {profile.user.username}"))
		return redirect(request.META.get("HTTP_REFERER"))

	else:
		messages.success(request, ("You Must Be Logged In To View This Page..."))
		return redirect('home')
 
       
def follow(request, pk):
	if request.user.is_authenticated:
		# Get the profile to unfollow
		profile = Profile.objects.get(user_id=pk)
		# Unfollow the user
		request.user.profile.follows.add(profile)
		# Save our profile
		request.user.profile.save()

		# Return message
		messages.success(request, (f"You Have Successfully Followed {profile.user.username}"))
		return redirect(request.META.get("HTTP_REFERER"))

	else:
		messages.success(request, ("You Must Be Logged In To View This Page..."))
		return redirect('home')


        
def profile(request, pk):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user_id=pk)
            meeps = Meep.objects.filter(user_id=pk).order_by("-created_at")  # Fetching Meep objects for the user
            if request.method == "POST":
                current_user_profile = request.user.profile
                action = request.POST['follow']
                if action == "unfollow":
                    current_user_profile.follows.remove(profile)
                elif action == "follow":
                    current_user_profile.follows.add(profile)
                current_user_profile.save()
            return render(request, "profile.html", {"profile": profile, "meeps": meeps})  # Use "meeps" instead of "meep"
        except Profile.DoesNotExist:
            messages.error(request, "Profile does not exist.")
            return redirect('home')  # Redirect to home if profile doesn't exist
    else:
        messages.error(request, "You must be logged in to view this page.")
        return redirect('home')


def followers(request, pk):
	if request.user.is_authenticated:
		if request.user.id == pk:
			profiles = Profile.objects.get(user_id=pk)
			return render(request, 'followers.html', {"profiles":profiles})
		else:
			messages.success(request, ("That's Not Your Profile Page..."))
			return redirect('home')	
	else:
		messages.success(request, ("You Must Be Logged In To View This Page..."))
		return redirect('home')

def follows(request, pk):
	if request.user.is_authenticated:
		if request.user.id == pk:
			profiles = Profile.objects.get(user_id=pk)
			return render(request, 'follows.html', {"profiles":profiles})
		else:
			messages.success(request, ("That's Not Your Profile Page..."))
			return redirect('home')	
	else:
		messages.success(request, ("You Must Be Logged In To View This Page..."))
		return redirect('home')



def create_reply(request, meep_id):
    if request.method == "POST":
        meep = Meep.objects.get(id=meep_id)
        reply_body = request.POST.get('reply_body')
        new_reply = Reply.objects.create(user=request.user, meep=meep, body=reply_body)
        # Additional logic or redirection after creating the reply
        # For example, redirecting back to the original Meep detail page
        return HttpResponseRedirect(reverse('meep_detail', args=[meep_id]))
    else:
        # Handle other request methods or situations
        # This could be a GET request, return a different response or render a template
        return HttpResponse("This endpoint only supports POST requests.")


def meep_detail(request, meep_id):
    meep = get_object_or_404(Meep, id=meep_id)
    # You can pass 'meep' to the template for rendering
    return render(request, 'home.html', {'meep': meep})

def login_user(request):
    if request.method=="POST":
       username= request.POST['username'] 
       password= request.POST['password']
       user= authenticate(request, username=username, password=password)
       if user is not None:
            login(request, user)
            messages.success(request,("You have been logged in!.."))
            return redirect('home')
       else:
            messages.error(request, "There was an error logging you in!")
            return redirect('login')

    else:
     return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request,("You have been Logged Out"))
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
          

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("You had made an account"))
            return redirect('home')
        
    return render(request, "register.html", {'form':form})





def update_user(request): 
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)
        user_form = SignUpForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,("You Profile has been updated"))
            login(request, current_user)
            return redirect('home')
        
        
        return render(request, "update_user.html", {'user_form': user_form,'profile_form':profile_form})

    else:
        messages.success(request,("You must be logged in To update profile"))
        return redirect('home')
    
    
def meep_likes(request, pk):
    if request.user.is_authenticated:
        meep = get_object_or_404(Meep, id=pk)
        if meep.likes.filter(id= request.user.id):
            meep.likes.remove(request.user)
        else:
            meep.likes.add(request.user)
        return redirect(request.META.get("HTTP_REFERER"))
            
        

    else:
        messages.error(request, "You Must Be Logged In To View That Page!")
        return redirect('home')
    
def meep_show(request, pk):
    meep = get_object_or_404(Meep, id=pk)
    if meep:
        return render(request, 'show_meep.html', {"meep":meep})

    else:
        messages.success(request,("You must be logged in To update profile"))
        return redirect('home')   
    
    
def delete_meep(request, pk):
      if request.user.is_authenticated:
        meep = get_object_or_404(Meep, id=pk)
        if request.user.username== meep.user.username:
            meep.delete()
            messages.success(request,("Tweet has been deleted"))
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            messages.success(request,("Tweet was delted"))
            return redirect('home')
      else:
         messages.success(request,("You must be logged in To update profile"))
         return redirect(request.META.get("HTTP_REFERER"))
      
def edit_meep(request,pk):
     if request.user.is_authenticated:
            meep = get_object_or_404(Meep, id=pk)

            if request.user.username== meep.user.username:
                form = MeepForm(request.POST or None, request.FILES or None, instance=meep)
                if request.method == "POST":
                      if form.is_valid():
                          meep = form.save(commit=False)
                          meep.user = request.user
                          meep.save()
                          messages.success(request, "Your post has been edited!.")
                          return redirect('home')
            # If form is not valid, reach he
                
                else:       
                    return render(request, "edit_meep.html", {'form': form,'meep':meep})

            else:
                 messages.success(request,("Tweet was delted"))
                 return redirect('home')
     else:
         messages.success(request,("You must be log in"))
         return redirect('home')
     
     
def search(request):
    if request.method=="POST":
        search = request.POST['search']
        
        searched = Meep.objects.filter(body__contains= search)
        
        return render(request, 'search.html',{'search': search, 'searched': searched})

    else:
        return render(request, 'search.html',{})


def search_user(request):
    if request.method=="POST":
        search = request.POST['search']
        
        searched = User.objects.filter(username__contains= search)
        
        return render(request, 'search_user.html',{'search': search, 'searched': searched})

    else:
        return render(request, 'search_user.html',{})
    
def meep_detail(request, pk):
    meep = get_object_or_404(Meep, id=pk)
    if meep:
        return render(request, 'ReplyTweet.html', {"meep":meep})

    else:
        messages.success(request,("You must be logged in To update profile"))
        return redirect('home')   