from django.shortcuts import render

def showindex(req):
     s={
        "101":{"name":"venkat","marks":[20,30,40,50,60,70]},
        "102":{"name":"sraven","marks":[55,25,35,45,55,100]},
        "103":{"name":"jagadesh","marks":[21, 31, 41, 51, 61, 71]},
        "104": {"name": "MANOHAR","marks":[10,35,26,63,30,35]}
    }
     return render(req,"indexx.html",{"data":s})
