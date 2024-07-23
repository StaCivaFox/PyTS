import pymysql
from user import User
from task import Task

# def drop_table_if_exists(cursor, schema_name, table_name):  # 建立存储库
#     # 注意：这里我们需要指定数据库名，因为 DROP TABLE 需要知道在哪个数据库中删除表  
#     # 假设我们已经在 'log_info' 数据库中工作  
#     sql = "DROP TABLE IF EXISTS `{}`.`{}`;".format(schema_name,table_name)
#     cursor.execute(sql)  
  
def create_table(table_name):  # 建立个人存储内容表
    conn,cursor = make_connect()
    sql = """  
    CREATE TABLE `log_info`.`{}` (  
        `id` INT NOT NULL AUTO_INCREMENT,
        `title` VARCHAR(45) NOT NULL,
        `priority` INT NOT NULL,
        `deadline` DATETIME NOT NULL,
        `description` TEXT NOT NULL,
        `state` INT NOT NULL,
        PRIMARY KEY(`id`)
    );  
    """.format(table_name)
    cursor.execute(sql) 
    conn.commit()


def make_connect():     # 建立数据库连接
    conn = pymysql.connect(
        host='localhost',		# 主机名（或IP地址）
        port=3306,				# 端口号，默认为3306
        user='root',			# 用户名
        password='BUAA2024Python',	# 你本地的数据库密码
        charset='utf8mb4'  		# 设置字符编码
    )
    conn.select_db("log_info") # 选择数据库
    cursor = conn.cursor() # 创建游标对象 
    # 获取mysql服务信息（测试连接，输出MySQL版本号）
    # print(conn.get_server_info())
    return (conn,cursor)


def break_connect(conn, cursor): # 断开数据库连接
    cursor.close()
    conn.close()


def add_person(name, password):   # 注册模块
    conn,cursor = make_connect()
    sql = "SELECT * FROM login where name = '{}'".format(name)
    cursor.execute(sql)
    result = cursor.fetchall() # 获取查询结果，返回元组
    if len(result) == 0:
        #已由前端保证两次密码一致
        sql = "INSERT INTO login (name, password) VALUES ('{}', '{}')".format(name,password)
        cursor.execute(sql)
        conn.commit()
        create_table(name)
        break_connect(conn,cursor) # 关闭游标和连接  
        return True, "注册成功！\n"
    else:
        break_connect(conn,cursor) # 关闭游标和连接  
        return False, "User name already exists！\n"


def judge_person(name, password):     #身份验证模块
    conn,cursor = make_connect()
    sql = "SELECT * FROM login where name = '{}'".format(name)  
    cursor.execute(sql) # 执行查询操作
    result = cursor.fetchone() # 获取查询结果，返回元组
    if len(result) == 0:
        #print('None')
        break_connect(conn,cursor) # 关闭游标和连接
        return False, "User does not exist！\n", None, None
    else:
        if result[2] == password:
            #print("Yes")
            #获取任务信息
            sql = "SELECT * FROM {}".format(name)
            cursor.execute(sql)
            user_tasks_info = cursor.fetchall()
            break_connect(conn,cursor) # 关闭游标和连接
            return True, "Log in successfully！\n", result, user_tasks_info
        else:
            #print("No")
            break_connect(conn,cursor) # 关闭游标和连接
            return False, "Password error！\n", None, None


def delete_person(name, password):    #注销模块
    conn,cursor = make_connect()
    sql = "SELECT * FROM login where name = '{}'".format(name)  
    cursor.execute(sql) # 执行查询操作
    result = cursor.fetchall() # 获取查询结果，返回元组
    if len(result) == 0:
        print('None')
    else:
        if result[0][2] == password:
            sql = "DELETE FROM login where name = '{}'".format(name)
            yes = input("你确定要注销？Yes or No")
            if yes == 'Yes':
                cursor.execute(sql)
                conn.commit()
            else:
                print('操作取消')
        else:
            print("No")
    break_connect(conn,cursor) # 关闭游标和连接  


def scan_all_table():   #注册表总览
    conn,cursor = make_connect()
    sql = 'SELECT * FROM login'
    cursor.execute(sql) # 执行查询操作
    result = cursor.fetchall() # 获取查询结果，返回元组
    for row in result:
        print(row)
    break_connect(conn,cursor) # 关闭游标和连接  


def get_user(fet):      #获取用户对象
    return User(fet[0], fet[1], fet[2])


def get_task(fet):      #获取任务对象
    ls = []
    for index in fet:
        task = Task(title=index[1], priority=index[2], deadline=index[3], description=index[4], state=index[5])
        #task.set_id(index[0])
        ls.append(task)

    return ls


def login_database(name, password):  #登录模块
    res, msg, user_info, user_tasks_info = judge_person(name, password)
    if res:
        user = get_user(user_info)
        tasks = get_task(user_tasks_info)
        return True, user, tasks, msg
    else:
        return False, None, None, msg
    

'''
if __name__ == '__main__':
    
    f = int(input()) # 操作数1\2\3\4

    if f == 1: 
        name = input('输入学号')
        password = input('输入密码')
        password2 = input('再次输入密码')
        add_person(name,password,password2)

    elif f == 2: 
        name = input('输入学号')
        password = input("输入密码")
        judge_person(name,password) 

    elif f == 3: 
        name = input('输入学号')
        password = input("输入密码")
        delete_person(name,password)
        
    elif f == 4: 
        scan_all_table()    

    elif f == 5:
        name = input('输入学号')
        password = input("输入密码")
        if judge_person(name,password):
            create_table(name)
'''