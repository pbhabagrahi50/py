FROM ubuntu:lastest
RUN apt-get update -y
RUN apt-get install apache2 -y
RUN apt-get install unzip -y
ADD https://www.free-css.com/assets/files/free-css-templates/download/page290/wave-cafe.zip /var/www/html
WORKDIR /var/www/html
RUN unzip wave-cafe.zip
RUN cp -rvf wave-cafe/* .
RUN rm -rm wafe-cafe wafe-cafe.zip
ENTRYPOINT ["/usr/sbin/apache2ctl"]
CMD ["-D","FOREGROUND"]
EXPOSE 80