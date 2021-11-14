from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from contacts.models import Contact

def contact(request):
    
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #if inquiry alredy made
        print('request', request.user)
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(Listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for these listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(Listing = listing, Listing_id = listing_id, name = name, email = email, phone = phone, message = message, user_id = user_id)

        contact.save()

        send_mail(
            subject='VT Real Estate Enquiry - {listing}'.format(listing=listing),
            message='The enquiry has been made by you for {listing} our Realtor will get back to you.\nThank you for your showing interest in VT Real Estate'.format(listing = listing),
            from_email='vikatthakur@gmail.com',
            recipient_list=[email, 'vikat2thakur@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted successfully. a realtor will get back to you.')

        return redirect('/listings/'+listing_id)
    

