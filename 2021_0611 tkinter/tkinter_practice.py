import tkinter as tk
import pandas as pd
import os

print(os.getcwd())

# 데이터 불러와서 변수로 선언
# . 해당폴더 / .. 상위폴더
dat = pd.read_excel("./korean_dictionary.xls")

# 기능 추가
# 제출 버튼을 클릭했을 때, 동작 가능

def click():
    print('버튼이 클릭되었습니다.')
    word = entry.get()
    output1.delete(0.0, tk.END)
    output2.delete(0.0, tk.END)

    try:
        def_word1 = dat.loc[dat['단어'] == word, '품사'].values[0]

    except:
        def_word1 = '품사를 찾을 수 없음.'
        # dat = window_add(dat)

    try:
        def_word2 = dat.loc[dat['단어'] == word, '풀이'].values[0]

    except:
        def_word2 = '풀이를 찾을 수 없음.'

    output1.insert(tk.END, def_word1)
    output2.insert(tk.END, def_word2)

window = tk.Tk()
window.title("한국어 풀이 사전")



# 01 입력 상자 설명 레이블
label = tk.Label(window, text='원하는 단어 입력후 엔터키 누르기')
label.grid(row=0, column=0, sticky='w')

# 02 텍스트 입력이 가능한 상자 (Entry)
entry = tk.Entry(window, width=15, bg='white')
entry.grid(row=1, column=0, sticky='w')

# 03 제출 버튼 추가
btn = tk.Button(window, text="제출", width=5, command=click)
btn.grid(row=2, column=0, sticky='w')

# 04 설명 레이블 - 의미
label2 = tk.Label(window, width=5, relief='solid', text='품사')
label2.grid(row=3, column=0, sticky='w')

label3 = tk.Label(window, width=5, relief='solid', text='풀이')
label3.grid(row=3, column=1, sticky='w')

# 05 텍스트 박스 입력 상자
output1 = tk.Text(window, width=30, height=2, wrap='word', background='light green')
output1.grid(row=4, column=0, columnspan=2, sticky='w')
output2 = tk.Text(window, width=30, height=2, wrap='word', background='white')
output2.grid(row=4, column=1, columnspan=2, sticky='w')


# window.geometry("640x400+100+100")
# window.resizable(True, True)
window.mainloop()

print('tkinter 프로젝트 연습')