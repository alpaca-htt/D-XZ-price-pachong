/envs/baojia/bin/uwsgi --ini ./uwsgi.ini &  >/dev/null
nginx -c /etc/nginx/mybaojia.conf -g 'daemon off;'