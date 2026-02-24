from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from web.models import UserProfile
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get('username').strip()
            password = request.data.get('password').strip()
            if not username or not password:
                return Response({'result': '用户名和密码不能为空'})
            
            user = authenticate(username=username, password=password)
            if user is not None: #用户名密码正确
                user_profile = UserProfile.objects.get(username=username)
                refresh = RefreshToken.for_user(user)
                response = Response({
                    'result': 'success',
                    'access': str(refresh.access_token),
                    'user_id': user.id,    
                    'username': user.username,
                    'photo': user_profile.photo.url,
                    'profile': user_profile.profile,
                })
                
                response.set_cookie(
                    key='refresh_token', 
                    value=str(refresh), 
                    httponly=True,
                    samesite='Lax',
                    secure=True,  # 在生产环境中使用 HTTPS 时设置为 True
                    max_age= 86400 * 7,  # 刷新令牌的过期时间，例如 7 天
                )
                return response
            return Response({'result': '用户名或密码错误'})
                
        except:
            return Response({'result': '系统异常，请稍后再试'})
            
        
        