# Projet

```bash
docker build -t my-quiz-api ./quiz-api
docker build -t my-quiz-ui ./quiz-ui
docker container run -it --rm -p 3000:80 --name my-quiz-ui my-quiz-ui 
docker container run -it --rm -p 5000:5000 --name my-quiz-api my-quiz-api 
```

```bash
docker tag my-quiz-api adham999/my-quiz-api
docker push adham999/my-quiz-api

docker tag my-quiz-api adham999/my-quiz-ui
docker push adham999/my-quiz-ui
```

kubectl apply -f file.yaml
kubectl get pods -n quiz-app
