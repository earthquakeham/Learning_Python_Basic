# 원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장 작성

import os

# 현재 스크립트의 디렉토리 경로를 동적으로 가져오기
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(SCRIPT_DIR, "Test Sample3.txt")

# Step1. Basic
# f = open(FILE_PATH, "w")
# memo = input("Input contents : ")
# f.write(memo)
# f.close()

# Step2. Add... Modify...
f = open(FILE_PATH, "a")
memo = input("Input contents : ")
f.write(memo)
f.write('\n')
f.close()