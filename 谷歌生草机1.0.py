print('谷歌生草机 作者：bilibili MC着火的冰块')
print('https://space.bilibili.com/551409211')
print()
import googletrans
fanyi = googletrans.Translator(
    service_urls=['translate.google.cn']
).translate
print('请输入原文文件的完整路径：')
before_path = input('>>>')
before_file = open(before_path,mode='r')
texts = before_file.readlines()
before_file.close()
print('\n识别到文件内容：')
print('\n',texts)
print('\n请输入翻译后文件存储的完整路径：')
after_path = input('>>>')
print('\n请输入翻译次数：')
n = int(input('>>>'))
print('\n正在翻译中...')
for i in texts:
    if i=='\n':
        texts.remove(i)
after_file = open(after_path,mode='w')
for i in range(len(texts)):
    i_text = texts[i]
    print(f'正在翻译第{i+1}行...')
    for j in range(n):
        i_text = fanyi(i_text,dest='en').text
        i_text = fanyi(i_text,dest='zh-CN').text
        finished = (j+1)/n
        print(f"\r[{'*'*int(50*finished)}\
{' '*(50-int(50*finished))}]\
\t{round(finished*100,2)}%\t{j+1}/{n}",
              end='')
    after_file.write(i_text+'\n')
    print('\n',i_text)
after_file.close()
print('\n翻译完成！',end='\n')
print(f'已将结果存储到{after_path}')
input('按Enter退出程序')
