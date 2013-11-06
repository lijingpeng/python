from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body> Time:%s</body></html>" %now
    return HttpResponse(html)

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body> In %s hours, it will be %s</body></html>" % (offset, dt)
    return HttpResponse(html)

# using model system
def m_current_datetime(response):
    now = datetime.datetime.now()
    t = get_template('m_current_datetime.html')
    #Template("<html></body> It is now: {{ current_date }}.</body></html>")
    html = t.render(Context( { 'current_date': now} ))
    return HttpResponse(html)
