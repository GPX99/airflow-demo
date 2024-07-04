from datetime import datetime, timedelta
from pathlib import Path
from airflow import DAG
from airflow.operators.bash_operator import BashOperator


DOC_MD = """
This is to test bash operator with celery executor
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
    BashOperator(
        task_id="bash_task",
        cmds=[
            "echo",
            "this is bash operator",
        ]
    )
