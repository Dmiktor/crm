from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Event, Partner, WorkersTeam, WorkerProfile, Project, Action, ServiceProvider, Service, \
    RecipientServices
from django.shortcuts import redirect
from taggit.models import Tag
from .forms import ActionForm


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


def partner_detailed(request, name):
    worker = None
    workersTeams = None
    recipient_of_services = None
    gotet_sevices = None
    gived_sevices = None
    serviceprovider = None

    partner = get_object_or_404(Partner, name=name)
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


def action_profile_add(request, name):
    partner = get_object_or_404(Partner, name=name)
    if request.method == "POST":
        form = ActionForm(request.POST)
        if form.is_valid():
            action = form.save(commit=False)
            action.partner = partner
            action.rel_manager = request.user
            action.save()
            return redirect('partner_detailed', name=partner.name)

    else:
        form = ActionForm
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


def projects_list_by_category(request, cat):
    project = Project.objects.filter(category=cat)
    context = {"project": project}
    return render(request, 'logic/projects_list.html', context)