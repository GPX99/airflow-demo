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
3. Serve the Argo CD locally with default url https://localhost:8081/
    ```
    kubectl port-forward svc/argocd-server -n argocd 8081:443
    ```
4. login with `admin` user and password from kube command 
    ```
    kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
    ```

***Notes:** to output the file with `--dry-run=client -o yaml>file_name.yml`*

### Airflow Deployment
1. (Optional) Update Airflow Helm values and verify the values:
    ```
    cd charts
    helm template demo-airflow . -f demo-values.yaml --namespace airflow --debug > rendered.yaml
    ```
2. (Optional) Build Airflow custom image:
    ```
    docker build -f infra/docker/apache-airflow/Dockerfile -t airflow-demo:apache-airflow-2.9.1-python3.10 .
    ```
3. (Optional) External Secret Set Up:
    ```
    argocd login 127.0.0.1:8081

    argocd app create external-secrets \
    --repo https://charts.external-secrets.io \
    --helm-chart external-secrets \
    --revision 0.9.19 \
    --dest-namespace external-secrets \
    --sync-option CreateNamespace=true \
    --dest-server https://kubernetes.default.svc
    ```
    
    What you need:
    1. new fernet key (defined by you)
    2. new webserver key (defined by you)
    3. new PostgreSQL connection (local or cloud)
    4. new redis password (defined by you)
    5. broker URL redis://:$REDIS_PASSWORD@k8s_redis_deployment_name:6379/0
    
    ***Tips:** Use [this](https://fernetkeygen.com/) to generate the keys and passwords.*
    
    Kubernetes Secret Store Set Up:
    ```
    echo -n "new_fernet_key" > temp/fernet-key
    echo -n "new_webserver_key" > temp/webserver-secret-key
    echo -n "new_postgres_connection" > temp/metadata-connection-url
    echo -n "new_redis_password" > temp/redis-password
    echo -n "redis://:$REDIS_PASSWORD@k8s_redis_deployment_name:6379/0" > temp/broker-connection-url

    kubectl create namespace airflow
    kubectl create secret generic demo-airflow-secret -n airflow --from-file=FERNET_KEY=temp/fernet-key --from-file=METADATA_CONNECTION_URL=temp/metadata-connection-url --from-file=REDIS_PASSWORD=temp/redis-password --from-file=BROKER_CONNECTION_URL=temp/broker-connection-url --from-file=WEBSERVER_SECRET_KEY=temp/webserver-secret-key
    ```

4. Deploy Airflow Helm with Argo CD and serve the Airflow webserver with default url https://127.0.0.1:8080/
    ```
    cd infra/argocd
    argocd app create demo-airflow --file demo-airflow.yaml
    kubectl port-forward svc/demo-airflow-webserver 8080:8080 --namespace airflow
    ```

5. Clean up
    ```
    argocd app delete demo-airflow --cascade
    ```

## References
- [Apache Airflow](https://airflow.apache.org/)
- [Apache Airflow Helm Chart](https://airflow.apache.org/docs/helm-chart/stable/index.html)
- [Helm Cheat Sheet](https://helm.sh/docs/intro/cheatsheet/)
- [ArgoCD Deployment](https://argo-cd.readthedocs.io/en/stable/getting_started/)
- [Kubectl Commands](https://jamesdefabia.github.io/docs/user-guide/kubectl/kubectl/)
- [Docker Commands](https://docs.docker.com/reference/cli/docker/)
