from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from web.models import UserProfile
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get('username').strip()
            password = request.data.get('password').strip()
            if not username or not password:
                return Response({
                    'result': '用户名和密码不能为空'
                })
            
            if User.objects.filter(username=username).exists():
                return Response({
                    'result': '用户名已存在'
                })
            
            user = User.objects.create_user(username=username, password=password)
            user_profile = UserProfile.objects.create(user=user)
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
        
        except:
            return Response({
                'result': '系统异常，请稍后再试'
            })