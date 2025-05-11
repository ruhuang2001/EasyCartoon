# EasyCartoon
将[全是漫画](https://github.com/hongchacha/cartoon)app下载的文件合并成pdf用于全平台观看的小工具

## 目前实现
- 能够识别整数话jpg的转换合并 (因为有些特别篇名字排序后错乱，后续可能会考虑如何实现Windows默认排序)

## 使用方法

### 准备
Golang 环境和下载好的漫画文件 [操作办法]()(TODO)

### 下载仓库

```shell
git clone https://github.com/ruhuang2001/EasyCartoon.git
```
或者直接点击右上角`Code`中`Download Zip`下载后解压

### 运行
将所有漫画文件移至`EasyCartoon`的`test`文件夹下（如果没有`test`文件夹自行创建一个）
```shell
go mod tidy  # 首次运行，安装依赖
go run main.go -path=./test/ -output=./cartoon.pdf -prefix=_第
```

参数说明：

- -path: 漫画文件夹路径，默认为./test/
- -output: 输出的PDF文件路径，默认为./cartoon.pdf
- -prefix: 漫画文件夹前缀，默认为_第

## 感谢
https://github.com/hongchacha/cartoon
