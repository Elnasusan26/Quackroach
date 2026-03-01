from django.core.management.base import BaseCommand
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from datetime import timedelta
from api.models import Executor

class Command(BaseCommand):
    help = 'Checks user inactivity and notifies executors with professional HTML emails.'

    def handle(self, *args, **options):
        # 6-month threshold
        threshold = timezone.now() - timedelta(days=180)
        
        # Target Active executors whose users are inactive
        executors = Executor.objects.filter(
            user__last_login__lt=threshold,
            status='Active'
        )

        for executor in executors:
            subject = f"Security Protocol Initiated: {executor.user.full_name}"
            
            # Context for the HTML template
            context = {
                'executor_name': executor.name,
                'user_name': executor.user.full_name,
                'site_url': 'http://localhost:5173' # Change to your production domain later
            }

            # Render HTML and create plain-text fallback
            html_content = render_to_string('emails/deadman_notification.html', context)
            text_content = strip_tags(html_content)

            msg = EmailMultiAlternatives(
                subject,
                text_content,
                None, # Uses DEFAULT_FROM_EMAIL from settings
                [executor.email]
            )
            msg.attach_alternative(html_content, "text/html")
            
            try:
                msg.send()
                executor.status = 'Verification_Pending'
                executor.save()
                self.stdout.write(self.style.SUCCESS(f"Professional alert sent to {executor.name}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to send to {executor.name}: {str(e)}"))