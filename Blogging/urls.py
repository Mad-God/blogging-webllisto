from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import (
        LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, 
        PasswordResetConfirmView, PasswordResetCompleteView, 
    )
from user import views as u_views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    
    # app's urls
    path('', u_views.index,name = 'index'),
    path('user/', include('user.urls', namespace = 'user')),
    path('blog/', include('blog.urls', namespace = 'blog')),
    # path('shop/', include('shop.urls', namespace = 'shop')),

    
    # authentication urls
    path('login/', u_views.login,name = 'login'),
    path('logout/', u_views.logout,name = 'logout'),
    path('signup/', u_views.signup,name = 'signup'),

    # for timymce
    path('tinymce/', include('tinymce.urls')),

    
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# if settings.DEBUG:
#     urlpatterns += [(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#         (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.STATIC_ROOT,
#         })]
