# Build the docker file 
docker build -t exp:v1 -f ./Dockerfile .
# Mount our volume to models directory (where train data is stored)
docker run -d  -p 5000:5000 -v ./models:/digits/models exp:v1 
