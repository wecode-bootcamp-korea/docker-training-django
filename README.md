# docker_train 

- my_settings.py 파일을 생성해서 database 접속 정보를 입력해주세요.
```python
  ex)
  DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DATABASE 명',
        'USER': 'DB접속 계정명',
        'PASSWORD': 'DB접속용 비밀번호',
        'HOST': '실제 DB 주소',
        'PORT': '포트번호',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
    }
  }
```
- secret key도 작성해주세요.
```python
  ex)
  SECRET = 'YOU_HAVE_TO_GENERATE_RANDOM_SECRET_KEY'
```
- setting_up.sh를 실행해 주세요.
```bash
source setting_up.sh
```
