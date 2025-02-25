from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from airflow.decorators import task

with DAG(
    dag_id="dags_python_template",
    schedule="30 9 * * *",
    start_date=False,
    catchup=False
) as dag:

    def python_function(start_date, end_date, **kwargs):
        print(start_date)
        print(end_date)

    print_t1 = PythonOperator(
        task_id="python_t1",
        python_callable=python_function,
        op_kwargs={'start_date': '{{date_interval_start | ds}}', 'end_date': '{{date_interval_end | ds}}'}
    )

    @task(task_id='python_t2'):
    def python_function2(**kwargs):
        print(kwargs)
        print
