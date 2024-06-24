# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from apis.models import Teacher, Classroom, School,  Student

class APITestCase(TestCase):
    def setUp(self):
        # สร้างข้อมูลทดสอบ
        self.client = APIClient()
        self.client.defaults['HTTP_ACCEPT'] = 'application/json'
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.school = School.objects.create(name_school="Test School", short_name="TS", address="123 Test St")
        self.classroom1 = Classroom.objects.create(grade_class=1, room_class=1, school=self.school)
        self.classroom2 = Classroom.objects.create(grade_class=2, room_class=1, school=self.school)
        self.teacher = Teacher.objects.create(name_teacher="John", last_name="Doe", gender = 'Male')
        self.teacher.classroom.set([self.classroom1, self.classroom2])
        self.student = Student.objects.create(name_student="Jane", last_name="Doe", gender = 'Male', classroom=self.classroom1)

    def test_create_school(self):
        data = {"name_school": "New School", "short_name": "NS", "address": "456 New St"}
        response = self.client.post('/api/v1/schools/', data, format='json')
        print(response.status_code)
        if response.status_code != status.HTTP_201_CREATED:
            print(response.content)  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_school(self):
        response = self.client.get(f'/api/v1/schools/{self.school.id_school}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name_school'], "Test School")
    
    def test_search_school(self):
        response = self.client.get('/api/v1/schools/?search=test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name_school'], "Test School")
    
    def test_update_school(self):
        data = {"name_school": "Updated School", "short_name": "US", "address": "789 Updated St"}
        response = self.client.put(f'/api/v1/schools/{self.school.id_school}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name_school'], "Updated School")
    
    def test_delete_school(self):
        response = self.client.delete(f'/api/v1/schools/{self.school.id_school}/')
        print(response.status_code)
        print(response.content)  
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
