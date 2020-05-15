from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from pets.models import Pet, Appointment
from .forms import *

# Create your tests here.
class PetsTest(TestCase):
    def test_pets(self):
        user = User.objects.create_user(username='usertest', password='password')
        self.client.login(username='usertest', password='password')

        Pet.objects.create(pet_name='Kuma', species='Dog', breed='Pomeranian', weight_in_pounds=7, Owner=user)

        response = self.client.get('/pets/')
        
        self.assertEqual(response.status_code, 200)
        get_response = self.client.get(reverse('pets'))
        
        self.assertContains(get_response, 'usertest')

class PetsDetailTest(TestCase):
    def test_pets(self):
        user = User.objects.create_user(username='usertest', password='password')
        self.client.login(username='usertest', password='password')

        Pet.objects.create(pet_name='Kuma', species='Dog', breed='Pomeranian', weight_in_pounds=7, Owner=user)
        pet = Pet.objects.get(pet_name='Kuma')

        Appointment.objects.create(date_of_appointment='2020-05-20', duration_minutes=60, special_instructions='Wash', pet=pet)

        response = self.client.get('/pet/1')
        
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response, 'Dog')

class PetCreationTest(TestCase):
    def test_creation(self):
        user = User.objects.create_user(username='usertest', password='password')
        self.client.login(username='usertest', password='password')
        
        response = self.client.post('/pet/create/', 
            {
                'pet_name': 'Mater', 
                'species': 'Flying Squirrel',
                'breed': 'N/A',
                'weight_in_pounds': 2,
                'Owner': user,
            })
        
        self.assertEqual(response.status_code, 302)
        
        new_pet = Pet.objects.filter(pet_name='Mater')
        self.assertTrue(new_pet.exists())

class PetCreationTest(TestCase):
    def test_creation(self):
        user = User.objects.create_user(username='usertest', password='password')
        self.client.login(username='usertest', password='password')
        
        pet = Pet.objects.create(pet_name='Kuma', species='Dog', breed='Pomeranian', weight_in_pounds=7, Owner=user)

        response = self.client.post('/appointment/create/', 
            {
                'date_of_appointment': '2020-05-16', 
                'duration_minutes': 30,
                'special_instructions': 'None',
                'pet': pet,
            })
        
        self.assertEqual(response.status_code, 302)
        
        new_appointment = Appointment.objects.filter(date_of_appointment='2020-05-16')
        self.assertTrue(new_appointment.exists())