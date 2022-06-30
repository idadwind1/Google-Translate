#提示
print('不要关闭这个窗口！！！')
#import
import tkinter as tk
import googletrans
#简化谷歌翻译
translate = googletrans.Translator(
    service_urls=['translate.google.cn']
).translate
#制作窗口
window = tk.Tk()
window.title('谷歌生草机    作者：bilibili MC着火的冰块 https://space.bilibili.com/551409211')
window.geometry('1000x618+100+100')
lable1 = tk.Label(  #第一句话
    master=window,
    text = '请输入要生草的内容：',
    font=('微软雅黑',20)
)
text_texts = tk.Text(   #输入原文的地方
    master=window,
    font=('微软雅黑',15),
    width=50,
    height=5
)
lable_times = tk.Label( #下面的"翻译次数："
    master=window,
    text = '次数：',
    font=('微软雅黑',20)
)
entry_times = tk.Entry( #输入翻译次数的地方
    master=window,
    font=('微软雅黑',20),
    width=5
)
label_last = tk.Label(  #下面的"生草结果："
    master=window,
    font=('微软雅黑',20),
    text='生草结果：'
)
text_last = tk.Text(    #输出最后结果
    master=window,
    font=('微软雅黑',15),
    width=50,
    height=5,
)
def start_translating():    #翻译的函数
    global translate,text_texts,entry_times,text_last   #global
    texts = text_texts.get('1.0','end') #读取原文
    times = int(entry_times.get())  #读取翻译次数
    for i in range(times):  #循环times次
        texts = translate(texts,dest='en').text #翻译成英文
        texts = translate(texts,dest='zh-cn').text  #翻译成中文
    text_last.delete('1.0','end')   #清空原来的东西
    text_last.insert('end',texts)   #写入结果
button_start = tk.Button(   #"开始翻译"的按钮
    master=window,
    text='开始翻译',
    font=('微软雅黑',15),
    command=start_translating
)
#一大堆place
lable1.place(x=0,y=10)
text_texts.place(x=0,y=60)
lable_times.place(x=0,y=215)
entry_times.place(x=100,y=215)
button_start.place(x=250,y=210)
label_last.place(x=0,y=280)
text_last.place(x=0,y=330)
#mainloop
window.mainloop()
