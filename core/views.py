from django.core.mail import send_mail
from django.conf import settings
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

        # Send Email Notification
        subject = f"New Contact Request from {name}"
        email_message = f"""
        New contact request received:

        Name: {name}
        Phone: {phone}
        Email: {email}
        Preferred Time: {preferred_time}
        Project Type: {project_type}
        Message: {message}
        """
        
        recipient_list = ['ankitnandoliya32@gmail.com', 'colourcraft@gmail.com']
        
        try:
            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                recipient_list,
                fail_silently=False,
            )
        except Exception as e:
            print(f"Error sending email: {e}")

        success = True

    return render(request, 'core/index.html', {'success': success})
