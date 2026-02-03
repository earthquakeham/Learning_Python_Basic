# 특정 디렉터리부터 시작해서 그 하위(디렉터리 포함)의 모든 파일 중 파이썬 파일(*.py)만 출력해 주는 프로그램을 만들려면 어떻게 해야 할까?

import os

# 현재 스크립트의 상위 디렉토리(1.BASIC) 경로를 동적으로 가져오기
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASIC_DIR = os.path.dirname(SCRIPT_DIR)  # 11.Coding Routine의 상위 디렉토리


# Step1. Basic...이제 이 디렉터리에 있는 파일을 검색할 수 있도록...
def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        print(full_filename)


search(BASIC_DIR)

# Step2. Add... Modify... 확장자가 .py인 파일만을 출력하도록...
# import os
# def search(dirname):
#     filenames = os.listdir(dirname)
#     for filename in filenames:
#         full_filename = os.path.join(dirname, filename)
#         ext = os.path.splitext(full_filename)[-1]
#         if ext == '.py':
#             print(full_filename)
# search(BASIC_DIR)

# Step3. Add... Modify... 확장자가 .py인 파일만을 출력하도록... 하위 폴더까지...
# import os
# def search(dirname):
#     try:
#         filenames = os.listdir(dirname)
#         for filename in filenames:
#             full_filename = os.path.join(dirname, filename)
#             if os.path.isdir(full_filename):
#                 search(full_filename)
#             else:
#                 ext = os.path.splitext(full_filename)[-1]
#                 if ext == '.py':
#                     print(full_filename)
#     except PermissionError:
#         pass
# search(BASIC_DIR)

# Tip! os.walk를 사용하면 앞에서 작성한 코드를 더 간단하게 만들 수 있다. os.walk는 시작 디렉터리부터 시작해 하위에 있는 모든 디렉터리를 차례대로 방문하는 함수이다.

import os

for path, dir, files in os.walk(BASIC_DIR):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == ".py":
            print("%s/%s" % (path, filename))
