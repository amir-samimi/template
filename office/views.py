from django.shortcuts import render,HttpResponse

# Create your views here.
def officehome(request):
    return HttpResponse ("<h1> به سایت 118 خوش آمدید</h1>")
def makan(request,sazman):
    l=[{"onvan":"fani","titel":"Sazman Fani v Herfeei","addres":"شهرکرد بلوار رهبر ، سازمان فنی و حرفه ای","tell":"03832221111","img":"fani.jpg"},
       {"onvan":"kar","titel":"Edare Kar v omor ejtemaei","addres":"شهرکرد مجتمع ادارات اداره کار و رفاه","tell":"03832222222","img":"kar.jpg"},
       {"onvan":"tamin","titel":"Sazman Tamin ejtemaei","addres":"شهرکرد خیابان طالقانی ، سازمان تأمین اجتماعی","tell":"03832223333","img":"tamin.jpg"},
       {"onvan":"uni","titel":"Daneshgah shahrekord","addres":"شهرکرد بلوار رهبر ، دانشگاه شهرگرد","tell":"03832224444","img":"uni.jpg"}]
    d=l[0]
    for i in l:
        if (sazman==i["onvan"]):
            d=i
            return render(request,"office/showbrand.html",context=d)
    return HttpResponse("<h1>لطفا از بین این موارد انتخاب کنید </h1>\n <h2>fani,kar, tamin , uni</h2>")
