from django.shortcuts import render

# Create your views here.
def card_list(request):
    # cards = Card.objects.all()
    # return render (request,"Courses/Courses_card.html")
    return render (request,"Courses/Course_detail_page.html")


def topic_list(request, card_slug):
    # card = get_object_or_404(Card, id=card_id)  # Get the specific card by ID
    # topics = card.topics.all()  # Fetch all topics related to this card
    # return render(request, 'topic_list.html', {'card': card, 'topics': topics})
    pass

def topic_detail(request, card_slug, topic_slug):
    # topic = get_object_or_404(Topic, id=topic_id)  # Get the specific topic by ID
    # return render(request, 'topic_detail.html', {'topic': topic, 'detail': topic.detail})
     pass