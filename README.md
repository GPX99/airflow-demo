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
3. ArgoCD - Install ArgoCD with Brew
    ```
    brew install argocd
    ```

### Argo CD Setup
1. Create a namespace
    ```
    kubectl create namespace argocd
    ```
2. Apply default stable version Argo CD
    ```
    kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
    ```
3. Serve the Argo CD locally with default url https://localhost:8080/
    ```
    kubectl port-forward svc/argocd-server -n argocd 8080:443
    ```
4. login with `admin` user and password from kube command 
    ```
    kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
    ```

***Notes:** to output the file with `--dry-run=client -o yaml>file_name.yml`*

### Airflow Deployment
1. Update Airflow Helm values (Optional)
2. Build Airflow custom image (Optional):
    ```
    docker build -f infra/docker/apache-airflow/Dockerfile -t airflow-demo:apache-airflow-2.9.1-python3.10 .
    ```
3. Deploy Airflow with Argo CD:

## References
- [Apache Airflow](https://airflow.apache.org/)
- [Apache Airflow Helm Chart](https://airflow.apache.org/docs/helm-chart/stable/index.html)
- [Helm Cheat Sheet](https://helm.sh/docs/intro/cheatsheet/)
- [ArgoCD Deployment](https://argo-cd.readthedocs.io/en/stable/getting_started/)
- [Kubectl Commands](https://jamesdefabia.github.io/docs/user-guide/kubectl/kubectl/)
- [Docker Commands](https://docs.docker.com/reference/cli/docker/)
