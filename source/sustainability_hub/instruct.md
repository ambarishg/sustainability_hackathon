az aks get-credentials --resource-group rgqdrant --name azqdrantcluster 

helm install <your desired installation name> ./qdrant-on-azure --create-namespace

helm install ambarish-qdrant ./qdrant-on-azure --create-namespace