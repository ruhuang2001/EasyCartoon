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
# 下载漫画文件夹的前缀(例如：_第x话 的前缀是 "_第"，话数前的所有内容叫前缀)
pre = "_第"


# 修改文件夹的名字，以便排序
def rename_folder(path):
    filename = os.listdir(path)
    for file in filename:
        if file.startswith(pre):
            new_file = file.split(pre, 1)[1]
            # new_file = temp.split("话", 1)[0]
            os.rename(path + '/' + file, path + '/' + new_file)
        else:
            shutil.rmtree(path + file + '/')


# 找一个文件夹下所有的图片, 加入all_img
def find_img_path(path):
    filename = os.listdir(path)
    print(filename)
    for file in filename:
        if file.endswith('.jpg'):
            fullname = os.path.join(path, file)
            all_img.append(fullname)


# 找到所有的img文件
def find_all_img(path):
    folders = sorted(os.listdir(path))
    folders = natsorted(folders)

    # 自然排序每话的文件夹名后依次遍历加入all_img
    for folder in folders:
        current_path = path + folder + '/'
        find_img_path(current_path)


# 合并所有图片到pdf
def make_pdf(pdf_path):
    pages = 0
    (w, h) = portrait(A4)
    c = canvas.Canvas(pdf_path, pagesize=portrait(A4))
    for i in all_img:
        c.drawImage(i, 0, 0, w, h)
        c.showPage()
        pages = pages + 1
    c.save()


def main():
    filename = "cartoon.pdf"

    # 避免第二次执行rename_folder把全部文件夹删除
    if not os.path.isfile(filename):
        open(filename, 'w').close()
        rename_folder(cartoon_path)

    find_all_img(cartoon_path)
    # print(all_img)
    make_pdf(cartoon_pdf)


if __name__ == '__main__':
    main()
