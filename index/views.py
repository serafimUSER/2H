from django.shortcuts import render
import numpy as np

# Create your views here.
def index(request):
    return render(request, 'index.html')


def test(request):
    data = {'Повышение кровиносного давления ': ['question0', 'question_20'],
 'Тахикардия ': ['question1', 'question_21'],
 'Брадикардия': ['question2', 'question_22'],
 'Отёчность нижних конечностей': ['question3', 'question_23'],
 'Повышенная утомляемость': ['question4', 'question_24'],
 'Частая отдышка без нагрузок': ['question5', 'question_25'],
 'Частое головокружене ': ['question6', 'question_26'],
 'Частая потеря сознания': ['question7', 'question_27'],
 'Болезненные ощущения в области грудной клетки': ['question8', 'question_28'],
 'Повышено ли у вас артеральное давление': ['question9', 'question_29'],
 'У ближайшх родственнков были ли сердечно сосудестые заболевания': ['question10',
  'question_210'],
 'Есть ли у вас диабет': ['question11', 'question_211'],
 'Употребляете вы табако содержащие изделья ': ['question12', 'question_212'],
 'Употребляете ли вы алкаголя содержащие изделья ': ['question13',
  'question_213'],
 'Часто ли вы испытываете стресс ': ['question14', 'question_214'],
 'Подвжный ли у вас образ жизни': ['question15', 'question_215']}
    res = [0 for _ in range(16)]
    if request.method == 'POST':
        for k in request.POST:
            lengh = 0
            for i in data:
                if k in data[i]:
                    if data[i][0] != k:
                        res[lengh] = float(0)
                        break
                    res[lengh] = float(1)
                    break
                lengh += 1
        array = np.array(res)
    return render(request, 'tests.html')


def learning(request):
    return render(request, 'learning.html')