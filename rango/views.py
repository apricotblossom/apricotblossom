from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login 
from rango.models import Category, Page, UserProfile
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from rango.webhose_search import run_query
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login
from registration.backends.simple.views import RegistrationView
from django.utils import timezone
from django.db.models import Sum
from django.views.decorators.csrf import csrf_protect



def index(request): 
    #context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    request.session.set_test_cookie()
    category_list = Category.objects.order_by('-likes')[:5] 
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,'pages':page_list}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    response = render(request,'rango/index.html',context=context_dict)
    return response


def get_server_side_cookie(request,cookie,default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request,'visits','1'))
    last_visit_cookie = get_server_side_cookie(request,'last_visit',str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],'%Y-%m-%d %H:%M:%S')
    if(datetime.now() - last_visit_time).days>0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits


def show_category(request, category_name_slug): 
    context_dict = {}
    try: 
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category 
    except Category.DoesNotExist: 
        context_dict['category'] = None 
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)

def add_category(request): 
    form = CategoryForm()
    if request.method == 'POST': 
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True) 
            
            return index(request) 

        else: 
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try: 
        category = Category.objects.get(slug=category_name_slug)
        #username = User.objects.get(slug=user_name_slug)
    except Category.DoesNotExist: 
        category = None
        #username = None

    form = PageForm() 
    if request.method == 'POST': 
        form = PageForm(request.POST) 
        if form.is_valid(): 
            if category: 
                page = form.save(commit=False) 
                page.category = category
                if request.user.is_authenticated():
                    page.username = request.user
                page.save()
                return show_category(request, category_name_slug)
        else: 
            print(form.errors)
    
    context_dict = {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)

@csrf_protect
def register(request): 
    registered = False
    if request.method == 'POST': 
        user_form = UserForm(data=request.POST) 
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid(): 
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False) 
            profile.user = user

            if 'picture' in request.FILES: 
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True 
        else:
            print(user_form.errors, profile_form.errors)

    else: 
        user_form = UserForm() 
        profile_form = UserProfileForm()
    
    return render(request, 
                  'rango/register.html', 
                  {'user_form': user_form, 
                  'profile_form': profile_form, 
                  'registered': registered})

@csrf_protect
def user_login(request):
    if request.method == 'POST': 
        username = request.POST.get('username') 
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user: 
            if user.is_active: 
                login(request, user) 
                return HttpResponseRedirect(reverse('index')) 
            else: 
                return HttpResponse("Your Rango account is disabled.")
        else: 
            print("Invalid login details: {0}, {1}".format(username, password)) 
            return HttpResponse("Invalid login details supplied.")
    else: 
        return render(request, 'rango/login.html', {})

def some_view(request): 
    if not request.user.is_authenticated(): 
        return HttpResponse("You are logged in.") 
    else: 
        return HttpResponse("You are not logged in.")

@login_required 
def restricted(request): 

    return HttpResponse("Since you're logged in, you can see this text!")

@login_required 
def user_logout(request): 
    logout(request) 
    return HttpResponseRedirect(reverse('index'))

def search(request): 
    result_list = []
    if request.method == 'POST':
        query = request.POST['query'].strip() 
        if query:
            result_list = run_query(query)
    return render(request, 'rango/search.html', {'result_list': result_list})

def get_category_list(max_results=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Category.objects.filter(name__istartswith=starts_with)

    if max_results > 0:
        if len(cat_list) > max_results:
            cat_list = cat_list[:max_results]

    return cat_list

def suggest_category(request):
    cat_list = []
    starts_with = ''

    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    cat_list = get_category_list(8, starts_with)
    
    return render(request, 'rango/cats.html', {'cats': cat_list })


def contact(request):
    return render(request, 'rango/contact.html')

def gamereview(request):
    category_list = Category.objects.order_by('-likes')[12:16]
    context_dict = {'categories': category_list}
    response = render(request,'rango/game-review.html',context=context_dict)
    return response

def gamereview2(request):
    category_list = Category.objects.order_by('-likes')[8:12]
    context_dict = {'categories': category_list}
    response = render(request,'rango/game-review2.html',context=context_dict)
    return response

def gamereview3(request):
    category_list = Category.objects.order_by('-likes')[4:8]
    context_dict = {'categories': category_list}
    response = render(request,'rango/game-review3.html',context=context_dict)
    return response

def age_check(user):
    return user.userprofile.age>=18

@user_passes_test(age_check)
def adultgamereview(request):
    category_list = Category.objects.order_by('-likes')[:4]
    context_dict = {'categories': category_list}
    response = render(request, 'rango/adult-game-review.html', context=context_dict)
    return response


def gamenews(request):
    return render(request, 'rango/post.html')
    
def deadbydaylightnews(request):
    return render(request, 'rango/deadbydaylight.html')

def conanexilesnews(request):
    return render(request, 'rango/conanexiles.html')

def ps4news(request):
    return render(request, 'rango/ps4news.html')

def marionews(request):
    return render(request, 'rango/marionews.html')

@user_passes_test(age_check)
def adultgamenews(request):
    return render(request, 'rango/adultgamenews.html')

def senrankaguraburstrenewal(request):
    return render(request, 'rango/senrankaguraburstrenewal.html')

def gta6news(request):
    return render(request, 'rango/gta6.html')

def deadoralivenews(request):
    return render(request, 'rango/deadoralive6.html')

@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect('index')
        else:
            print(form.errors)

    context_dict = {'form': form}

    return render(request, 'rango/profile_registration.html', context_dict)


@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm(
            {'age':userprofile.age, 'website': userprofile.website, 'picture': userprofile.picture})
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)
    return render(request, 'rango/profile.html',
            {'userprofile': userprofile, 'selecteduser': user, 'form': form})




class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')


@login_required
def list_profiles(request):
    user_list = User.objects.all()
    userprofile_list = UserProfile.objects.all()
    return render(request, 'rango/list_profiles.html', {'user_list': user_list, 'userprofile_list': userprofile_list})


def get_category_list(max_results=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Category.objects.filter(name__istartswith=starts_with)
    if max_results > 0:
        if len(cat_list) > max_results:
            cat_list = cat_list[:max_results]
    return cat_list


def suggest_category(request):
    cat_list = []
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    cat_list = get_category_list(8, starts_with)

    return render(request, 'rango/cats.html', {'cats': cat_list })


@login_required
def auto_add_page(request):
    cat_id = None
    url = None
    title = None
    context_dict = {}
    if request.method == 'GET':
        cat_id = request.GET['category_id']
        url = request.GET['url']
        title = request.GET['title']
        if cat_id:
            category = Category.objects.get(id=int(cat_id))
            p = Page.objects.get_or_create(category=category,
                title=title, url=url)
            pages = Page.objects.filter(category=category).order_by('-views')
            # Adds our results list to the template context under name pages.
            context_dict['pages'] = pages
    return render(request, 'rango/page_list.html', context_dict)


@login_required
def like_category(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']
        likes = 0
    if cat_id:
        cat = Category.objects.get(id=int(cat_id))
        if cat:
            likes = cat.likes + 1
            cat.likes =  likes
            cat.save()
    return HttpResponse(likes)


def track_url(request):
    page_id = None
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
    if page_id:
        try:
            page = Page.objects.get(id=page_id)
            page.views = page.views + 1
            page.save()
            return redirect(page.url)
        except:
            return HttpResponse("Page id {0} not found".format(page_id))
    print("No page_id in get string")
    return redirect(reverse('index'))

























