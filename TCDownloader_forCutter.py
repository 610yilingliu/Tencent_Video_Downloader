import requests
import urllib.request as rq
import os

def dllist():
	if os.path.isfile('dllist.txt'):
		infile = open('dllist.txt','r')
		contents = infile.readlines()
		ls = []
		print('文件列表: ')
		for i in range(int(len(contents)/2)):
			ls.append([contents[i*2].replace('\n',''),contents[i*2+1].replace('\n','')])
			print(contents[i * 2].replace('\n', ''))
		return ls
	else:
		print('dllist.txt 不在目录下')
		input('输入任意字符退出')

def dl(input_list):
	# read list of list
	for i in range(len(input_list)):
		for j in range(1,100):
			try:
				url = input_list[i][1].format(str(j))
				fname = input_list[i][0]
				print('检查链接' + url)
				# If page is available
				print('HTML Status:' + str(rq.urlopen(url).status))
				print('正在下载' + fname + 'part' + str(j) + '，请等待...')
				sourcefile = requests.get(url)
				with open(fname+"_"+str(j)+".mp4","wb") as dl_file:
					dl_file.write(sourcefile.content)
				dl_file.close()
			except:
				print(fname+'中所有分块视频下载成功')
				break

def main():
	print('Author: 风逝无殇（落羽惊云)')
	print('作者很懒，不想写图形界面也不想写下载进度条\n')
	ipt=input('确认开始下载？开始请按Y(大小写无所谓)，不想开始请按其他随便什么乱七八糟的: ')
	if(ipt=='Y' or ipt=='y'):
		dl(dllist())
		print('全部视频资源下载完成')
		input('输入任意字符结束')
	else:
		print('byebye~')
		input('输入任意字符结束')
main()