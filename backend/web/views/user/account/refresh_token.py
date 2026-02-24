from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView

class RefreshTokenView(APIView):
    def post(self, request):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            if not refresh_token:
                return Response({
                    'result': 'refresh token不存在'
                }, status=401)
            refresh = RefreshToken(refresh_token)
            if settings.SIMPLE_JWT['ROTATE_REFRESH_TOKENS']:
                refresh.set_jti()
                response = Response({
                    'result': 'success',
                    'access': str(refresh.access_token),
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
            return Response({
                'result': 'success',
                'access': str(refresh.access_token),
            })
        except:
            return Response({
                'result': 'refresh_token 过期了',
            }, status=401)