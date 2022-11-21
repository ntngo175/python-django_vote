from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question,Choice

# Create your views here.
def index(request):
    myname = 'ThanhNhon'
    thongtin = ['Tên:Thành Nhơn', 'Tuổi:21', 'Trường:Bách Khoa Đà Nẵng','Ngành:Kỹ thuật Điện tử-Viễn thông']
    binhchon = 'Vote'
    context = {'name':myname, 'infor':thongtin, 'vote':binhchon}
    return render(request, 'polls/index.html', context)

def viewlist(request):
    # list_question = get_object_or_404(Question, pk=1)
    list_question = Question.objects.all()
    context = {'dsquest':list_question}
    return render(request, 'polls/question_list.html', context)

def detailView(request, question_id):
    q=Question.objects.get(pk=question_id)
    return render(request, 'polls/detail_question.html', {'qs':q})

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu = request.POST['choice']
        c = q.choice_set.get(pk=dulieu)
    except:
        HttpResponse('Loi ko co choice')
    c.vote = c.vote + 1
    c.save()
    return render(request, 'polls/result.html', {'q':q})
