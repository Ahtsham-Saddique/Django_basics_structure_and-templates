from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import App,store
from .forms  import ChaiVarietyForm

# Create your views here.
def all_temp(request):
    chais=App.objects.all()
    return render(request,'my_first_app/app.html',{'chais':chais})
def chai_details(request,chai_id):
    chai = get_object_or_404(App,pk=chai_id)
    return render(request, "my_first_app/chai_details.html", {'chai': chai})
def chai_store_view(request):
    stores=None
    form=ChaiVarietyForm()
    if request.method=='POST':
        form=ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety=form.cleaned_data['chai_variety']
            stores= store.objects.filter(chai_varieties=chai_variety)
    else:
        chai=ChaiVarietyForm()
    return render(request,"my_first_app/chai_store.html",
                  {'stores':stores ,'form':form})