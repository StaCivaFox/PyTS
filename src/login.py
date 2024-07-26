import pymysql
from datetime import datetime
from user import User
from task import Task 

#################################### 数据库操作 ##############################################
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
##############################################################################################



#################################### 登录操作 #################################################

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
        return False, "User name already exists!\n"

def judge_person(name, password):     #身份验证模块
    conn,cursor = make_connect()
    sql = "SELECT * FROM login where name = '{}'".format(name)  
    cursor.execute(sql) # 执行查询操作
    result = cursor.fetchone() # 获取查询结果，返回元组
    if result == None:
        #print('None')
        break_connect(conn,cursor) # 关闭游标和连接
        return False, "User does not exist!\n", None, None
    else:
        if result[2] == password:
            #print("Yes")
            #获取任务信息
            sql = "SELECT * FROM {}".format(name)
            cursor.execute(sql)
            user_tasks_info = cursor.fetchall()
            break_connect(conn,cursor) # 关闭游标和连接
            return True, "Log in successfully!\n", result, user_tasks_info
        else:
            #print("No")
            break_connect(conn,cursor) # 关闭游标和连接
            return False, "Password error!\n", None, None


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


def scan_login_table():   #注册表总览
    conn,cursor = make_connect()
    sql = 'SELECT * FROM login'
    cursor.execute(sql) # 执行查询操作
    result = cursor.fetchall() # 获取查询结果，返回元组
    for row in result:
        print(row)
    break_connect(conn,cursor) # 关闭游标和连接  
##################################################################################################



#################################### 计划的增删改查以及排序 ########################################
def add_schedule(name,task):
    conn,cursor = make_connect()
    sql = "SELECT * FROM {} where title = '{}'".format(name,task.title)
    cursor.execute(sql)
    result = cursor.fetchall() # 获取查询结果，返回元组
    if len(result) == 0:
        sql = "INSERT INTO `log_info`.`{}` (`title`, `priority`, `deadline`, `description`, `state`) VALUES ('{}', '{}', '{}', '{}', '{}')".format(name,task.title,task.priority,task.deadline,task.description,task.state)
        cursor.execute(sql)
        conn.commit()
        break_connect(conn,cursor) # 关闭游标和连接  
        return True, "添加任务成功！\n"
    else:
        break_connect(conn,cursor) # 关闭游标和连接  
        return False, "任务已存在！\n"


def edit_schedule_priority(name,task,priority):
    conn,cursor = make_connect()
    sql = "SELECT * FROM {} where title = '{}'".format(name,task.title)
    cursor.execute(sql)
    result = cursor.fetchall() # 获取查询结果，返回元组
    if len(result) != 0:
        sql = "UPDATE {} SET priority = {} WHERE title = '{}'".format(name,priority,task.title)
        cursor.execute(sql)
        conn.commit()
        break_connect(conn,cursor) # 关闭游标和连接  
        return True, "修改成功！\n"
    else:
        break_connect(conn,cursor) # 关闭游标和连接  
        return False, "无此任务！\n"


def edit_schedule_deadline(name,task,deadline):
    conn,cursor = make_connect()
    sql = "SELECT * FROM {} where title = '{}'".format(name,task.title)
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchall() # 获取查询结果，返回元组
    if len(result) != 0:
        sql = "UPDATE {} SET deadline = '{}' WHERE title = '{}'".format(name,deadline,task.title)
        cursor.execute(sql)
        conn.commit()
        break_connect(conn,cursor) # 关闭游标和连接  
        return True, "修改成功！\n"
    else:
        break_connect(conn,cursor) # 关闭游标和连接  
        return False, "无此任务！\n"


def edit_schedule_description(name,task,description):
    conn,cursor = make_connect()
    sql = "SELECT * FROM {} where title = '{}'".format(name,task.title)
    cursor.execute(sql)
    result = cursor.fetchall() # 获取查询结果，返回元组
    if len(result) != 0:
        sql = "UPDATE {} SET description = '{}' WHERE title = '{}'".format(name,description,task.title)
        cursor.execute(sql)
        conn.commit()
        break_connect(conn,cursor) # 关闭游标和连接  
        return True, "修改成功！\n"
    else:
        break_connect(conn,cursor) # 关闭游标和连接  
        return False, "无此任务！\n"


def edit_schedule_state(name,task,state):
    conn,cursor = make_connect()
    sql = "SELECT * FROM {} where title = '{}'".format(name,task.title)
    cursor.execute(sql)
    result = cursor.fetchall() # 获取查询结果，返回元组
    if len(result) != 0:
        sql = "UPDATE {} SET state = {} WHERE title = '{}'".format(name,state,task.title)
        cursor.execute(sql)
        conn.commit()
        break_connect(conn,cursor) # 关闭游标和连接  
        return True, "修改成功！\n"
    else:
        break_connect(conn,cursor) # 关闭游标和连接  
        return False, "无此任务！\n"


def scan_schedule(name):
    conn,cursor = make_connect()
    sql = 'SELECT * FROM {}'.format(name)
    cursor.execute(sql) # 执行查询操作
    result = cursor.fetchall() # 获取查询结果，返回元组
    #for row in result:
    #    print(row)
    break_connect(conn,cursor) # 关闭游标和连接
    return result


def search_schedule_by_date(name,datetime): # 查询该日期之后截止的任务
    conn,cursor = make_connect()
    sql = "SELECT * FROM `{}` WHERE TIMESTAMPDIFF(MINUTE, CAST('{}' AS DATETIME), deadline) >= 0".format(name,datetime) 
    cursor.execute(sql) # 执行查询操作
    result = cursor.fetchall() # 获取查询结果，返回元组
    # from datetime import datetime    
    # ans = list(result)
    # ans_lists = [list(tup) for tup in ans]
    # for one in ans_lists:
    #     custom_tuple = (one[3].year, one[3].month, one[3].day, one[3].hour, one[3].minute) 
    #     one[3] = custom_tuple
    # ans_tups = [tuple(lists) for lists in ans_lists]
    # return tuple(ans_tups)
    ans = []
    for one in result:
        task = Task(one[1], one[2], one[3], one[4], one[5])
        ans.append(task)
    break_connect(conn,cursor) # 关闭游标和连接
    return tuple(ans)
    

def sort_schedules(tasks): # 任务自动排序功能函数
    ans = []
    task_lists = list(tasks)
    task_lists.sort(reverse=False,key=lambda task: (task.deadline,task.priority)) # 升序排列
    return tuple(task_lists)


def sort_schedules_by_deadline(tasks): # 任务自动排序功能函数
    ans = []
    task_lists = list(tasks)
    task_lists.sort(reverse=False,key=lambda task: task.deadline) # 升序排列
    return tuple(task_lists)


def sort_schedules_by_priority(tasks): # 任务自动排序功能函数
    ans = []
    task_lists = list(tasks)
    task_lists.sort(reverse=False,key=lambda task: task.priority) # 升序排列
    return tuple(task_lists)


def is_overdue(task,now): # 任务是否超时函数: 如果当前时刻超过task截止日期了返回True,否则返回False
    return ((task.deadline - now).total_seconds() < 0)


def search_schedule_by_title(name,title): # 根据标题查任务(may be useless)
    conn,cursor = make_connect()
    sql = "SELECT * FROM {} WHERE title = '{}'".format(name,title)
    cursor.execute(sql) # 执行查询操作
    result = cursor.fetchall() # 获取查询结果，返回元组
    # from datetime import datetime  
    # custom_tuple = (result[0][3].year, result[0][3].month, result[0][3].day, result[0][3].hour, result[0][3].minute) 
    # ans = list(result[0])
    # ans[3] = custom_tuple
    # return tuple(ans)
    task = Task(result[0][1], result[0][2], result[0][3], result[0][4], result[0][5])
    break_connect(conn,cursor) # 关闭游标和连接
    return task


def delete_schedule(name,task): # 删掉任务
    conn,cursor = make_connect()
    sql = "SELECT * FROM {} where title = '{}'".format(name,task.title)  
    cursor.execute(sql) # 执行查询操作
    result = cursor.fetchall() # 获取查询结果，返回元组
    if len(result) == 0:
        print('None')
    else:
        sql = "DELETE FROM {} where title = '{}'".format(name,task.title)
        yes = input("你确定要删除任务？Yes or No")
        if yes == 'Yes':
            cursor.execute(sql)
            conn.commit()
        else:
            print('操作取消')
    break_connect(conn,cursor) # 关闭游标和连接

##############################################################################################



#################################### 前后端接口 #################################################

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

####################################################################################################



###################################### 一些本地才有用的函数 ##########################################

def create_table(table_name):  # 建立个人存储内容表
    conn,cursor = make_connect()
    sql = """  
    CREATE TABLE `log_info`.`{}` (  
        `id` INT NOT NULL AUTO_INCREMENT,
        `title` VARCHAR(45) NOT NULL,
        `priority` INT NOT NULL,
        `deadline` DATETIME NOT NULL,
        `description` TEXT NOT NULL,
        `state` TEXT NOT NULL,
        PRIMARY KEY(`id`)
    );  
    """.format(table_name)
    cursor.execute(sql) 
    conn.commit()

################################################################################################
    


######################################## 本地验证 ###############################################
if __name__ == '__main__':
    
    f = int(input()) # 操作数1\2\3\4

    if f == 1: 
        name = input('输入学号')
        password = input('输入密码')
        password2 = input('再次输入密码')
        add_person(name,password)

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
    elif f == 6:
        name = input('输入名字')
        title = input('输入标题')
        priority = input('输入优先级')
        year,month,day,hour,minute = input('输入年 月 日 小时 分钟').split(' ')
        deadline = '{}-{}-{} {}:{}:00'.format(year,month,day,hour,minute)
        description = input('输入描述')
        state = input('输入状态')
        task0 = Task(title, priority, deadline, description, state)
        add_schedule(name,task0)

    elif f == 7:
        name = input('输入名字')
        title = input('输入标题')
        delete_schedule(name,title)
    
    elif f == 8:
        name = input('输入名字')
        title = input('输入标题')
        priority = input('输入优先级')
        year,month,day,hour,minute = input('输入年 月 日 小时 分钟').split(' ')
        deadline = '{}-{}-{} {}:{}:00'.format(year,month,day,hour,minute)
        description = input('输入描述')
        state = input('输入状态')
        task0 = Task(title, priority, deadline, description, state)
        # edit_schedule_priority(name,task0,priority)
        edit_schedule_deadline(name,task0,deadline)
        # edit_schedule_description(name,task0,description)
        # edit_schedule_state(name,task0,state)

    elif f == 9:
        name = input('输入名字')
        scan_schedule(name)

    elif f == 10:
        name = input('输入名字')
        title = input('输入标题')
        search_schedule(name,title)

    elif f == 11:
        name = input('输入名字')
        year,month,day,hour,minute = input('输入年 月 日 小时 分钟').split(' ')
        date = '{}-{}-{} {}:{}:00'.format(year,month,day,hour,minute)
        print(search_schedule_by_date(name,date))

    elif f == 12:
        # title = 'test'
        # priority = '1'
        # year,month,day,hour,minute = input('输入年 月 日 小时 分钟').split(' ')
        # deadline = '{}-{}-{} {}:{}:00'.format(year,month,day,hour,minute)
        # description = '123'
        # state = '123'
        task0 = search_schedule_by_title('KJH','123')

        year,month,day,hour,minute = input('输入年 月 日 小时 分钟').split(' ')
        now = '{}-{}-{} {}:{}:00'.format(year,month,day,hour,minute)
        now = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
        print(is_overdue(task0,now))

    elif f == 13:
        print('before:')
        for i in search_schedule_by_date('KJH','1-12-12 0:0:0'):
            print(i.title)

        print('after:')
        for i in sort_schedules(search_schedule_by_date('KJH','1-12-12 0:0:0')):
            print(i.title)
        