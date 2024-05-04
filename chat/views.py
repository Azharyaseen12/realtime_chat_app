from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate,logout
from .forms import CustomUserCreationForm ,CustomAuthenticationForm
from django.contrib.auth.models import User

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

# Create your views here.
def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users':users})

def room(request, room):
    username = request.GET.get('username')
    room_details = User.objects.get(id = room)
    print(room_details.id)
    return render(request, 'room.html', {
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    print(room,username)
    user = User.objects.get(id = room)
    if User.objects.filter(id = room).exists():
        return redirect('room',user.id)   

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    
    receiver_user = User.objects.get(id=room_id) 
    
    new_message = Message.objects.create(message=message, sender = request.user, receiver = receiver_user)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    # room_details = Room.objects.get(name=room)
    receiver_user = User.objects.get(id=room)    
    sent_messages = Message.objects.filter(sender=request.user, receiver=receiver_user)
    received_messages = Message.objects.filter(sender=receiver_user, receiver=request.user)    
    # Combine sent and received messages into a single queryset
    messages = sent_messages.union(received_messages).order_by('timestamp')

    return JsonResponse({"messages":list(messages.values())})