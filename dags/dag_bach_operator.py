from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    # dag_id는 배치명, 파일명과 일치시켜야 좋다.
    dag_id="dag_bach_oprator",
    schedule="0 0 * * *",
    # UTC일 경우 9시간 늦게 수행
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    # 60분이상 돌았을 때 실패로 처리.
    # dagrun_timeout=datetime.timedelta(minutes=60),
    # tags=["example", "example2"],
    # 타스크들의 공통 파라미터.
    # params={"example_key": "example_value"},
) as dag:
    bash_t1 = BashOperator(
        # 객체명과 타스크아이디는 공통되야 찾기 쉽다.
        task_id="bash_t1",
        bash_command="echo whoami",
    )
    bash_t2 = BashOperator(
        # 객체명과 타스크아이디는 공통되야 찾기 쉽다.
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )
    #수행 순서 정해준다(bash_t1 다음에 bash-t2 수행한다.)
    bash_t1 >> bash_t2