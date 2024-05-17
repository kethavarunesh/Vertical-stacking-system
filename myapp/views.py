from django.shortcuts import render,redirect,get_object_or_404
from . models import LayoutDetals,TableDetails
from django.utils import timezone
from django.db import transaction
from django.db.models import Q
def dashbaord(request):
    return render(request,'Dashbaord.html')
def home(request):
    return render(request,'home.html')
def layout(request):
    if request.method == 'POST':
        layout_name = request.POST.get('layoutname')
        layout_image = request.FILES.get('layoutimg')
        layout = LayoutDetals(layout_name=layout_name, layout_image=layout_image)
        layout.save()
    return render(request,'layoutpage.html')
def view_layout(request):
    layouts = LayoutDetals.objects.all()
    return render(request, 'viewlayout.html', {'layouts': layouts})

def edit_layout(request, layout_id):
    layout = get_object_or_404(LayoutDetals, id=layout_id)
    
    if request.method == 'POST':
        layout_name = request.POST.get('layoutname')
        layout_image = request.FILES.get('layoutimg')
        layout.layout_name = layout_name
        layout.layout_image = layout_image

        layout.save()
        return redirect('view_layout')  
    
    return render(request, 'edit.html', {'layout': layout})


def delete_layout(request, layout_id):
    layout=get_object_or_404(LayoutDetals,id=layout_id)
    layout.delete()
    return redirect('view_layout')

def manual(request):
    layouts = LayoutDetals.objects.all()
    context = {'layouts': layouts}

    if request.method == 'POST':
        employeecode = request.POST.get('employeecode')
        layout_name = request.POST.get('layout')
        date = timezone.now()
        binsno_list = request.POST.getlist('binsno[]')
        binloc_list = request.POST.getlist('binloc[]')
        project_list = request.POST.getlist('project[]')
        component1_list = request.POST.getlist('component1[]')
        component2_list = request.POST.getlist('component2[]')
        testing = request.POST.getlist('testing[]')
        remarks = request.POST.getlist('remarks[]')
       
        layout_instance = LayoutDetals.objects.get(layout_name=layout_name)

        with transaction.atomic():
            for bin_no, bin_loc, project_name, component1, component2, testing,remarks in zip(binsno_list, binloc_list, project_list, component1_list, component2_list,testing,remarks):
                TableDetails.objects.create(
                    employeecode=employeecode,
                    binserial_no=bin_no,
                    bin_location=bin_loc,
                    projectname=project_name,
                    component1=component1,
                    component2=component2,
                    testing=testing,
                    remarks=remarks,
                    layout=layout_instance 
                )

    return render(request, 'manual.html', context)


def search_layout(request):
    layouts = LayoutDetals.objects.all()
    
    if request.method == "POST":
        layout_name = request.POST.get('layout')
        component1 = request.POST.get('component1')
        component2 = request.POST.get('component2')
        binserial_no = request.POST.get('binsno')

        # Using Django ORM to filter results based on user inputs
        if layout_name:
            entrydetails = TableDetails.objects.filter(layout__layout_name=layout_name)
        else:
            entrydetails = TableDetails.objects.all()

        if component1:
            entrydetails = entrydetails.filter(component1=component1)

        if component2:
            entrydetails = entrydetails.filter(component2=component2)

        if binserial_no:
            entrydetails = entrydetails.filter(binserial_no=binserial_no)
    else:
      
        entrydetails = TableDetails.objects.all()

    return render(request, 'search_layout.html', {'entrydetails': entrydetails, 'layouts': layouts})

def editpage(request):
      if 'bin' in request.GET:
        bin_serial_number = request.GET['bin']
        table_details = TableDetails.objects.filter(binserial_no__icontains=bin_serial_number)
        return render(request, 'editpage.html', {'table_details': table_details, 'bin_serial_number': bin_serial_number})
      return render(request, 'editpage.html', {'bin_serial_number': None})
    
def update_details(request):
    if request.method == 'POST':
        bin_serial_number = request.POST['bin_serial_number']
        component1 = request.POST['component1']
        component2 = request.POST['component2']
        testing = request.POST['testing']
        remarks = request.POST['remarks']
        
        table_detail = TableDetails.objects.get(binserial_no=bin_serial_number)
        table_detail.component1 = component1
        table_detail.component2 = component2
        table_detail.testing = testing
        table_detail.remarks = remarks
        table_detail.date = timezone.now()
        table_detail.save()
        
        return redirect('editpage') 