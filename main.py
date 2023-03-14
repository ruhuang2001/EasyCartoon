import os
import shutil
from natsort import natsorted
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfgen import canvas

# 下载的文件夹
cartoon_path = './test/'
# 生成的pdf
cartoon_pdf = './cartoon.pdf'
# 存储所有图像路径
all_img = []


# 修改文件夹的名字，以便排序
def renamePre(path):
    filename = os.listdir(path)
    for file in filename:
        if file.startswith('_第'):
            temp = file.split("_第", 1)[1]
            new_file = temp.split("话", 1)[0]
            os.rename(path + '/' + file, path + '/' + new_file)
        else:
            shutil.rmtree(path + file + '/')


# 找一个文件夹下所有的图片, 加入all_img
def findImg(path):
    filename = os.listdir(path)
    for file in filename:
        if file.endswith('.jpg'):
            fullname = os.path.join(path, file)
            all_img.append(fullname)


# 找到所有的img文件
def findAllImg(path):
    folders = sorted(os.listdir(path))
    folders = natsorted(folders)

    # 自然排序后遍历加入all_img
    for folder in folders:
        current_path = path + folder + '/'
        findImg(current_path)


# 合并所有图片到pdf
def imageToPdf(pdf_path):
    pages = 0
    (w, h) = portrait(A4)
    c = canvas.Canvas(pdf_path, pagesize=portrait(A4))
    for i in all_img:
        c.drawImage(i, 0, 0, w, h)
        c.showPage()
        pages = pages + 1
    c.save()


def main():
    # 因为test文件夹已经改好名字了，所有无需执行这个，第一次执行请取消下面的注释
    # renamePre(cartoon_path)
    findAllImg(cartoon_path)
    imageToPdf(cartoon_pdf)


if __name__ == '__main__':
    main()
