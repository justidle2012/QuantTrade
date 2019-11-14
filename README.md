# QuantTrade
量化交易

Python语言

基于TqSDK

# 目的

实现期货的量化交易

# 开发环境

Win10 + Python 3.7 + VSCode

# 目录结构

logs	 用来存放输出的日志文件 

utils	一些应用类

strategy	策略



# 如何搭建环境

## Win10环境

### 安装Python

从https://www.python.org/downloads/下载Python3.7。然后运行安装文件。安装完成后，win+r运行cmd，运行

```
python -v
```

如果有反馈，说明python正确安装。

### 安装pip

从https://pypi.org/project/pip/#files下载pip，可以选择tar.gz文件并解压。win+r运行cmd，进入对应的目录，运行：

```
python setup.py install
```

### 安装TqSDK

win+r运行cmd，运行

```
pip install tqsdk
```

### 升级TqSDK

win+r运行cmd，运行

```
pip install --upgrade tqsdk
```

# 关于TqSDK

文档：https://doc.shinnytech.com/tqsdk/latest/。

源码：https://github.com/shinnytech/tqsdk-python/tree/master/tqsdk。