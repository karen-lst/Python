## Django库的开发流程、安装测试、操作指令
- `pip install django`
- `python -m django --version`

## 开发流程、指令
- 新建一个Web框架工程
    - `django-admin startproject cloudms`
- 新建应用
    + `python manage.py startapp msgapp`
- 增加模板，配置路径
    + 添加模板`msgapp/templates/MsgSingleWeb.html`
    + 操作`cloudms/settings.py`
    + 设定URL路由，本地路由`msgapp/urls.py `和全局路由` cloudms/urls.py`
- 编写交互代码`msgapp/views.py`
- 编写模板`msgapp/templates/MsgSingleWeb.html`
- 调试运行Web框架（在mysite工程目录下）`python manage.py runserver`

