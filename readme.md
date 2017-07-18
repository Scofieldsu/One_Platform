# <center>Smart-Tools</center>

- 安装依赖：pip install -r requirements.txt

- 本机调试运行：python run.py

- 运行后，localhost:5050  为登录页面

- linux上部署：

 > gunicorn -c gun.conf run:app

- 打包docker镜像(在Dockfile文件路径下)：

 > docker build -t smart_tools .

 > docker run -d -p 8000:5050 smart_tools


---

## 数据库迁移升级：

 - 使用flask-migrate和flask-script实现。

 - 修改数据库模型时，可以运行以下语句升级数据库：
   ```python
   python manage.py  db  migrate
   python manage.py  db  upgrade
   ```

 - 使用 python  manage.py  init_db 则会清空所有数据重新建表。