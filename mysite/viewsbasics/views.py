from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from random import choice
from django.views import View
from django.shortcuts import render

def funktionally(request):
    response = """<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Funktionally Page</title>
    <link rel="icon" href="https://ict.gctaa.net/resources/GCTAAfavicon.png">
    <style>
    body {
        margin: 4vw;
    }
    main {
        padding: 4vw;
        border: 1px dotted #777;
    }
    h1, footer {
        text-align: center;
    }
    footer {
        margin-top: 1vw;
    }
    a, a:visited {
        text-decoration: none;
        font-weight: bold;
        color: #C92; 
    }
    </style>
    </head>
    <body>
    <h1>Funktionally Page</h1>
    <p>
    This is the <i>Funktionally Page</i>.  It was returned as a literal string
    from a simple Django functional view that did nothing else but return it.
    </p>

    <footer>
    <a href="../viewsbasics/">Return to Viewbasics index page</a>
    </footer>
    </body>
    """
    return HttpResponse(response)


def danger(request):
    response = """<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Danger Page!</title>
    <link rel="icon" href="https://ict.gctaa.net/resources/GCTAAfavicon.png">
    <style>
    body {
        margin: 4vw;
    }
    main {
        padding: 4vw;
        border: 1px dotted #777;
    }
    h1, footer {
        text-align: center;
    }
    span {
        font-size: x-large;
        font-weight: bold;
        color: red;
    }
    footer {
        margin-top: 1vw;
    }
    a, a:visited {
        text-decoration: none;
        font-weight: bold;
        color: #C92; 
    }
    </style>
    </head>
    <body>
    <h1>Danger Page!</h1>
    <p>Your thing was: <span>"""+request.GET['thing']+"""</span></p>
    <p>You can learn more about <b>URL encoding</b> by clicking
    <a href="https://en.wikipedia.org/wiki/Percent-encoding">here</a>.</p>
    <footer>
    <a href="../viewsbasics/">Return to Viewbasics index page</a>
    </footer>
    </body>
    """
    return HttpResponse(response)


def safer(request):
    response = """<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Safer Page</title>
    <link rel="icon" href="https://ict.gctaa.net/resources/GCTAAfavicon.png">
    <style>
    body {
        margin: 4vw;
    }
    main {
        padding: 4vw;
        border: 1px dotted #777;
    }
    h1, footer {
        text-align: center;
    }
    span {
        font-size: x-large;
        font-weight: bold;
        color: red;
    }
    footer {
        margin-top: 1vw;
    }
    a, a:visited {
        text-decoration: none;
        font-weight: bold;
        color: #C92; 
    }
    </style>
    </head>
    <body>
    <h1>Safer Page</h1>
    <p>Your thing was: <span>"""+escape(request.GET['thing'])+"""</span></p>
    <footer>
    <a href="../viewsbasics/">Return to Viewbasics index page</a>
    </footer>
    </body>
    """
    return HttpResponse(response)


def prettyurldata(request, thing):
    response = """<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Pretty URL Data Page</title>
    <link rel="icon" href="https://ict.gctaa.net/resources/GCTAAfavicon.png">
    <style>
    body {
        margin: 4vw;
    }
    main {
        padding: 4vw;
        border: 1px dotted #777;
    }
    h1, footer {
        text-align: center;
    }
    span {
        font-size: x-large;
        font-weight: bold;
        color: red;
    }
    footer {
        margin-top: 1vw;
    }
    a, a:visited {
        text-decoration: none;
        font-weight: bold;
        color: #C92; 
    }
    </style>
    </head>
    <body>
    <h1>Pretty URL Data Page</h1>
    <p>Your thing was: <span>"""+escape(thing)+"""</span></p>
    <footer>
    <a href="../">Return to Viewbasics index page</a>
    </footer>
    </body>
    """
    return HttpResponse(response)

class Icecream(View):
    def get(self, request, flavor=''):
        x={'flavor':flavor}
        return render(request, 'viewsbasics/icecream.html', x)
class bigtext(View):
    def get(self, request, text=':3'):
        x = {'text':text}
        return render(request,'viewsbasics/bigtext.html', x)
class color(View):
    def get(self, request, color='000000'):
        r = [color[0]]
        r.append(color[1])
        red = ''.join(r)
        g = [color[2]]
        g.append(color[3])
        green = ''.join(g)
        b = [color[4]]
        b.append(color[5])
        blue = ''.join(b)
        x = {'red':red,'green':green,'blue':blue}
        return render(request,'viewsbasics/color.html', x)

class BMI(View):
    def get(self, request, h='h', w='w'):
        try:
            h = float(h)
            print(h)
            w = float(w)
            print(w)
            BMI = w/(h**2)
            print(BMI)
            x = {'BMI':BMI,'w':w, 'h':h}
            print(x)
            return render(request,'viewsbasics/BMI.html',x)
        except:
            print('error')
            return render(request, 'viewsbasics/BMIfail.html')

class RPC(View):
    def get(self, request, p='p', r='r'):
        try:
            p = float(p)/100
            r = float(r)
            pf = 1 - p
            prob = 100 - 100*(pf**r)

            print(p," ",pf," ",r," ",prob)
            if prob == 100:
                prob = "basicly 100"
            x = {'p':p*100,'r':r,'prob':prob}
            return render(request, 'viewsbasics/RPC.html', x)
        except:
            return render(request, 'viewsbasics/RPCfail.html') 

def bounce(request):
    places = [
        'https://www.python.org/',
        'https://ict.gctaa.net/',
        'https://www.dj4e.com/',
        'https://www.djangoproject.com/',
    ]
    return HttpResponseRedirect(choice(places))
