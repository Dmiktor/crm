from django.contrib import admin
from .models import Event, Partner, WorkerProfile, WorkersTeam, Project, Action, ServiceProvider, Service, \
    RecipientServices, ProjectSectionType, ProjectSection,ExpertiseRequest

# Register your models here.

admin.site.register(Event)
admin.site.register(Partner)
admin.site.register(WorkerProfile)
admin.site.register(WorkersTeam)
admin.site.register(Project)
admin.site.register(Action)
admin.site.register(ServiceProvider)
admin.site.register(Service)
admin.site.register(RecipientServices)
admin.site.register(ProjectSectionType)
admin.site.register(ProjectSection)
admin.site.register(ExpertiseRequest)
