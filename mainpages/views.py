from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'text1': 'latest_question_list'}
    return render(request, 'mainpages/index.html', context)
