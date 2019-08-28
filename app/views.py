from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Patient
from django.contrib.messages.views import SuccessMessageMixin
from .models import Detalis
from .models import Description
from django.shortcuts import render, redirect
from .ModalForms import *
from .models import Pat
import re
def index(request):
    return render(request,"index.html")


def show(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    Hb = request.POST.get("Hb")
    GlbLevel = request.POST.get("GlbLevel")
    HlBac = request.POST.get("HlBac")
    Heatbeet = request.POST.get("Heatbeet")
    Oxeygenlevel = request.POST.get("Oxeygenlevel")
    Bmi = request.POST.get("Bmi")
    Name = request.POST.get("Name")
    Age = request.POST.get("Age")
    Gen = request.POST.get("Gen")
    Phone = request.POST.get("Phone")
    id = request.POST.get("id")
    City = request.POST.get("City")
    Blood = request.POST.get("Blood")
    Addres = request.POST.get("Addres")
    a = re.fullmatch("[6-9]\d{9}", Phone)
    if a != None:
        Detalis(Name=Name, Age=Age, Gen=Gen, Phone=Phone, id=id, City=City, Blood=Blood, Addres=Addres, ).save()
        Des = request.POST.get("Description")
        Description(Des=Des).save()
        # return render(request, "index3.html", {"message": "SuccessFull Register"})
        Patient(idno=idno, name=name, Hb=Hb, GlbLevel=GlbLevel, HlBac=HlBac, Heatbeet=Heatbeet,
                Oxeygenlevel=Oxeygenlevel, Bmi=Bmi).save()
        qr = (
                    Hb >= '13.2' and GlbLevel <= '95' and HlBac <= '4.5' and Heatbeet == '80' and Oxeygenlevel >= '90' and Bmi == '22.8')
        #num = (Hb + GlbLevel + HlBac + Heatbeet + Oxeygenlevel + Bmi)
        #qs = Patient.objects.values("idno")
        if qr:
            return render(request, "index1.html")
        else:
            return render(request, "index2.html", {"message": "Patient Is Bad Positions"})
    else:
        return render(request, "index3.html", {"message": "Invalid Phone Number"})

    #if Hb >= '13':
    #    return render(request, "index1.html")
    #elif GlbLevel >= '12':
    #    return render(request, "index1.html")
    #elif HlBac == '10':
    #    return render(request, "index1.html")
    #elif Heatbeet == '10':
    #    return render(request, "index1.html")
    #elif Oxeygenlevel == '10':
    #    return render(request, "index1.html")
    #elif Bmi == '10':
    #    return render(request, "index1.html")
    #else:
    #    return render(request, "patient.html")



class Viewall(ListView):
    template_name = "Viewall.html"
    model = Patient


class AllPatientIds(ListView):
    template_name = "Allides.html"
    model = Patient
    quryset=Patient.objects.values("idno")

def index5(request):
    if request.method=="POST":
        a=request.POST.get("Hb")
        b=request.POST.get("GlbLevel")
        c=request.POST.get("HlBac")
        d=request.POST.get("Heatbeet")
        e=request.POST.get(" Oxeygenlevel")
        f=request.POST.get("Bmi")
        g=a+b+c+d+e+f
        qs=Patient.objects.filter(a+b+c+d+e+f)
        if qs<=305.5:
            return render(request, "OnePatient.html", )




        #qs=Patient.objects.filter(Hb=a,GlbLevel=b,HlBac=c,Heatbeet=d,Oxeygenlevel=e,Bmi=f)






class OnePatient(SuccessMessageMixin,DetailView):
    template_name = "OnePatient.html"
    model = Patient
    qs=Patient.objects.values("Bmi")
    success_message = "Patient Is Safe"






def home(request):
    return render(request,"home.html")


def search(request):
    y = request.GET['idno']
    recs = Patient.objects.filter(idno=y)
    return render(request, 'patient.html', {'recs': recs})


#class Ammount(ListView):
 #   template_name = "Total.html"
  #  model = Patient
   # queryset = Patient.objects.values("name")


#class PatientName(DetailView):
 #   template_name = "Total.html"
  #  model = Patient

def index2(request):
    Name=request.POST.get("Name")
    Age=request.POST.get("Age")
    Gen=request.POST.get("Gen")
    Phone=request.POST.get("Phone")
    id=request.POST.get("id")
    City=request.POST.get("City")
    Blood=request.POST.get("Blood")
    Addres=request.POST.get("Addres")
    a=re.fullmatch("[6-9]\d{9}",Phone)
    if a!=None:
        Detalis(Name=Name,Age=Age,Gen=Gen,Phone=Phone,id=id,City=City,Blood=Blood,Addres=Addres,).save()
        return render(request,"index3.html",{"message":"SuccessFull Register"})
    else:
        return render(request, "show.html", {"message": "Phone Number is Invalid"})


class Index4(ListView,SuccessMessageMixin):
    template_name = "show1.html"
    model = Patient
    success_message = "Patient Is Safe"


"""def index5(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    Hb = request.POST.get("Hb")
    GlbLevel = request.POST.get("GlbLevel")
    HlBac = request.POST.get("HlBac")
    Heatbeet = request.POST.get("Heatbeet")
    Oxeygenlevel = request.POST.get("Oxeygenlevel")
    Bmi = request.POST.get("Bmi")
    qr = Patient.objects.values(Hb + GlbLevel + HlBac + Heatbeet + Oxeygenlevel + Bmi, idno, name)
    Name = request.POST.get("Name")
    Age = request.POST.get("Age")
    Gen = request.POST.get("Gen")
    Phone = request.POST.get("Phone")
    id = request.POST.get("id")
    City = request.POST.get("City")
    Blood = request.POST.get("Blood")
    Addres = request.POST.get("Addres")
    a = re.fullmatch("[6-9]\d{9}", Phone)
    if a != None:
        Detalis(Name=Name, Age=Age, Gen=Gen, Phone=Phone, id=id, City=City, Blood=Blood, Addres=Addres, ).save()
        Des = request.POST.get("Description")
        Description(Des=Des).save()
        # return render(request, "index3.html", {"message": "SuccessFull Register"})
        Patient(idno=idno, name=name, Hb=Hb, GlbLevel=GlbLevel, HlBac=HlBac, Heatbeet=Heatbeet,
                Oxeygenlevel=Oxeygenlevel, Bmi=Bmi).save()
        qr = (
                Hb >= '13.2' and GlbLevel <= '95' and HlBac <= '4.5' and Heatbeet == '80' and Oxeygenlevel >= '90' and Bmi == '22.8')
        num = (Hb + GlbLevel + HlBac + Heatbeet + Oxeygenlevel + Bmi)
        if qr:
            return render(request, "index1.html", num)
        elif qr <= 305.5:
            return render(request, "show1.html")
        else:
            return render(request, "index2.html", {"message": "Patient Is Bad Positions"})

    else:
        return render(request, "index3.html", {"message": "Invalid Phone Number"})
        """""


def pre(request):
    Description=request.POST.get("Description")
    prescription=request.POST.get("prescription")
    OtherAtachment=request.POST.get("OtherAtachment")
    Pat(Description=Description,prescription=prescription,OtherAtachment=OtherAtachment).save()
    return render(request,"index.html")


