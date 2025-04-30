FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*

COPY html /usr/share/nginx/html
COPY css /usr/share/nginx/html/css
COPY images /usr/share/nginx/html/images

EXPOSE 80
