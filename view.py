import random
from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.emailspam import predict_spam
from myapp.models import *
# from myapp.pred import predict
from myapp.phishing_detection import detect_phishing, getResult


def login(request):
    return render(request,'loginindex.html')
def login_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    lobj = Login.objects.filter(username=username, password=password)
    if lobj.exists():
        lobj1 = Login.objects.get(username=username, password=password)
        request.session['lid'] = lobj1.id
        if lobj1.type == 'admin':
            request.session['lid'] = lobj1.id
            return HttpResponse('<script>alert("Success");window.location="/myapp/admin_home/"</script>')
        elif lobj1.type == 'user':
            return HttpResponse('<script>alert("Success");window.location="/myapp/user_home/"</script>')
        else:
            return HttpResponse('''<script>alert('invalid user');window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert('wrong username or password');window.location='/myapp/login/'</script>''')

def admin_home(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')
    return render(request,'admin/index.html')


def logout(request):
    request.session['lid']=""
    return redirect('/myapp/login/')

def forgotpassword(request):
    return render(request,'forgot.html')
def forgotpassword_post(request):
    from django.core.mail import send_mail
    from django.conf import settings
    address = request.POST['textfield']
    l=Login.objects.filter(username=address)
    if l.exists():
        p=random.randint(0000,9999)
        Login.objects.filter(username=address).update(password=p)
        send_mail("Send Scuccessfully", str(p), settings.EMAIL_HOST_USER, [address])
        return HttpResponse('''<script>alert('Successfully Changed');window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert('Invalid email address);window.location='/myapp/forgotpassword/'</script>''')





def admin_change_password(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')

    return render(request,'admin/change pass.html')

def admin_change_password_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')

    Current_password = request.POST['textfield']
    new_password = request.POST['textfield2']
    retype_password = request.POST['textfield2']
    lid = request.session['lid']

    var =Login.objects.get(id=lid)
    if var.password == Current_password:
        if retype_password == new_password:
            Login.objects.filter(id=lid,password=Current_password).update(password=retype_password)
            return HttpResponse('''<script>alert('Password updated Successfully');window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert('password does not match');window.location='/myapp/admin_change_password/'</script>''')
    else:
        return HttpResponse('''<script>alert('Worng password');window.location='/myapp/admin_change_password/'</script>''')



def  admin_send_replay(request,id):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')
    return render(request,'admin/send replay.html',{'id':id})
def  admin_send_replay_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')

    Replay = request.POST['textarea']
    id = request.POST['id']

    var = Complaint.objects.get(id=id)
    var.reply = Replay
    var.status = 'replied'
    var.save()
    return HttpResponse('''<script>alert('Replied Successfully');window.location='/myapp/admin_view_complaint/#about'</script>''')


def  admin_view_app_review(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')
    var = Review.objects.all()
    return render(request,'admin/view app review.html',{'data':var})
def  admin_view_app_review_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')

    From = request.POST['textfield']
    To = request.POST['textfield2']
    var = Review.objects.filter(date__range=[From, To])
    return render(request,'admin/view app review.html',{'data':var})


def  admin_view_complaint(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')
    var = Complaint.objects.all()
    return render(request,'admin/view complaint.html',{'data':var})
def  admin_view_complaint_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')

    From = request.POST['textfield']
    To = request.POST['textfield2']
    var = Complaint.objects.filter(date__range=[From,To])
    return render(request,'admin/view complaint.html',{'data':var})


def  admin_view_customer(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')
    var = User.objects.all()
    return render(request, 'admin/view customer.html', {'data': var})
def  admin_view_customer_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')

    search = request.POST['textfield']
    var = User.objects.filter(username__icontains=search)
    return render(request,'admin/view customer.html',{'data':var})

#---------------------------------------------------------------------------------------------------------------


def user_home(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')
    return render(request,'user/phish index.html')


def user_change_password(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')
    return render(request,'user/change pass.html')
def user_change_password_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')

    Current_password = request.POST['textfield']
    print(Current_password,'----------------cp')
    new_password = request.POST['textfield2']
    print(new_password,'--------------------np')
    retype_password = request.POST['textfield3']
    print(retype_password,'------------------rp')

    lid = request.session['lid']

    print (lid,'==================lid')

    var = Login.objects.get(id=lid)
    if var.password == Current_password:
        if retype_password == new_password:
            Login.objects.filter(id=lid, password=Current_password).update(password=retype_password)
            return HttpResponse(
                '''<script>alert('Password updated Successfully');window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse(
                '''<script>alert('password does not match');window.location='/myapp/user_change_password/'</script>''')
    else:
        return HttpResponse('''<script>alert('Worng password');window.location='/myapp/user_change_password/'</script>''')





def user_edit_profile(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')
    lid = request.session['lid']
    var = User.objects.get(LOGIN_id=lid)
    return render(request,'user/edit profile.html',{'data':var})

def user_edit_profile_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')

    Name = request.POST['textfield']
    E_mail = request.POST['textfield2']
    phone = request.POST['textfield3']
    gender = request.POST['gender']
    place =request.POST['place']
    lid = request.session['lid']

    l = Login.objects.get(id=lid)
    l.username = E_mail
    l.save()

    var = User.objects.get(LOGIN_id=lid)
    var.username = Name
    var.email = E_mail
    var.phone_no = phone
    var.gender = gender
    var.place=place
    var.save()
    return HttpResponse('''<script>alert('Profile updated Successfully');window.location='/myapp/user_view_profile/'</script>''')





def user_image_forgery(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')
    return render(request,'user/image forgery.html')
def user_image_forgery_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')
    import numpy as np
    import matplotlib.pyplot as plt

    np.random.seed(2)
    from PIL import Image, ImageChops, ImageEnhance
    photo=request.FILES['fileField']
    date=datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
    fs=FileSystemStorage()
    fs.save(date,photo)
    path=fs.url(date)
    mpath = "C:\\Users\\aksha\\PycharmProjects\\M_D_threat_dectection"+path
    highlightpath = "C:\\Users\\aksha\\PycharmProjects\\M_D_threat_dectection\\media\\high\\"+date

    def ela_analysis2(image_path, quality=90):
        # Open the original image
        original = Image.open(image_path).convert("RGB")

        # Save at lower quality to force recompression
        temp_path = "temp_ela.jpg"
        original.save(temp_path, "JPEG", quality=quality)

        # Reopen the recompressed image
        compressed = Image.open(temp_path)

        # Compute the difference (ELA)
        ela_image = ImageChops.difference(original, compressed)

        # Enhance the differences
        enhancer = ImageEnhance.Contrast(ela_image)
        ela_image = enhancer.enhance(20)  # Increase contrast to highlight changes

        ela_image.save(highlightpath)

    
    # Example usage
    ela_analysis2(mpath)

    def convert_to_ela_image(path, quality):
        temp_filename = 'temp_file_name.jpg'

        image = Image.open(path).convert('RGB')
        image.save(temp_filename, 'JPEG', quality=quality)
        temp_image = Image.open(temp_filename)

        ela_image = ImageChops.difference(image, temp_image)

        extrema = ela_image.getextrema()
        max_diff = max([ex[1] for ex in extrema])
        if max_diff == 0:
            max_diff = 1
        scale = 255.0 / max_diff

        ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)

        return ela_image

    image_size = (128, 128)

    def prepare_image(image_path):
        return np.array(convert_to_ela_image(image_path, 90).resize(image_size)).flatten() / 255.0

    from tensorflow import keras
    model = keras.models.load_model(r'C:\Users\aksha\PycharmProjects\M_D_threat_dectection\myapp\model_casia_run1.h5')

    class_names = ['fake', 'real']

    real_image_path = mpath
    image = prepare_image(real_image_path)
    image = image.reshape(-1, 128, 128, 3)
    y_pred = model.predict(image)
    y_pred_class = np.argmax(y_pred, axis=1)[0]
    print(f'Class: {class_names[y_pred_class]} Confidence: {np.amax(y_pred) * 100:0.2f}')
    out=f'Class: {class_names[y_pred_class]} Confidence: {np.amax(y_pred) * 100:0.2f}'

    return render(request,'user/image forgery.html',{'out':out,"img":date})




def user_mail_spamming(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')
    return render(request,'user/mail spamming.html')
def user_mail_spamming_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')
    content=request.POST['textarea']
    res=predict_spam(content)

    print(res)

    return render(request,'user/mail spamming.html',{'result':res[0],'img':res[1]})




def user_send_complaint(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')
    return render(request ,'user/send complaint.html')

def user_send_complaint_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')

    date = datetime.now().today()
    complaint = request.POST['textarea']
    lid = request.session['lid']

    var = Complaint()
    var.date = date
    var.complaint = complaint
    var.status = 'pending'
    var.reply = 'pending'
    var.USER = User.objects.get(LOGIN_id=lid)
    var.save()
    return HttpResponse('''<script>alert('send successfully');window.location='/myapp/user_view_replay/'</script>''')









def user_send_review(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')
    return render(request,'user/send review.html')
def user_send_review_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')

    review = request.POST['textarea']

    rating = request.POST['rating']
    date = datetime.now().today()
    lid = request.session['lid']

    var = Review()
    var.date = date
    var.rating = rating
    var.review = review
    var.USER = User.objects.get(LOGIN_id=lid)
    var.save()
    return HttpResponse('''<script>alert('send successfully');window.location='/myapp/user_home/'</script>''')



def user_url(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')
    return render(request,'user/url.html')




def user_url_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')

    url = request.POST['textfield']
    phishing_data = getResult(url)
    # phishing_data = "Legitimate"
    # phishing_data = detect_phishing(url)
    print(phishing_data["status"],'---hiii---')
    # Pass all data to the template
    status = phishing_data["status"].lower()
    if 'safe' not in status and 'legitimate' not in status:
        status = 'suspicious'
    else:
        status = 'safe'
    return render(request, 'user/url.html', {
        "res1": url,  # Input URL
        # "res2":"Legitimate",  # Phishing Status
        "res2": status,  # Phishing Status
        # "res2": phishing_data["status"].lower,  # Phishing Status
        "res3": phishing_data["confidence"],  # Confidence Level
        "res4": phishing_data["url_length"],  # URL Length
        "res5": phishing_data["contains_ip"],  # Contains IP Address
        "res6": phishing_data["hyphen_count"],  # Hyphen Count
        "res7": phishing_data["@_symbol_count"],  # @ Symbol Count
        "res8": phishing_data["subdomain_count"],  # Subdomain Count
        "res9": phishing_data["https_status"],  # HTTPS Status
        "res10": phishing_data["domain_age"],  # Domain Age
        "res11": datetime.now().today()  # Analysis Time
    })


def user_reg(request):
    return render(request,'user/signupindex.html')

def user_reg_post(request):
    Username = request.POST['textfield']
    E_mail = request.POST['textfield2']
    Phone = request.POST['textfield5']
    gender = request.POST['gender']
    place = request.POST['textfield6']
    Confrim_password = request.POST['textfield4']

    if Login.objects.filter(username=E_mail).exists():
        return HttpResponse('''<script>alert('Email is already registered');window.location='/myapp/user_reg/'</script>''')


    l = Login()
    l.username = E_mail
    l.password = Confrim_password
    l.type = 'user'
    l.save()

    var = User()

    var.LOGIN = l
    var.username = Username
    var.email = E_mail
    var.phone_no = Phone
    var.place = place
    var.gender = gender
    var.save()

    return HttpResponse('''<script>alert('Account Created Successfully');window.location='/myapp/login/'</script>''')

def user_view_profile(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')

    lid = request.session['lid']
    var = User.objects.get(LOGIN_id=lid)
    return render(request,'user/view profile.html',{'data':var})






def user_view_replay(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')
    lid = request.session['lid']
    var = Complaint.objects.filter(USER__LOGIN_id=lid)
    return render(request,'user/view replay.html',{'data':var})
def user_view_replay_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert('please login');window.location='/myapp/login/'</script>''')

    From = request.POST['textfield']
    To = request.POST['textfield2']
    lid = request.session['lid']
    var = Complaint.objects.filter(USER__LOGIN_id=lid,date__range=[From,To])
    return render(request,'user/view replay.html',{'data':var})



