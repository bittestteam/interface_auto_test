from publicMethod import *

sql1="select * from f_user where fid in (%s,%s)"
sql="update f_user set femail=%s where fid=%s"
publicMethod.operate_mysql(2,sql,("222",667600))

config = configparser.ConfigParser()
config.read("config.ini")
host = config['Mysql']['host']
port = int(config['Mysql']['port'])
user = config['Mysql']['user']
password = config['Mysql']['password']
database = config['Mysql']['database']
charset = config['Mysql']['charset']
conn = pymysql.connect(host=host, port=port, password=password, user=user, database=database,charset=charset)
curs = conn.cursor()
curs.execute(sql,(666666,667600))
result = curs.fetchall()
print("ok")
print(result)

