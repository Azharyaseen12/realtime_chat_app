from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login, authenticate,logout
from .forms import CustomUserCreationForm ,CustomAuthenticationForm
from .models import CustomUser, Message
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')                
            else:
                return HttpResponse("login success")                
    else:
        form = CustomAuthenticationForm()  # Use the custom form here
    return render(request, 'login.html', {'form': form})


def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users':users})



def personel_chat(request, pk):

    receiver_user = CustomUser.objects.get(id=pk)    
    sent_messages = Message.objects.filter(sender=request.user, receiver=receiver_user)
    received_messages = Message.objects.filter(sender=receiver_user, receiver=request.user)    
    # Combine sent and received messages into a single queryset
    messages = sent_messages.union(received_messages).order_by('timestamp')
    if request.method == 'POST':
        message = request.POST.get('message')
        my_message = Message(
            sender = request.user,
            receiver = receiver_user,
            message = message,
        )
        my_message.save()

    return render(request, 'personal_chat.html', {'receiver_user': receiver_user, 'messages': messages})