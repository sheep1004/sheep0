"""
百钱百鸡问题
说明：百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
"""
for cock in range(1,20):
    for hen in range(1,33):
        chick = 100 - cock -hen
        if 100 == 5*cock + 3*hen + chick/3:
            print(f'公鸡有{cock:d}只，母鸡有{hen:d}只，小鸡有{chick:d}只')
            break