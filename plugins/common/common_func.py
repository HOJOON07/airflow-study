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


def regist2(name, sex, *args, **kwargs):
    print('이름 : ', name)
    print('성별 : ', sex),
    print(f'기타옵션들 : {args}')
    email = kwargs['email'] or None
    phone = kwargs["phone"] or None
    if email:
        print(email)
    if phone:
        print(phone)
