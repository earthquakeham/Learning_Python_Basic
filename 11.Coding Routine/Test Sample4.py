# 문서 파일을 읽어서 그 문서 파일 안에 있는 탭 문자(Tab)를 "*"" 4개로 바꾸어 주는 프로그램

import os

# 현재 스크립트의 디렉토리 경로를 동적으로 가져오기
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TAB_FILE = os.path.join(SCRIPT_DIR, "Test Sample4_tab.txt")
STAR_FILE = os.path.join(SCRIPT_DIR, "Test Sample4_star.txt")

# Step1. Basic
# f = open(TAB_FILE, "r")
# data = f.read()
# data2 = data.replace("  ","****")
# print(data)
# print(data2)

# Step2. Add... Modify...
f = open(TAB_FILE, "r")
data = f.read()
f.close()

data2 = data.replace("\t", "*" * 4)
f = open(STAR_FILE, "w")
f.write(data2)
f.close()
