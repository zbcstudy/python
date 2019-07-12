import os
import re


# 扫描某个路径下的所有PDF文件
def scan_pdf(root, dirs, files):
    for file in files:
        path = os.path.join(root, file)
        path = os.path.normcase(path)
        if re.search(r".*\.pdf", path):
            print(path)


for root, dirs, files in os.walk("F:\\文档\\2018-01-24"):
    print(root)
    print(dirs)
    print(files)
    scan_pdf(root, dirs, files)
