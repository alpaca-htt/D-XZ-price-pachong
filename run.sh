# 执行Django数据库迁移
/envs/baojia/bin/python3 manage.py makemigrations
/envs/baojia/bin/python3 manage.py migrate


/envs/baojia/bin/uwsgi --ini ./uwsgi.ini &  >/dev/null
nginx -c /etc/nginx/mybaojia.conf -g 'daemon off;'