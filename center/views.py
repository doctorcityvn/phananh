from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render
from .models import Division, Patient
from django.template import loader


# Create your views here.
def benhnhan(request,phong_id,benhnhan_id):
        namediv_list = Division.div.all()
        person1 =Patient.pat.all().filter(id=benhnhan_id) 
        context = {
            'namediv_list': namediv_list,
            'person1': person1,
            'benhnhan_id': benhnhan_id,

        }
        return render(request, 'center/benhnhan.html', context)
def cacphong(request,phong_id):
    namediv_list = Division.div.all()

    #isphong=request.POST.get("phongs", "")
    #request.POST['phongs']
    #person1 = Patient.pat.all()
    
    #person1 =Patient.pat.raw('SELECT * FROM center_Patient WHERE Type_id.id=phong_id')
    #person1 =Patient.pat.all().filter(Type_id_id=phong_id) 
    person1 =Patient.pat.all().filter(Type_id_id=phong_id) 
    context = {
        'namediv_list': namediv_list,
        'person1': person1,
        'phong_id': phong_id,

        
        
    }
    return render(request, 'center/cacphong.html', context)


def index(request):
    namediv_list = Division.div.all()
    isphong=request.POST.get("phongs", "")
    #request.POST['phongs']
    #person1 = Patient.pat.all()
    
    person1 =Patient.pat.raw('SELECT * FROM center_Patient WHERE Type_id.id=1' )
    context = {
        'namediv_list': namediv_list,
        'person1': person1,
        'isphong': isphong,
        
        
    }
    return render(request, 'center/index.html', context)

def detail(request):
        namediv_list = Division.div.all()
        isphong=request.POST.get("phongs", "")
        #request.POST['phongs']
        #person1 = Patient.pat.all()
        
        person1 =Patient.pat.raw('SELECT * FROM center_Patient' )
        context = {
            'namediv_list': namediv_list,
            'person1': person1,
            'isphong': isphong,
            
            
        }
        return render(request, 'center/index1.html', context)
def DivA(request):
        namediv_list = Division.div.all()
        isphong=request.POST.get("phongs", "")
        #request.POST['phongs']
        #person1 = Patient.pat.all()
        
        person1 =Patient.pat.raw('SELECT * FROM center_Patient WHERE Type_id_id=1'  )
        context = {
            'namediv_list': namediv_list,
            'person1': person1,
            'isphong': isphong,
            
            
        }
        return render(request, 'center/DivA.html', context)
def DivB(request):
        namediv_list = Division.div.all()
        isphong=request.POST.get("phongs", "")
        #request.POST['phongs']
        #person1 = Patient.pat.all()
        
        person1 =Patient.pat.raw('SELECT * FROM center_Patient WHERE Type_id_id=2'  )
        context = {
            'namediv_list': namediv_list,
            'person1': person1,
            'isphong': isphong,
            
            
        }
        return render(request, 'center/DivB.html', context)
def DivC(request):
        namediv_list = Division.div.all()
        isphong=request.POST.get("phongs", "")
        #request.POST['phongs']
        #person1 = Patient.pat.all()
        
        person1 =Patient.pat.raw('SELECT * FROM center_Patient WHERE Type_id_id=3'  )
        context = {
            'namediv_list': namediv_list,
            'person1': person1,
            'isphong': isphong,
            
            
        }
        return render(request, 'center/DivC.html', context)