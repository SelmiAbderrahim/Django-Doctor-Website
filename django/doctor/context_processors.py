from .models import Appointment

def get_notification(request):
    count = Appointment.objects.filter(accepted=False).count()
    data = {
        "count":count
    }
    return data