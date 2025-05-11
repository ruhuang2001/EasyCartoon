package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"

	"github.com/jung-kurt/gofpdf"
	"github.com/facette/natsort"
)

var (
	// 下载的文件夹
	cartoonPath string
	// 生成的pdf
	cartoonPDF string
	// 下载漫画文件夹的前缀(例如：_第x话 的前缀是 "_第"，话数前的所有内容叫前缀)
	pre string
)

// 修改文件夹的名字，以便排序
func renameFolder(path string) {
	files, err := ioutil.ReadDir(path)
	if err != nil {
		fmt.Println("读取目录错误:", err)
		return
	}

	for _, file := range files {
		if file.IsDir() && strings.HasPrefix(file.Name(), pre) {
			newFile := strings.SplitN(file.Name(), pre, 2)[1]
			err := os.Rename(filepath.Join(path, file.Name()), filepath.Join(path, newFile))
			if err != nil {
				fmt.Println("重命名文件夹错误:", err)
			}
		} else if file.IsDir() {
			err := os.RemoveAll(filepath.Join(path, file.Name()))
			if err != nil {
				fmt.Println("删除文件夹错误:", err)
			}
		}
	}
}

// 找一个文件夹下所有的图片, 加入allImg
func findImgPath(path string) []string {
	var imgPaths []string
	files, err := ioutil.ReadDir(path)
	if err != nil {
		fmt.Println("读取目录错误:", err)
		return imgPaths
	}

	fmt.Println(files)
	for _, file := range files {
		if !file.IsDir() && strings.HasSuffix(file.Name(), ".jpg") {
			fullname := filepath.Join(path, file.Name())
			imgPaths = append(imgPaths, fullname)
		}
	}
	return imgPaths
}

// 找到所有的img文件
func findAllImg(path string) []string {
	var allImg []string
	folders, err := ioutil.ReadDir(path)
	if err != nil {
		fmt.Println("读取目录错误:", err)
		return allImg
	}

	// 提取文件夹名称
	var folderNames []string
	for _, folder := range folders {
		if folder.IsDir() {
			folderNames = append(folderNames, folder.Name())
		}
	}

	// 自然排序文件夹名
	natsort.Sort(folderNames)

	// 自然排序每话的文件夹名后依次遍历加入allImg
	for _, folder := range folderNames {
		currentPath := filepath.Join(path, folder)
		imgPaths := findImgPath(currentPath)
		allImg = append(allImg, imgPaths...)
	}

	return allImg
}

// 合并所有图片到pdf
func makePDF(pdfPath string, allImg []string) {
	pdf := gofpdf.New("P", "mm", "A4", "")
	
	for _, imgPath := range allImg {
		pdf.AddPage()
		pdf.Image(imgPath, 0, 0, 210, 297, false, "", 0, "")
	}

	err := pdf.OutputFileAndClose(pdfPath)
	if err != nil {
		fmt.Println("生成PDF错误:", err)
	}
}

func main() {
	// 定义命令行参数
	flag.StringVar(&cartoonPath, "path", "./test/", "漫画文件夹路径")
	flag.StringVar(&cartoonPDF, "output", "./cartoon.pdf", "输出的PDF文件路径")
	flag.StringVar(&pre, "prefix", "_第", "漫画文件夹前缀")
	flag.Parse()

	if !strings.HasSuffix(cartoonPath, "/") {
		cartoonPath += "/"
	}

	fmt.Println("漫画文件夹路径:", cartoonPath)
	fmt.Println("输出PDF路径:", cartoonPDF)
	fmt.Println("文件夹前缀:", pre)

	// 避免第二次执行renameFolder把全部文件夹删除
	if _, err := os.Stat(cartoonPDF); os.IsNotExist(err) {
		file, err := os.Create(cartoonPDF)
		if err != nil {
			fmt.Println("创建文件错误:", err)
			return
		}
		file.Close()
		renameFolder(cartoonPath)
	}

	allImg := findAllImg(cartoonPath)
	makePDF(cartoonPDF, allImg)
	fmt.Println("PDF生成完成!")
}
