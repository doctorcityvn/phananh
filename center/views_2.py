from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import (login as auth_login,  authenticate)
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Division, Patient, Service,Trieuchung, Trieuchungtq,Trieuchungcb, Ketluan, Xlkhancap,Donthuoc, Typeservice, Medicine
from .models import Benhan, Trieuchungbenhnhan, Xuly,Dichvuyeucau,Donthuocdieutri,Yeucau, Khachhang

from django.template import loader
from django.db.models import Q
from datetime import datetime
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def somathing():
   return something

def user1(request):
        namediv_list = Division.div.all()
        phong1=1
        person1 =Patient.pat.all()
        bncount = Patient.pat.all().count()+1
        tc =Trieuchung.tchung.all()
        thuoc=Medicine.medi.all()
        tccount=Trieuchung.tchung.all().count()
        date1=datetime.today()
        map1='AIzaSyD5wAflNNOYGLM4FiA9HWXZvYcPiyGi2sw'
        st1=""
        st2=""
        st3=""
        i1=1
        if 'codestaff' in request.GET:
            if 'tuoistaff' in request.GET:

                q=Patient(Type_id_id=request.GET['phongidstaff'],codepatientp=request.GET['codestaff'],namepatient=request.GET['hotenstaff'],age=request.GET['tuoistaff'], place=request.GET['diachistaff'],City=request.GET['thanhphostaff'])
                q.save()
                bncount = Patient.pat.all().count()+1
                st1=" in active"
                st2=""
                st3=""


        else:
            message = 'You submitted an empty form.'
        if 'codedonthuoc' in request.GET:
            if 'tenthuoc' in request.GET:

                q1=Medicine(codemedicine=request.GET['codedonthuoc'],name_medi=request.GET['tenthuoc'],dosage=request.GET['lieudung'],function1=request.GET['congdung_staff'], sideeffect=request.GET['tacdungphu'])
                q1.save()
                st2=" in active"
                st1=""
                st3=""


        else:
            message = 'You submitted an empty form.'

        if 'madichvu' in request.GET:
            if 'tendichvu' in request.GET:

                q3=Typeservice(codeservice=request.GET['madichvu'],name_serv=request.GET['tendichvu'])
                q3.save()
                st3=" in active"
                st1=""
                st2=""


        else:
            message = 'You submitted an empty form.'
        context = {
            'namediv_list': namediv_list,
            'phong1': phong1,
            'person1': person1,
            'bncount': bncount,
            'tc': tc,
            'st1': st1,
            'st2': st2,
            'date1': date1,
            'map1': map1,


        }
        return render(request, 'center/user.html', context)




def Test(request):
        current_user = request.user
        namediv_list = Division.div.all()
        phong1=1
        person1 =Patient.pat.all()
        bncount = Patient.pat.all().count()+1
        tc =Trieuchung.tchung.all()
        thuoc=Medicine.medi.all()
        tccount=Trieuchung.tchung.all().count()
        date1=datetime.today()
        pancolor='#778899'
        map1='AIzaSyD5wAflNNOYGLM4FiA9HWXZvYcPiyGi2sw'
        st1=""
        st2=""
        st3=""
        i1=1
        if 'codestaff' in request.GET:
            if 'tuoistaff' in request.GET:

                q=Patient(Type_id_id=request.GET['phongidstaff'],codepatientp=request.GET['codestaff'],namepatient=request.GET['hotenstaff'],age=request.GET['tuoistaff'], place=request.GET['diachistaff'],City=request.GET['thanhphostaff'])
                q.save()
                bncount = Patient.pat.all().count()+1
                st1=" in active"
                st2=""
                st3=""


        else:
            message = 'You submitted an empty form.'
        if 'codedonthuoc' in request.GET:
            if 'tenthuoc' in request.GET:

                q1=Medicine(codemedicine=request.GET['codedonthuoc'],name_medi=request.GET['tenthuoc'],dosage=request.GET['lieudung'],function1=request.GET['congdung_staff'], sideeffect=request.GET['tacdungphu'])
                q1.save()
                st2=" in active"
                st1=""
                st3=""


        else:
            message = 'You submitted an empty form.'

        if 'madichvu' in request.GET:
            if 'tendichvu' in request.GET:

                q3=Typeservice(codeservice=request.GET['madichvu'],name_serv=request.GET['tendichvu'])
                q3.save()
                st3=" in active"
                st1=""
                st2=""


        else:
            message = 'You submitted an empty form.'
        context = {
            'namediv_list': namediv_list,
            'phong1': phong1,
            'person1': person1,
            'bncount': bncount,
            'tc': tc,
            'st1': st1,
            'st2': st2,
            'date1': date1,
            'pancolor': pancolor,
            'map1': map1,
            'current_user': current_user,


        }
        return render(request, 'center/test5.html', context)
def Test1(request):
        namediv_list = Division.div.all()
        phong1=1
        person1 =Patient.pat.all()
        bncount = Patient.pat.all().count()+1
        tc =Trieuchung.tchung.all()
        thuoc=Medicine.medi.all()
        tccount=Trieuchung.tchung.all().count()
        date1=datetime.today()
        pancolor='#778899'
        map1='AIzaSyD5wAflNNOYGLM4FiA9HWXZvYcPiyGi2sw'
        st1=""
        st2=""
        st3=""
        i1=1
        if 'codestaff' in request.GET:
            if 'tuoistaff' in request.GET:

                q=Patient(Type_id_id=request.GET['phongidstaff'],codepatientp=request.GET['codestaff'],namepatient=request.GET['hotenstaff'],age=request.GET['tuoistaff'], place=request.GET['diachistaff'],City=request.GET['thanhphostaff'])
                q.save()
                bncount = Patient.pat.all().count()+1
                st1=" in active"
                st2=""
                st3=""


        else:
            message = 'You submitted an empty form.'
        if 'codedonthuoc' in request.GET:
            if 'tenthuoc' in request.GET:

                q1=Medicine(codemedicine=request.GET['codedonthuoc'],name_medi=request.GET['tenthuoc'],dosage=request.GET['lieudung'],function1=request.GET['congdung_staff'], sideeffect=request.GET['tacdungphu'])
                q1.save()
                st2=" in active"
                st1=""
                st3=""


        else:
            message = 'You submitted an empty form.'

        if 'madichvu' in request.GET:
            if 'tendichvu' in request.GET:

                q3=Typeservice(codeservice=request.GET['madichvu'],name_serv=request.GET['tendichvu'])
                q3.save()
                st3=" in active"
                st1=""
                st2=""


        else:
            message = 'You submitted an empty form.'
        context = {
            'namediv_list': namediv_list,
            'phong1': phong1,
            'person1': person1,
            'bncount': bncount,
            'tc': tc,
            'st1': st1,
            'st2': st2,
            'date1': date1,
            'pancolor': pancolor,
            'map1': map1,


        }
        return render(request, 'center/test6.html', context)

def About(request):
        return render(request, 'center/about.html')

def map(request):
        return render(request, 'center/map.html')

def menu(request):
        return render(request, 'center/menu.html')
def Contact(request):
        return render(request, 'center/contact.html')
def Staff(request):
        namediv_list = Division.div.all()
        phong1=1
        person1 =Patient.pat.all()
        bncount = Patient.pat.all().count()+1
        tc =Trieuchung.tchung.all()
        thuoc=Medicine.medi.all()
        tccount=Trieuchung.tchung.all().count()
        date1=datetime.today()
        map1='AIzaSyD5wAflNNOYGLM4FiA9HWXZvYcPiyGi2sw'
        st1=""
        st2=""
        st3=""
        i1=1
        if 'codestaff' in request.GET:
            if 'tuoistaff' in request.GET:

                q=Patient(Type_id_id=request.GET['phongidstaff'],codepatientp=request.GET['codestaff'],namepatient=request.GET['hotenstaff'],age=request.GET['tuoistaff'], place=request.GET['diachistaff'],City=request.GET['thanhphostaff'])
                q.save()
                bncount = Patient.pat.all().count()+1
                st1=" in active"
                st2=""
                st3=""


        else:
            message = 'You submitted an empty form.'
        if 'codedonthuoc' in request.GET:
            if 'tenthuoc' in request.GET:

                q1=Medicine(codemedicine=request.GET['codedonthuoc'],name_medi=request.GET['tenthuoc'],dosage=request.GET['lieudung'],function1=request.GET['congdung_staff'], sideeffect=request.GET['tacdungphu'])
                q1.save()
                st2=" in active"
                st1=""
                st3=""


        else:
            message = 'You submitted an empty form.'

        if 'madichvu' in request.GET:
            if 'tendichvu' in request.GET:

                q3=Typeservice(codeservice=request.GET['madichvu'],name_serv=request.GET['tendichvu'])
                q3.save()
                st3=" in active"
                st1=""
                st2=""


        else:
            message = 'You submitted an empty form.'
        context = {
            'namediv_list': namediv_list,
            'phong1': phong1,
            'person1': person1,
            'bncount': bncount,
            'tc': tc,
            'st1': st1,
            'st2': st2,
            'date1': date1,
            'map1': map1,


        }
        return render(request, 'center/staff.html',context)

def Onsite(request):
        namediv_list = Division.div.all()
        phong1=1
        person1 =Patient.pat.all()
        bncount = Patient.pat.all().count()+1
        tc =Trieuchung.tchung.all()
        tccount=Trieuchung.tchung.all().count()
        date1=datetime.now()
        map1='AIzaSyD5wAflNNOYGLM4FiA9HWXZvYcPiyGi2sw'
        i1=1
        if 'code' in request.GET:
            if 'tuoi' in request.GET:

                q=Patient(Type_id_id=request.GET['phongid'],codepatientp=request.GET['code'],namepatient=request.GET['hoten'],age=request.GET['tuoi'], place=request.GET['diachi'],City=request.GET['thanhpho'])
                q.save()
                bncount = Patient.pat.all().count()+1
                count3=0
                for t1 in tc:
                    count3=count3+1
                    st='codetc' + str(count3)
                    strangthai='trangthai' + str(count3)
                    slankham='lankham' + str(count3)
                    sngaykham='ngaykham' + str(count3)
                    tc1=Trieuchung.tchung.all().filter(codetrieuchung=request.GET[st])
                    person4 =Patient.pat.all().filter(codepatientp=request.GET['code'])
                    for p in person4:
                        for t in tc1:
                            q4=Trieuchungtq(codepatient_id=p.codepatientp,codetrieuchung_id=t.codetrieuchung,status1=request.GET[strangthai],lankham=slankham)
                            q4.save()



        else:
            message = 'You submitted an empty form.'

        context = {
            'namediv_list': namediv_list,
            'phong1': phong1,
            'person1': person1,
            'bncount': bncount,
            'tc': tc,
            'date1': date1,
            'map1': map1,


        }
        return render(request, 'center/onsite.html',context)




def updatetc(request,slug):
        date1=datetime.date
        namediv_list = Division.div.all()
        isname=request.POST.get("searchnamebn", "")
        person1 =Patient.pat.all().filter(namepatient__icontains=isname)
        service1 =Service.serv.all().filter(codepatient_id=slug)
        tctq =Trieuchungtq.trieuchungtqs.all().filter(codepatient_id=slug)
        tccb =Trieuchungcb.tccucbo.all().filter(codepatient_id=slug)
        tc =Trieuchung.tchung.all()
        sv =Typeservice.typeserv.all()
        donthuoc1 =Donthuoc.Donthuoc1.all().filter(codepatient_id=slug)
        dt =Medicine.medi.all()
        Xlkc1 =Xlkhancap.Xlkhancap1.all().filter(codepatient_id=slug)
        Kluan1 =Ketluan.ketluan1.all().filter(codepatient_id=slug)
        isname=request.POST.get("searchnamebn", "")
        person2 =Patient.pat.all().filter(codepatientp=slug)
        phong_id=slug
        context = {
            'namediv_list': namediv_list,
            'person1': person1,
            'person2': person2,
            'service1': service1,
            'donthuoc1': donthuoc1,
            'tctq': tctq,
            'tccb': tccb,
            'tc': tc,
            'sv': sv,
            'dt': dt,
            'phong_id': phong_id,
            'donthuoc1': donthuoc1,
            'Xlkc1': Xlkc1,
            'date1': date1,
            'phong_id': phong_id,
            'Kluan1': Kluan1,
        }
        return render(request, 'center/benhnhan_cb.html', context)

def cacphong1(request,slug):
        date1=datetime.date
        namediv_list = Division.div.all()
        isname=request.POST.get("searchnamebn", "")
        person1 =Patient.pat.all().filter(namepatient__icontains=isname)
        service1 =Service.serv.all().filter(codepatient_id=slug)
        tctq =Trieuchungtq.trieuchungtqs.all().filter(codepatient_id=slug)
        tccb =Trieuchungcb.tccucbo.all().filter(codepatient_id=slug)
        tc =Trieuchung.tchung.all()
        sv =Typeservice.typeserv.all()
        donthuoc1 =Donthuoc.Donthuoc1.all().filter(codepatient_id=slug)
        dt =Medicine.medi.all()
        Xlkc1 =Xlkhancap.Xlkhancap1.all().filter(codepatient_id=slug)
        Kluan1 =Ketluan.ketluan1.all().filter(codepatient_id=slug)
        isname=request.POST.get("searchnamebn", "")
        person2 =Patient.pat.all().filter(codepatientp=slug)
        phong_id="Phong A"
        context = {
            'namediv_list': namediv_list,
            'person1': person1,
            'person2': person2,
            'service1': service1,
            'donthuoc1': donthuoc1,
            'tctq': tctq,
            'tccb': tccb,
            'tc': tc,
            'sv': sv,
            'dt': dt,
            'donthuoc1': donthuoc1,
            'Xlkc1': Xlkc1,
            'date1': date1,
            'phong_id': phong_id,
            'Kluan1': Kluan1,
            'slug': slug,






        }
        return render(request, 'center/benhnhan.html', context)

def input1(request):
    namediv_list = Division.div.all()

    isname=request.POST.get("searchname", "")
    person2 =Patient.pat.all().filter(namepatient__icontains=isname)

    person1 =Patient.pat.all().filter(namepatient__icontains=isname,Type_id_id=1)
    context = {
        'namediv_list': namediv_list,
        'person1': person1,
        'person2': person2,




    }
    return render(request, 'center/input1.html', context)


def benhnhan2(request,phong_id,benhnhan_id):
        pass
        date1=datetime.date
        namediv_list = Division.div.all()
        person1 =Patient.pat.all().filter(id=benhnhan_id)
        service1 =Service.serv.all().filter(codepatient_id=benhnhan_id)
        tctq =Trieuchungtq.trieuchungtqs.all().filter(codepatient_id=benhnhan_id)
        tccb =Trieuchungcb.tccucbo.all().filter(codepatient_id=benhnhan_id)
        donthuoc1 =Donthuoc.Donthuoc1.all().filter(codepatient_id=benhnhan_id)
        Xlkc1 =Xlkhancap.Xlkhancap1.all().filter(codepatient_id=benhnhan_id)
        Kluan1 =Ketluan.ketluan1.all().filter(codepatient_id=benhnhan_id)
        isname=request.POST.get("searchnamebn", "")
        person2 =Patient.pat.all().filter(namepatient__icontains=isname)
        context = {
            'namediv_list': namediv_list,
            'person1': person1,
            'person2': person2,
            'benhnhan_id': benhnhan_id,
            'service1': service1,
            'tctq': tctq,
            'tccb': tccb,
            'donthuoc1': donthuoc1,
            'Xlkc1': Xlkc1,
            'date1': date1,
            'phong_id': phong_id,
            'benhnhan_id': benhnhan_id,
            'Kluan1': Kluan1,

        }

        return render(request, 'center/benhnhan_cb.html', context)

def benhnhan1(request,phong_id,benhnhan_id):
        pass
        date1=datetime.date
        namediv_list = Division.div.all()
        person1 =Patient.pat.all().filter(id=benhnhan_id)
        service1 =Service.serv.all().filter(codepatient_id=benhnhan_id)
        tctq =Trieuchungtq.trieuchungtqs.all().filter(codepatient_id=benhnhan_id)
        tccb =Trieuchungcb.tccucbo.all().filter(codepatient_id=benhnhan_id)
        donthuoc1 =Donthuoc.Donthuoc1.all().filter(codepatient_id=benhnhan_id)
        Xlkc1 =Xlkhancap.Xlkhancap1.all().filter(codepatient_id=benhnhan_id)
        Kluan1 =Ketluan.ketluan1.all().filter(codepatient_id=benhnhan_id)
        isname=request.POST.get("searchnamebn", "")
        person2 =Patient.pat.all().filter(namepatient__icontains=isname)
        context = {
            'namediv_list': namediv_list,
            'person1': person1,
            'person2': person2,
            'benhnhan_id': benhnhan_id,
            'service1': service1,
            'tctq': tctq,
            'tccb': tccb,
            'donthuoc1': donthuoc1,
            'Xlkc1': Xlkc1,
            'date1': date1,
            'phong_id': phong_id,
            'benhnhan_id': benhnhan_id,
            'Kluan1': Kluan1,



        }

        return render(request, 'center/benhnhan_tttq.html', context)
def benhnhan(request,phong_id,benhnhan_id):
        pass
        date1=datetime.date
        namediv_list = Division.div.all()
        person1 =Patient.pat.all().filter(id=benhnhan_id)
        service1 =Service.serv.all().filter(codepatient_id=benhnhan_id)
        tctq =Trieuchungtq.trieuchungtqs.all().filter(codepatient_id=benhnhan_id)
        tccb =Trieuchungcb.tccucbo.all().filter(codepatient_id=benhnhan_id)
        donthuoc1 =Donthuoc.Donthuoc1.all().filter(codepatient_id=benhnhan_id)
        Xlkc1 =Xlkhancap.Xlkhancap1.all().filter(codepatient_id=benhnhan_id)
        Kluan1 =Ketluan.ketluan1.all().filter(codepatient_id=benhnhan_id)
        isname=request.POST.get("searchnamebn", "")
        person2 =Patient.pat.all().filter(namepatient__icontains=isname)
        context = {
            'namediv_list': namediv_list,
            'person1': person1,
            'person2': person2,
            'benhnhan_id': benhnhan_id,
            'service1': service1,
            'tctq': tctq,
            'tccb': tccb,
            'donthuoc1': donthuoc1,
            'Xlkc1': Xlkc1,
            'date1': date1,
            'phong_id': phong_id,
            'benhnhan_id': benhnhan_id,
            'Kluan1': Kluan1,



        }

        return render(request, 'center/benhnhan.html', context)
def cacphong(request,phong_id):
    namediv_list = Division.div.all()

    isname=request.POST.get("searchname", "")
    person2 =Patient.pat.all().filter(namepatient__icontains=isname)

    person1 =Patient.pat.all().filter(namepatient__icontains=isname,Type_id_id=phong_id)
    context = {
        'namediv_list': namediv_list,
        'person1': person1,
        'person2': person2,
        'phong_id': phong_id,



    }
    return render(request, 'center/cacphong.html', context)


def index(request):
    namediv_list = Division.div.all()
    isphong=request.POST.get("phongs", "")
    person2 =Patient.pat.all().filter(namepatient=isname)
    #request.POST['phongs']
    #person1 = Patient.pat.all()

    person1 =Patient.pat.raw('SELECT * FROM center_Patient WHERE Type_id.id=1' )
    context = {
        'namediv_list': namediv_list,
        'person1': person1,
        'person2': person2,
        'isphong': isphong,


    }
    return render(request, 'center/index.html', context)

def detail(request):
        namediv_list = Division.div.all()
        isname=request.POST.get("searchname", "")
        person2 =Patient.pat.all().filter(namepatient__icontains=isname)
        map1='AIzaSyD5wAflNNOYGLM4FiA9HWXZvYcPiyGi2sw'
        #person2 =Patient.pat.all().get(namepatient__contains=isname)
        #request.POST['phongs']
        #person1 = Patient.pat.all()
        #person2 =Patient.pat.all().get(namepatient__contains=isname)

        #person2 =Patient.pat.raw('SELECT * FROM center_Patient LIKE ' + 'isname%' )
        person1 =Patient.pat.raw('SELECT * FROM center_Patient' )
        context = {
            'namediv_list': namediv_list,
            'person1': person1,
            'person2': person2,
            'map1': map1,


        }
        return render(request, 'center/index1.html', context)
