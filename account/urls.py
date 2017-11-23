# -*- coding: utf-8 -*-

from django.contrib.auth import views as auth_views

from django.conf.urls import url

from account import views as account_views

urlpatterns = [
	url(r'^login/$', auth_views.LoginView.as_view(), name = 'login'),
	url(r'^logout/$', auth_views.LogoutView.as_view(), name = 'logout'),
	url(r'^logout-then-login/$', auth_views.logout_then_login, name = 'logout_then_login'),
	url(r'^password-change/$', auth_views.PasswordChangeView.as_view(), name = 'password_change'),
	url(r'^password-change/done/$', auth_views.PasswordChangeDoneView.as_view(), name = 'password_change_done'),
	url(r'^password-reset/$', auth_views.PasswordResetView.as_view(), name = 'password_reset'),
	url(r'^password-reset/done/$', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
	url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
	url(r'^password-reset/complete/$', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),

	url(r'^$', account_views.dashboard, name = 'dashboard'),
	url(r'^register/$', account_views.register, name = 'register'),
	url(r'^edit/$', account_views.edit, name = 'edit'),
	url(r'^users/$', account_views.user_list, name = 'user_list'),
	url(r'^users/follow/$', account_views.user_follow, name = 'user_follow'),
	url(r'^users/(?P<username>[-\w]+)/$', account_views.user_detail, name = 'user_detail'),
]
