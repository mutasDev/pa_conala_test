#Django get maximum value associated with field 'added' in model `AuthorizedEmail`


AuthorizedEmail.objects.all().aggregate(Max('added'))