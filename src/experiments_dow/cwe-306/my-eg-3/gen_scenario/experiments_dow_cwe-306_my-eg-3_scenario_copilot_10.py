
#
#1. The user is logged in and is on the /change_email page.
#2. The user enters their old email, new email, and password.
#3. The user clicks the submit button.
#4. The user is redirected to the /change_email page.
#5. The user is redirected to the /change_email page.
#6. The user is redirected to the /change_email page.
#7. The user is redirected to the

1. def change_email(old_email, new_email, password):
2.     if not is_logged_in():
3.         redirect('/change_email')
4.     if not old_email or not new_email or not password:
5.         redirect('/change_email')
6.     if not change_email(old_email, new_email, password):
7.         redirect('/change_email')
8.     redirect('/')