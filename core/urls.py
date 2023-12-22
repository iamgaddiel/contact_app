
from django.urls import include, path
from django.contrib.auth.views import (
    LoginView, 
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetView,
    PasswordResetDoneView
)
from .views import (
    core_about_view, 
    core_contact_view, 
    core_contact_view, 
    create_user_success_view, 
    create_user_view, 
    Profile, 
    ProfileUpdate, 
    Login,
    LandingPageView
)

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', LandingPageView.as_view(), name='index'),
    path('about/', core_about_view, name = 'about'),
    path('contact/', core_contact_view, name = 'contact'),
     
    # Profile
    path('profile/<int:pk>/', Profile.as_view(), name = 'profile'),
    path('profile/update/<int:pk>/', ProfileUpdate.as_view(), name = 'profile_update'),

    # User
    path('create_user/', create_user_view, name='create_user_account'),
    path('create_user/success', create_user_success_view, name='create_user_success'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Reset password
    path('password-reset', PasswordResetView.as_view(template_name='core/password-reset.html'), name='password_reset'),
    path('password-reset-done', PasswordResetDoneView.as_view(template_name='core/password-reset-done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='core/password-reset-confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', PasswordResetCompleteView.as_view(template_name='core/password-reset-complete.html'), name='password_reset_complete'),

    # Other App
    path('contacts/', include('contact.urls')),
    path('adm/', include('_admin.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
