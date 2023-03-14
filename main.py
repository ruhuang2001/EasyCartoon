import os
import shutil
from natsort import natsorted
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfgen import canvas
from pypdf import PdfWriter

cartoon_path = './test/'
# temp_pdf = './temp.pdf'
cartoon_pdf = './cartoon.pdf'
all_img = []  # 存储的图像名路径
merger = PdfWriter()


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
def findAllFile(path):
    filename = os.listdir(path)
    for file in filename:
        if file.endswith('.jpg'):
            fullname = os.path.join(path, file)
            all_img.append(fullname)


# 合并所有图片到pdf
def imageToPdf(pdf_path):
    pages = 0
    (w, h) = portrait(A4)
    c = canvas.Canvas(pdf_path, pagesize=portrait(A4))
    # findAllFile(img_path)
    for i in all_img:
        c.drawImage(i, 0, 0, w, h)
        c.showPage()
        pages = pages + 1
    c.save()


def mergeAllPdf(path, pdf_path):
    folders = sorted(os.listdir(path))
    folders = natsorted(folders)
    # 自然排序后遍历加入all_img
    for folder in folders:
        current_path = path + folder + '/'
        # imageToPdf(pdf_path)
        findAllFile(current_path)
        # merger.append(pdf_path)
        # all_img.clear()

    imageToPdf(pdf_path)
    # merger.append(pdf_path)
    # # 写入cartoon.pdf中
    # merger.write(merge_pdf)
    # merger.close()


def main():
    # 因为test文件夹已经改好名字了，所有无需执行这个，第一次执行请取消下面的注释
    # renamePre(cartoon_path)
    mergeAllPdf(cartoon_path, cartoon_pdf)


if __name__ == '__main__':
    main()
