FROM mysql:5.7

WORKDIR /app

EXPOSE 3306
ENV MYSQL_ROOT_PASSWORD dumbPassword
ENV MYSQL_USER testUser
ENV MYSQL_PASSWORD testPass
ENV MYSQL_DATABASE testDb

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Copy SQL Fixture
COPY ./start.sh ./start.sh
COPY ./dbInit.sql ./dbInit.sql

#ENTRYPOINT ["./start.sh"]
#CMD [""]
