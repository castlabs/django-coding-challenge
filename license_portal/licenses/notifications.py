from typing import List, Any

from django.core.mail import send_mail
from django.template import Template
from django.template.loader import get_template


DEFAULT_FROM_EMAIL = 'noreply@email.com'


class EmailNotification:
    """ A convenience class to send email notifications
    """
    subject = None  # type: str
    from_email = DEFAULT_FROM_EMAIL  # type: str
    template_path = None  # type: str

    @classmethod
    def load_template(cls) -> Template:
        """Load the configured template path"""
        return get_template(cls.template_path)

    @classmethod
    def send_notification(cls, recipients: List[str], context: Any):
        """Send the notification using the given context"""
        template = cls.load_template()
        message_body = template.render(context=context)
        send_mail(cls.subject, message_body, cls.from_email, recipients, fail_silently=False)
