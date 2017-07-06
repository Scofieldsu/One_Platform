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

 - 使用Vue.js开发前端页面可以选择参数，传参给服务后端，然后请求阿里云市场的api查询数据，经过转换后返回给前端。

 - 小工具箱，方便扩展。
