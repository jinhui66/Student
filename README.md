配置文件
### config.py
```
# 数据库的配置信息
HOSTNAME = ""
PORT = 3306
USERNAME = "root"
PASSWORD = ""
DATABASE = "StuDormitoryManager"
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

```
