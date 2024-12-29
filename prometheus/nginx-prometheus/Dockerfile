FROM nginx:1.24.0
USER root

# for applying password to prometheus
COPY default.conf /etc/nginx/conf.d/default.conf
COPY .htpasswd /etc/nginx/.htpasswd

USER nginx