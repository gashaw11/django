# SETUP

.\myvenv\Scripts\Activate

source myvenv/bin/activate

python -m venv myvenv

pip install -r requirements.txt 

http://127.0.0.1:8000/admin/

# #opening shell

python manage.py shell

from django.contrib.auth.models import User.

print(User.objects.all())  # Lists all users.

user = User.objects.get(username="admin").

user.set_password("new_secure_password").

user.save().

exit()

# #sql
SELECT * FROM myapp_product;



