import random
from django.core.mail import send_mail

def send_otp(request):
    if request.method == "POST":
        email = request.POST.get('email')
        otp_code = str(random.randint(100000, 999999))
        
        # حفظ الرمز في الجلسة (Session) للتحقق منه لاحقاً
        request.session['otp'] = otp_code
        request.session['user_email'] = email
        
        # إرسال الإيميل
        send_mail(
            'رمز التحقق الخاص بمنصة الريادة',
            f'رمزك هو: {otp_code}',
            'rachgifts@gmail.com',
            [email],
        )
        return redirect('verify_otp_page')

def set_alert(request, company_id):
    if request.method == "POST":
        target = request.POST.get('target_price')
        company = Company.objects.get(id=company_id)
        
        # حفظ التنبيه في قاعدة البيانات
        PriceAlert.objects.create(
            user=request.user,
            company=company,
            target_price=target
        )
        return render(request, 'success_alert.html')
