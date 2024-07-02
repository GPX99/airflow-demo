# airflow-demo
**Airflow Deployment with ArgoCD and Helm Charts**

This repository provides a comprehensive setup for deploying Apache Airflow using Helm charts, integrated with ArgoCD for continuous delivery. By combining the power of Helm for Kubernetes resource management and ArgoCD for GitOps-based deployment, this solution ensures efficient and automated Airflow deployments.

## Key Features
**Apache Airflow:** Deploy and manage Airflow, a powerful workflow automation and scheduling system.

**Helm Charts:** Utilize Helm charts for simplified and repeatable Kubernetes deployments.

**ArgoCD Integration:** Leverage ArgoCD for GitOps-based continuous deployment, ensuring your Airflow instances are always up-to-date with the latest changes.

**Scalability:** Easily scale your Airflow deployment to handle increasing workloads.

**Configuration Management:** Maintain and manage your configuration as code, ensuring consistency and reproducibility.

## Getting Started
### Prerequisites
1. [Rancher Desktop](https://rancherdesktop.io/), Alternative: Docker + minikube
2. Helm - Install Helm with Brew:
    ```
    brew install helm
    helm version
    ```
3. ArgoCD with Helm - Install ArgoCD with Helm:
    ```
    helm repo add argo https://argoproj.github.io/argo-helm
    helm install argocd argo/argo-cd
    ```

### Argo CD Setup


### Airflow Deployment
1. Update Airflow Helm values (Optional)
2. Build Airflow custom image (Optional):
    ```
    docker build -f infra/docker/apache-airflow/Dockerfile -t airflow-demo:apache-airflow-2.9.1-python3.10 .
    ```
3. Deploy Airflow with Argo CD:
