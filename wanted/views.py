from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.

from rest_framework import viewsets
from .serializers import CompanySerializer
from .models import Company
from .forms import CompanyCreateForm

# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

def company_create(request):
    """
    채용공고 등록
    """
    if request.method == 'POST':
        form = CompanyCreateForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            return redirect('wanted:company')
    else:
        form = CompanyCreateForm()
    context = {'form':form}
    return render(request, 'company/company_form.html',context)

def company_list(request):
    """
    채용공고 출력
    """
    company_list = Company.objects.all()
    context = {'company_list':company_list}
    return render(request, 'company/company_list.html',context)

def company_delete(request,company_id):
    """
    채용공고 삭제
    """
    company = Company.objects.get(id=company_id)
    company.delete()
    return redirect('wanted:company')

def company_edit(request,company_id):
    """
    채용공고 수정
    """
    company = get_object_or_404(Company, pk=company_id)
    if request.method == "POST":
        form = CompanyCreateForm(request.POST, instance=company)
        if form.is_valid():
            company=form.save(commit=False)
            company.save()
            return redirect('wanted:detail', company_id=company.id)
    else:
        form = CompanyCreateForm(instance=company)
    context = {'form':form}
    return render(request, 'company/company_form.html',context)

def company_detail(request, company_id):
    """
    채용공고 내용 출력
    """
    company = Company.objects.get(id=company_id)
    context = {'company':company}
    return render(request, 'company/company_detail.html',context)
