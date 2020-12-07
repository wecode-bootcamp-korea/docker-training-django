import os
import django
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

os.chdir("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "docker_train.settings")
django.setup()

from basic.models import Basic

if Basic.objects.filter().exists():
    Basic.objects.all().delete()
Basic.objects.create(name='코딩의 기본은 공식 문서를 보자')
Basic.objects.create(name='도커의 기본도 공식 문서이다.')
Basic.objects.create(name='도커 공식 홈페이지 주소는 http://docker.com 이다')
Basic.objects.create(name='백엔드 화이팅!!')


