# Projet

```bash
docker build -t my-quiz-api ./quiz-api
docker build -t my-quiz-ui ./quiz-ui
# docker container run --rm -p 3000:80 --name my-quiz-ui adham999/my-quiz-ui
# docker container run --rm -p 5000:5000 --name my-quiz-api adham999/my-quiz-api
```

```bash
docker tag my-quiz-api adham999/my-quiz-api
docker push adham999/my-quiz-api

docker tag my-quiz-ui adham999/my-quiz-ui
docker push adham999/my-quiz-ui
```

```bash

kubectl apply -f my-quiz-namespace.yaml
kubectl apply -f my-quiz-ui-deployment.yaml
kubectl apply -f my-quiz-api-deployment.yaml
kubectl apply -f my-quiz-ui-service.yaml
kubectl apply -f my-quiz-api-service.yaml
kubectl apply -f my-quiz-ingress.yaml
```

On utilise traefik

```bash
helm install traefik traefik/traefik
```

Serve :

```bash
minikube service
```
