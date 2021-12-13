# Razorpay-payment-integration
NGO website using HTML, CSS, JS, Django and payment gateway integration using 'Razorpay'.

- create project using django-admin startproject 'payment_gateway'.
- create app inside project using py manage.py startapp 'payment'.
- create model 'Donation'.
- make all migrations first using py manage.py makemigartions.
- migrate all changes into database using py manage.py migrate.
- create account at 'razorpay' and do necessary steps according to razorpay python documentation.
- created django model form 'DonationForm' and connect both razorpay and django modelform.
- used bootstrap's  'crispy forms' for styling forms and use bootstrap for other styling.
- created another payment button using razorway latest feature.
- You can run the server using py.manage.py runserver
