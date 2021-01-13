from django.db import models



#validation, new class
class ShowManager(models.Manager):
    def validateShow(self,postData):
        errors = {}
        if len(postData['show_title']) < 2:
            errors['show_title'] = "Release date NEEDS more than 1 letter. dude"
        if len(postData['show_network']) < 2 :
            errors['show_network'] = "network NEEDS more than 1 letter. dude"
        # if len(postData["show_release_date"] == 0):
        #     errors['show_release_date'] = "Release date CANNOT be blank. dude"
        if len(postData["show_description"]) == 0:
            errors['show_description'] = "Description CANNOT be blank. dude"
        
        # if show exists in list       
        showExists = Show.objects.filter(title=postData['show_title'])
        if showExists:
            errors['title_existss'] = 'show already in DATABASE'

        return errors

class Show(models.Model):
    title = models.TextField(max_length=255)
    network = models.TextField(max_length=255)
    release_date = models.DateField(auto_now_add=False, auto_now=False)
    description = models.TextField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # objects = models.Manager()
    objects = ShowManager()