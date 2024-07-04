from datetime import datetime, timedelta
from pathlib import Path
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)


DOC_MD = """
This is to test kubernetes operator with celery executor
"""

DAG_ID = Path(__file__).stem

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime.utcnow(),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id=DAG_ID,
    default_args=default_args,
    schedule=None,
    doc_md=DOC_MD,
) as dag:
    KubernetesPodOperator(
        task_id="k8s_task",
        image="alpine:latest",
        cmds=[
            "echo",
            "this is k8s operator",
        ],
    )
