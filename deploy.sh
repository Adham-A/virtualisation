kubectl apply -f my-quiz-namespace.yaml
kubectl apply -f my-quiz-ui-deployment.yaml
kubectl apply -f my-quiz-api-deployment.yaml
kubectl apply -f my-quiz-ui-service.yaml
kubectl apply -f my-quiz-api-service.yaml
kubectl apply -f my-quiz-ingress.yaml