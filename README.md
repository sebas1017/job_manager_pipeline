docker build -t manager_local .
docker run -p 8220:8220 manager_local
http://localhost:8220/docs


ejecutar al nivel del dockerfile

heroku login
heroku container:login
heroku create nombre_app  #o el nombre que desee
heroku container:push web -a  nombre_app
heroku container:release web -a  nombre_app  #esto despliega


