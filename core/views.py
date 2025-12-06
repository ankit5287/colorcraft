from django.shortcuts import render
from .models import Contact

def contact_view(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        preferred_time = request.POST.get('preferred-time')  # Note the hyphen from HTML name
        project_type = request.POST.get('project-type')      # Note the hyphen from HTML name
        message = request.POST.get('message')

        contact = Contact(
            name=name,
            phone=phone,
            email=email,
            preferred_time=preferred_time,
            project_type=project_type,
            message=message
        )
        contact.save()
        success = True

    return render(request, 'core/index.html', {'success': success})
