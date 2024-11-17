import bcrypt
from healthapp.models import User
from django.shortcuts import redirect

# decorator function for views that should only be accessible by authenticated users
def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(stored_password: str, provided_password: str) -> bool:
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))

def register_user(username: str, password: str):
    hashed_password = hash_password(password)
    user = User(username=username, password=hashed_password)
    user.save()

def logout_user(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('login')

def authenticate_user(username: str, password: str):
    try:
        user = User.objects.get(username=username)
        if verify_password(user.password, password):
            return user # authentication successful
    except User.DoesNotExist:
        pass
    return None # authentication failed