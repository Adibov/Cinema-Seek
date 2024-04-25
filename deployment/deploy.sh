#!/bin/zsh

kubectl apply -f secrets.yaml
kubectl apply -f configmap.yaml
kubectl apply -f pvc.yaml
kubectl apply -f services.yaml
kubectl apply -f deployments.yaml
