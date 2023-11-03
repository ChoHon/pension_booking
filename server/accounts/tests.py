from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

from config.testcases import test_user

# 회원 가입 테스트
class SignupAPITest(APITestCase):
    User = get_user_model()

    def setUp(self):
        self.signup_url = reverse("accounts-signup")
        self.client = APIClient()

    def tearDown(self):
        self.signup_url = None
        self.client = None

        self.User.objects.all().delete()

    # 회원 가입 성공
    def test_signup_success(self):

        response = self.client.post(self.signup_url, data=test_user, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # 회원 가입 실패 - 이미 등록된 이메일
    def test_signup_fail_already_registed_email(self):
        self.client.post(self.signup_url, data=test_user, format="json")
        response = self.client.post(self.signup_url, data=test_user, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# 로그인 테스트
class LoginAPITest(APITestCase):
    User = get_user_model()

    def setUp(self):
        self.login_url = reverse("accounts-login")

        self.user = self.User.objects.create(
            email=test_user["email"],
            password=make_password(test_user["password"])
        )
        
        self.client = APIClient()

    def tearDown(self):
        self.login_url = None
        self.user = None
        self.client = None

        self.User.objects.all().delete()
        OutstandingToken.objects.all().delete()

    # 로그인 성공
    def test_login_success(self):
        response = self.client.post(self.login_url, test_user, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.content.decode("utf-8"))
        self.assertTrue("refresh" in response.content.decode("utf-8"))

    # 로그인 실패 - 잘못된 비밀번호
    def test_login_fail_wrong_password(self):
        body = {"email": test_user["email"], "password": test_user["password"] + "abc"}

        response = self.client.post(self.login_url, data=body, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # 로그인 실패 - 등록되지 않은 이메일
    def test_login_fail_not_registed_email(self):
        body = {"email": "test2@test.com", "password": test_user["password"]}

        response = self.client.post(self.login_url, data=body, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# 로그아웃 테스트
class LogoutAPITest(APITestCase):
    User = get_user_model()

    def setUp(self):
        self.logout_url = reverse("accounts-logout")

        self.user = self.User.objects.create(
            email=test_user["email"],
            password=make_password(test_user["password"])
        )

        self.token = TokenObtainPairSerializer.get_token(self.user)
        self.refresh_token = str(self.token)
        self.access_token = str(self.token.access_token)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)

    def tearDown(self):
        self.logout_url = None
        self.user = None
        self.token = None
        self.refresh_token = None
        self.access_token = None
        self.client = None

        self.User.objects.all().delete()
        OutstandingToken.objects.all().delete()
        BlacklistedToken.objects.all().delete()

    # 로그아웃 성공
    def test_logout_success(self):
        body = {"refresh": self.refresh_token}

        response = self.client.post(self.logout_url, data=body, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # 로그아웃 실패 - 잘못된 Access 토큰
    def test_logout_fail_invalidated_access_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token + 'abc')
        body = {"refresh": self.refresh_token}

        response = self.client.post(self.logout_url, data=body, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # 로그아웃 실패 - 잘못된 Refresh 토큰
    def test_logout_fail_invalidated_refresh_token(self):
        body = {"refresh": self.refresh_token + "abc"}

        response = self.client.post(self.logout_url, data=body, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

# 토큰 재발급 테스트
class TokenRefreshTest(APITestCase):
    User = get_user_model()

    def setUp(self):
        self.refresh_url = reverse("accounts-refresh")

        self.user = self.User.objects.create(
            email=test_user["email"],
            password=make_password(test_user["password"])
        )

        self.token = TokenObtainPairSerializer.get_token(self.user)
        self.refresh_token = str(self.token)
        self.access_token = str(self.token.access_token)
        
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)

    def tearDown(self):
        self.refresh_url = None
        self.user = None
        self.token = None
        self.refresh_token = None
        self.access_token = None
        self.client = None

        self.User.objects.all().delete()
        OutstandingToken.objects.all().delete()

    # 토큰 재발급 성공
    def test_refresh_success(self):
        body = {"refresh": self.refresh_token}

        response = self.client.post(self.refresh_url, data=body, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.content.decode("utf-8"))

    # 토큰 재발급 실패 - 잘못된 Refresh 토큰
    def test_refresh_fail_invalidated_refresh_token(self):
        body = {"refresh": self.refresh_token + "abc"}

        response = self.client.post(self.refresh_url, data=body, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)