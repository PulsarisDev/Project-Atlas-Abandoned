#region import
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from PIL import Image
import configparser
import hashlib
#endregion

#region loadConfig
print("Loading configurations...")
try:
    config = configparser.ConfigParser()
    config.readfp(open('config.ini'))
#endregion

#region OperateFunction
def GetProfilePictureHash(Filename):
    byte = bytes()
    hash = hashlib.sha256()
    img = Image.open('./{}.png'.format(Filename))
    Width,Height = img.size
    byte += struct.pack('>1',Width)
    byte += struct.pack('>1',Height)
    for x in range(Width):
        for y in range(Height):
            tmp = img.getdata()[y*Width+x]
            if tmp[3] == 0x00:
                byte += struct.pack('>I',0)
            else:
                byte += struct.pack('>B',tmp[3])
                byte += struct.pack('>B',tmp[0])
                byte += struct.pack('>B',tmp[1])
                byte += struct.pack('>B',tmp[2])
    hash.update(byte)
    return hash.hexdigest()
#endregion

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
