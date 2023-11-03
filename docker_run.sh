# Build the docker file 
docker build -t exp:v1 -f ./Dockerfile .
# Mount our volume to models directory (where train data is stored)
docker run -v /home/maverick/digits_dataset/MLOPScourse/models:/digits/models exp:v1