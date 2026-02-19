from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Team, User, Workout, Activity, Leaderboard

class APISmokeTest(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Marvel", description="Team Marvel")
        self.user = User.objects.create(name="Tony Stark", email="tony@stark.com", team=self.team)
        self.workout = Workout.objects.create(name="Pushups", description="Upper body", difficulty="Easy")
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, duration=30, calories_burned=200)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=100, rank=1)

    def test_api_root(self):
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_list(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_teams_list(self):
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_workouts_list(self):
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activities_list(self):
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leaderboard_list(self):
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
