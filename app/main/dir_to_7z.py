# coding=utf8
# 将目录内所有文件打包压缩为7z
# 参数：源文件目录，压缩文件保存目录，压缩文件名
# -*- coding: utf-8 -*-

import os
import zipfile
import re


def dir_to_7z(dir_path, zip_path, zip_name):
    try:
        # 检查参数目录，若不存在，创建
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        if not os.path.exists(zip_path):
            os.makedirs(zip_path)
        # 创建压缩文件
        zip_path_name = zip_path + zip_name
        zf = zipfile.ZipFile(zip_path_name, 'w', zipfile.ZIP_DEFLATED)
        # 遍历目标目录
        for root, dirs, files in os.walk(dir_path, topdown=False):
            fpath = root.replace(dir_path, '')  # 这一句很重要，不replace的话，就从根目录开始复制
            fpath = fpath and fpath + os.sep or ''  # 这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
            for filename in files:
                zf.write(os.path.join(root, filename), fpath + filename)
        zf.close()
        # print "succeed"
    except Exception as e:
        # print "failed", e
        pass


if __name__ == "__main__":
    root_path = u"E:\\block_han\\mydata\\my_python\\my_learn\\flask_learn\\flasky-first-edition"
    str = u"组网工程_实验一"
    print str.split("_")
    class_name = str.split('_')[0]
    test_num = str.split('_')[1]
    doc_dir = root_path + "\\upload" + "\\" + class_name + '\\' + test_num
    zip_dir = root_path + "\\download"
    zip_name = "\\docx.zip"
    dir_to_7z(doc_dir, zip_dir, zip_name)

