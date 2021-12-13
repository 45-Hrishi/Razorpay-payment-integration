from django.http import response
from django.shortcuts import redirect, render
import razorpay
from .models import Donation
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .forms import DonationForm
import razorpay



# Create your views here.

#rzp_test_asEBn8bj4p0Fq7 key
#qbr88MrwoCIFY3xrmW9OfDgq secret

def home(request):
    return render(request, 'home.html')

def donate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        amount = int(request.POST.get('amount'))*100#paise
       
        
        
        client = razorpay.Client(auth=("rzp_test_asEBn8bj4p0Fq7", "qbr88MrwoCIFY3xrmW9OfDgq"))
        try:
            payment_responce = client.order.create(dict(amount=amount,currency="INR",payment_capture='1'))
            
            order_id = payment_responce['id']
            order_status = payment_responce['status']

            if order_status == 'created':
                donation = Donation(
                    amount = amount,
                    name = name,
                    email = email,
                    phone_no = phone_no,
                    order_id = order_id,
                )
                donation.save()
                payment_responce['name'] = name            
                payment_responce['email'] = email            
                payment_responce['phone_no'] = phone_no            
                payment_responce['amount'] = amount           

                form = DonationForm(request.POST or None)
                return render(request,'donate.html',{'form':form,'payment':payment_responce})
        except:
            messages.warning(request, 'Please Enter Correct Amount. Amount Should be in rupppes only and amount should be positive.')         
            form = DonationForm(request.POST or None)
            return render(request,'donate.html',{'form':form})

    form = DonationForm()
    return render(request,'donate.html',{'form':form})

def success(request):
    response = request.POST
    print(response)
    client = razorpay.Client(auth = ("rzp_test_asEBn8bj4p0Fq7", "qbr88MrwoCIFY3xrmW9OfDgq"))
    params_dict={
        'razorpay_order_id':response['razorpay_order_id'],
        'razorpay_payment_id':response['razorpay_payment_id'],
        'razorpay_signature':response['razorpay_signature']
    }
    
    try:  
        status = client.utility.verify_payment_signature(params_dict)    
        donation = Donation.objects.get(order_id=response['razorpay_order_id'])
        donation.paid = True
        donation.payment_id = response['razorpay_payment_id']
        donation.save()
        return render(request,'success.html',{'status':True})
    except:
        return render(request,'success.html',{'status':False})
