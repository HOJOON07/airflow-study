def get_sftp():
    print("작업을 시작합니다.")


def regist(name, sex, *args):
    print(f'이름은 {name}이고 성별은 {sex}입니다.')
    print(args)

    # python_task = PythonOperator(
    #     task_id="python_task",
    #     python_callable=regist
    #     op_args=['hjkim', 'man']
    # )


def regist2(name, sex, *args):
    print(name)
    print(sex)
    print(args)


# python_task2 = PythonOperator(
#     task_id="python_task2",
#     python_callable=regist2,
#     op_args=['hojoon', 'man', "korea", "seoul"]
# )
