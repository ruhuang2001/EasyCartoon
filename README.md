# EasyCartoon
将[全是漫画](https://github.com/hongchacha/cartoon)app下载的文件合并成pdf用于全平台观看的小工具

## 目前实现
- 能够识别整数话jpg的转换合并 (因为有些特别篇名字排序后错乱，后续可能会考虑如何实现Windows默认排序)

## 使用方法

### 准备
Python环境和下载好的漫画文件 [操作办法]()(TODO)

### 下载仓库

```shell
git clone https://github.com/ruhuang2001/EasyCartoon.git
```
或者直接点击右上角`Code`中`Download Zip`下载后解压

### 运行
将所有漫画文件移至`EasyCartoon`的`test`文件夹下（如果没有`test`文件夹自行创建一个）, 根据漫画文件夹名修改`main.py`中第14行`pre`变量的值

```python
# 下载漫画文件夹的前缀(例如：_第x话 的前缀是 "_第"，话数前的所有内容叫前缀)
pre = "_第"
```

```shell
pip install -r requestments.txt
python main.py
```
或者使用Pycharm等编译器安装好`requestments`中的库运行`main.py`

## 感谢
https://github.com/hongchacha/cartoon
