from django.shortcuts import render

from .models import Message

def index(request):
    messages = Message.objects
    return render(request, 'wall/index.html', {'messages':messages})

# Post method that adds a new message to the database and removes entries
# that are over the limit
def postmessage(request):
    messages = Message.objects
    if request.method == "POST":
        print("Adding a post")
        data = request.POST
        print(data.__getitem__('text'))
        print(data.__getitem__('mood'))
        newMessage = Message(text=data.__getitem__('text'), mood=data.__getitem__('mood'))
        newMessage.save()

        amount = messages.count()
        iterator = 0;
        limit = 8
        amount = amount - limit

        if amount > 0:
            for message in messages.all():
                if iterator < amount:
                    message.delete()
                iterator += 1
    # Reroute to the default page
    return render(request, 'wall/index.html', {'messages':messages})
