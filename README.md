git clone https://github.com/walkiop/compose.git

cd compose

docker-compose up

docker exec -it 65f bash

mysql -uroot -p

use fibdb



#####
git clone https://github.com/josecastillolema/fiap/aso/compose.git

cd mongoDB-compose

git pull --atualiza repositorio

docker exec -it mongodb-container bash

#subir imagem para dockerHub
docker login
docker images
docker tag compose_mysql walkio/compose_mysql
docker tag compose_api walkio/compose_mysql

docker push walkio/compose_mysql
docker push walkio/compose_api
