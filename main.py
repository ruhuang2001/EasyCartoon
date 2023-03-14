import os
import shutil
from natsort import natsorted
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfgen import canvas
from pypdf import PdfWriter

allImg = []  # 存储的图像名路径
merger = PdfWriter()


# 改好文件夹的名字，以便排序
def renamePre(path):
    filename = os.listdir(path)
    for file in filename:
        if file.startswith('_第'):
            temp = file.split("_第", 1)[1]
            new_file = temp.split("话", 1)[0]
            os.rename(path + '/' + file, path + '/' + new_file)
        else:
            shutil.rmtree(path + file + '/')


# 找到一个文件夹下所有的图片
def findAllFile(path):
    filename = os.listdir(path)
    for file in filename:
        if file.endswith('.jpg'):
            fullname = os.path.join(path, file)
            allImg.append(fullname)


# 图片变pdf
def imageToPdf(img_path, pdf_path):
    pages = 0
    (w, h) = portrait(A4)
    c = canvas.Canvas(pdf_path, pagesize=portrait(A4))
    findAllFile(img_path)
    for i in allImg:
        c.drawImage(i, 0, 0, w, h)
        c.showPage()
        pages = pages + 1
    c.save()


def mergeAllPdf(path, pdf_path):
    folders = sorted(os.listdir(path))
    folders = natsorted(folders)

    for folder in folders:
        newpath = path + folder + '/'
        imageToPdf(newpath, pdf_path)
        # merger = PdfWriter()
        merger.append(pdf_path)
        allImg.clear()


def main():
    path = './test/'
    temp_pdf = './temp.pdf'
    merge_pdf = './cartoon.pdf'
    # renamePre(path)
    mergeAllPdf(path, temp_pdf)
    merger.write(merge_pdf)


if __name__ == '__main__':
    main()
