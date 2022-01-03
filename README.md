# docker_train 

- RDS mysql 서버에 접속합니다.
    ```shell
  $ mysql -h 'RDS Database Endpoint 주소' -u root -p
    ```

- 데이터베이스를 생성합니다.
    ```shell
  mysql> create database 'DATABASE 명' character set utf8mb4 collate utf8mb4_general_ci;
    ```

- my_settings 생성 후 DATABASES 의 정보를 본인의 RDS 데이터베이스에 맞게 수정합니다.
    ```python
  ex)
  DATABASES = {
      'default' : {
          'ENGINE'   : 'django.db.backends.mysql',
          'NAME'     : 'DATABASE 명',
          'USER'     : 'DB 접속 계정명',
          'PASSWORD' : 'DB 접속 비밀번호',
          'HOST'     : 'RDS Database Endpoint 주소',
          'PORT'     : 'DB PORT',
          'OPTIONS'  :  {
              'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'"
          },
      }
  }
    ```
- secret key도 작성해주세요.
    ```python
  ex)
  SECRET_KEY = 'YOU_HAVE_TO_GENERATE_RANDOM_SECRET_KEY'
    ```
- setting_up.sh를 실행해 주세요.
    ```bash
  source setting_up.sh
    ```
