# UI自动化框架

## 1. 框架说明

### 1.1. 路径说明

```
Platform2.0_UI_Auto_Test
- Auth	保存登录状态，用于执行非登录用例时使用
- BasePage	高频定位和操作的封装
- BuildLibrary	内建库，参数设置、获取、替换
- Common	公用注解和方法，目前封装了Allure生成报告
- Config	项目配置文件：基础地址，Playwright配置
- Logs	失败用例日志
- Pages	页面对象，包括页面元素和操作
- TestCases	用例文件夹
- TestDatas	测试数据文件夹
- TestFiles	用例中需要使用到的文件
- TestReport	测试报告
- Utils	其他工具模块
- .gitignore
- conftest.py	pytest中的fixtures方法
- pytest.ini	pytest的配置文件
- requirements.txt	框架依赖
- runner.py	用例统一执行入口
```

### 1.2. 环境依赖

```
框架依赖：
1.allure-pytest==2.13.1
2.allure-python-commons==2.13.1
3.attrs==23.1.0
4.colorama==0.4.6
5.exceptiongroup==1.1.1
6.greenlet==2.0.1
7.iniconfig==2.0.0
8.packaging==23.1
9.playwright==1.32.1
10.pluggy==1.0.0
11.pyee==9.0.4
12.pytest==7.3.1
13.pytest-ordering==0.6
14.pytest-rerunfailures==11.1.2
15.PyYAML==6.0
16.tomli==2.0.1
17.typing_extensions==4.5.0
外部依赖：
1.Aullre >= 2.0
```

## 2. 使用方法

### 2.1. 安装依赖

```
框架依赖：
pip install -r requirements.txt

Allure安装参考：
https://docs.qameta.io/allure-report/
```

### 2.2. Playwright

```
在命令行执行
playwright install [optional: browser type]
[browser type]为可选参数，参数包括：chromium firefox webkit
```

## 3. 部分命令

### 3.1. 录制脚本

```
playwright codegen [url]
参考：https://playwright.dev/python/docs/codegen
```

### 3.2. 测试过程回放

```
playwright show-trace [path]
参考：https://playwright.dev/python/docs/trace-viewer
```

