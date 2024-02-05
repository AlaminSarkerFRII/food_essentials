from django.urls import path
from .views import home, about, contact, CategoryView, ProductDetails, CategoryTitleView, CustomerRegistrationView,CustomerProfileView, address,UpdateAddress,PasswordChangeView,PasswordChangeDoneView

from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordResetForm , MyPasswordChangeForm, MySetPasswordForm


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('category-title/<val>', CategoryTitleView.as_view(), name='category-title'),
    path('category/<slug:val>', CategoryView.as_view(), name='category'),
    path('product-details/<int:pk>',
         ProductDetails.as_view(), name='product-details'),

    path('profile/', CustomerProfileView.as_view(), name='profile'),
    path('address/', address, name='address'),

    path('updateAddress/<int:pk>', UpdateAddress.as_view(), name='updateAddress'),

    
    # ---- Authentication Route---------------

    path('registration/',
         CustomerRegistrationView.as_view(), name='registration'),

    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='mainapp/login.html',authentication_form=LoginForm), name='login'),
    
  path('passwordchange/',
         auth_views.PasswordChangeView.as_view(
             template_name='mainapp/passwordchange.html',
             form_class=MyPasswordChangeForm,
             success_url='/passwordchangedone'
         ),
         name='passwordchange'),
    
    path('passwordchangedone/',
         auth_views.PasswordChangeDoneView.as_view(template_name='mainapp/passwordchangedone.html'), name='passwordchangedone'),
    
    path('logout/',
         auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
# ========== password-reset Routes ===========
     
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='mainapp/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='mainapp/password_reset_done.html'), name='password_reset_done'),
    
    path('password-reset-confirm/<uuid4>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='mainapp/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),
    
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='mainapp/password_reset_complete.html'), name='password_reset_complete'),

]
