from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Event, Partner, WorkersTeam, WorkerProfile, Project, Action, ServiceProvider, Service, \
    RecipientServices
from django.shortcuts import redirect
from taggit.models import Tag
from .forms import *


def home(request):
    return render(request, 'logic/home.html')


def events_by_category(request, cat):
    events = Event.objects.filter(category=cat).order_by('-date')
    context = {"events": events}
    return render(request, 'logic/events.html', context)


def events_detailed(request, slug):
    event = get_object_or_404(Event, slug=slug)
    context = {"event": event}
    return render(request, 'logic/events_detailed.html', context)


def partner_list(request):
    partners = Partner.objects.all()
    context = {"partners": partners}
    return render(request, 'logic/partners.html', context)


def workers_list(request):
    partners = Partner.objects.filter(isWorker=True)
    context = {"partners": partners}
    return render(request, 'logic/partners.html', context)


def serviceprovider_list(request):
    partners = Partner.objects.filter(isSeviceGiver=True)
    context = {"partners": partners}
    return render(request, 'logic/partners.html', context)


def recipientservices_list(request):
    partners = Partner.objects.filter(isSeviceTaker=True)
    context = {"partners": partners}
    return render(request, 'logic/partners.html', context)


def partner_detailed(request, indef):
    worker = None
    workersTeams = None
    recipient_of_services = None
    gotet_sevices = None
    gived_sevices = None
    serviceprovider = None

    partner = get_object_or_404(Partner, indef=indef)
    actions = partner.action_set.all().order_by('-date')

    if partner.isWorker:
        worker = WorkerProfile.objects.get(partner=partner)
        workersTeams = WorkersTeam.objects.filter(workers=worker)
    if partner.isSeviceTaker:
        recipient_of_services = partner.recipientservices
        gotet_sevices = recipient_of_services.service_set.all()
    if partner.isSeviceGiver:
        serviceprovider = partner.serviceprovider
        gived_sevices = serviceprovider.service_set.all()

    context = {"partner": partner,
               "worker": worker,
               "workersTeams": workersTeams,
               "actions": actions,
               "recipient_of_services": recipient_of_services,
               "gotet_sevices": gotet_sevices,
               "serviceprovider": serviceprovider,
               "gived_sevices": gived_sevices,
               }

    return render(request, 'logic/partners_detailed.html', context)


def action_profile_add(request, indef):
    partner = get_object_or_404(Partner, indef=indef)
    form = ActionForm
    if request.method == "POST":
        form = ActionForm(request.POST)
        if form.is_valid():
            action = form.save(commit=False)
            action.partner = partner
            action.rel_manager = request.user
            action.save()
            return redirect('partner_detailed', indef=partner.indef)

    context = {"partner": partner,
               "form": form,
               }
    return render(request, 'logic/action_profile_add.html', context)


def service_list(request):
    services = Service.objects.all()
    context = {"services": services,
               }
    return render(request, 'logic/service_list.html', context)


def service_detailed(request, title):
    service = get_object_or_404(Service, title=title)
    context = {"service": service,
               }
    return render(request, 'logic/service_detailed.html', context)


def development_list(request):
    projects = Project.objects.filter(rel_manager=None)
    context = {"projects": projects}
    return render(request, 'logic/projects_list.html', context)


def partner_register(request):
    context = {}

    form = PartnerForm()

    if request.POST:
        form = PartnerForm(request.POST)
        if form.is_valid():
            partner = form.save(commit=False)
            partner.save()
            return redirect('partner_register_cont', indef=partner.indef)

    context['form'] = form
    return render(request, 'logic/partner_register.html', context)


def partner_register_cont(request, indef):
    form = PartnerFormSecond()

    partner = get_object_or_404(Partner, indef=indef)

    if request.POST:
        form = PartnerFormSecond(request.POST)
        if form.is_valid():
            partner.isWorker = form.instance.isWorker
            partner.isSeviceGiver = form.instance.isSeviceGiver
            partner.isStudent = form.instance.isStudent
            partner.isInvestor = form.instance.isWorker
            partner.save()
            return redirect('partner_register_last', indef=partner.indef)

    context = {'partner': partner, 'form': form}
    return render(request, 'logic/partner_register_cont.html', context)


def partner_register_last(request, indef):
    partner = get_object_or_404(Partner, indef=indef)

    workerform = WorkerProfileReg
    teamform = WorkersTeamReg
    projectform = ProjectReg
    errorList = {}

    if request.POST:
        workerform = WorkerProfileReg(request.POST)
        teamform = WorkersTeamReg(request.POST)
        projectform = ProjectReg(request.POST)

        if workerform.is_valid() and teamform.is_valid() and projectform.is_valid():
            workprof = WorkerProfile.objects.get(partner=partner)
            workprof.org = request.POST['org']
            workprof.position = request.POST['position']
            team = teamform.save(commit=False)
            team.titleW = request.POST['titleW']
            team.save()
            team.rel_partner = partner
            team.workers.add(partner.workerprofile)
            workersStr = request.POST['workers']
            workersEmailsList = workersStr.split()
            for workerEmail in workersEmailsList:
                try:
                    partner = get_object_or_404(Partner, email=workerEmail)
                    if partner.isWorker:
                        worker = partner.workerprofile
                        team.workers.add(worker)
                    else:
                        partner.isWorker = True
                        worker = partner.workerprofile
                        team.workers.add(worker)
                except:
                    error = "Немає користувача з таким email:" + workerEmail
                    context = {'partner': partner, 'workerform': workerform, 'teamform': teamform,
                               'projectform': projectform, 'error': error}
                    return render(request, 'logic/partner_register_last.html', context)
            project = projectform.save(commit=False)
            project.projectTeams = team
            workprof.save()
            team.save()
            project.save()
            return redirect('home')

    context = {'partner': partner, 'workerform': workerform, 'teamform': teamform, 'projectform': projectform}
    return render(request, 'logic/partner_register_last.html', context)


def development_take(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.rel_manager = request.user
    project.save()
    return redirect('project_detailed', pk=pk)


def my_projects(request):
    projects = Project.objects.filter(rel_manager=request.user)

    context = {'projects': projects}

    return render(request, 'logic/my_projects_list.html', context)


def project_detailed(request, pk):
    project = get_object_or_404(Project, pk=pk)
    workers = WorkerProfile.objects.filter(workersteam=project.projectTeams)
    context = {'project': project,
               'workers': workers, }
    return render(request, 'logic/my_project_detailed.html', context)
