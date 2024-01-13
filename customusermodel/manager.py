from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class customusermanager(BaseUserManager):

    def cheakinputs(self,email,firstname,lastname,password,DOB,**other_fields):
        if (email!=None and firstname!=None and lastname!=None and password!=None and DOB!=None):
            email=self.normalize_email(email)
            try :
               validate_email(email)
               return True
            except ValidationError:
                raise ValueError("Invalid Email")
        


        else:
            raise ValueError("Invalid Inputs No Value can be None")
        
    def create_user(self,email,firstname,lastname,password,DOB,**other_fields):
         x= self.cheakinputs(email,firstname,lastname,password,DOB,**other_fields)
         if (x):
             user=self.model(
                 firstname=firstname,
                 lastname=lastname,
                 email=email,
                 DOB=DOB,
                 **other_fields
             )
             user.set_password(password)
             other_fields.setdefault("is_superuser",False)
             other_fields.setdefault("is_active",False)
             other_fields.setdefault("is_staff",False)
             user.save(using=self._db)
             return user
         else:
             raise ValueError("Enter Valid Details")
         
    def create_superuser(self,email,firstname,lastname,password,DOB,**other_fields):
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_active',True)
        x= self.cheakinputs(email,firstname,lastname,password,DOB,**other_fields)
        if (x):
            user=self.model(
                firstname=firstname,
                lastname=lastname,
                email=email,
                DOB=DOB,
                **other_fields

            )
            user.set_password(password)
            
            user.save(using=self._db)
            return user
        else:
            raise ValueError("Enter Valid Credentials For Super User")
            