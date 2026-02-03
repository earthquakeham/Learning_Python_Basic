# 게시물의 총 개수와 한 페이지에 보여 줄 게시물 수를 입력으로 주었을 때 총 페이지 수를 출력하는 프로그램이 필요하다고 한다.

# Step1. Basic
# article_total = 500
# article_page = 34
# page_total = article_total / article_page
# print(page_total)

# Step2. Add... Modify...
article_total = int(input("Total article : "))
article_page = int(input("One page max article : "))
if article_total <= article_page:
    print("Page : 1")
elif article_total % article_page == 0:
    print("Page : ",article_total/article_page)
else:
    print("Page : ",(article_total//article_page)+1)