from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import*
import random
import traceback

# Create your views here.
def home(request):
    context={'categories':Category.objects.all()}

    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")
    return render(request,'home.html',context)

# {
#     'status' : True,
#     'data' : [
#         {},
#     ]
# }

def quiz(request):
    context={'category':request.GET.get('category')}
    return render(request,'quiz.html',context)

def get_quiz(request):
    try:
        question_objs = Question.objects.all()
        if request.GET.get('category'):
            question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category'))

        data = []

        question_list = list(question_objs)  # Convert QuerySet to a list
        random.shuffle(question_list)

        for question_obj in question_list:
            answers = question_obj.get_answers()
            answers_list = list(answers)
            random.shuffle(answers_list)
            data.append({
                "uid": question_obj.uid,
                "category": question_obj.category.category_name,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answers": answers_list  # Use the shuffled answers here
            })
            print(answers_list)  # Print the shuffled answers for debugging

        payload = {'status': True, 'data': data}
        return JsonResponse(payload)

    except Exception as e:
        traceback.print_exc()  # Print the traceback to the console for debugging
        error_payload = {'status': False, 'error_message': 'Something Went Wrong'}
        return JsonResponse(error_payload, status=500)

        