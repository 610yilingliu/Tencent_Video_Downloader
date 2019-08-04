import requests
import urllib
import os

def dllist():
	if os.path.isfile('dllist.txt'):
		infile=open('dllist.txt','r')
		contents=infile.readlines()
		ls=[]
		print('File List: ')
		for i in range(int(len(contents)/2)):
			ls.append([contents[i*2].replace('\n',''),contents[i*2+1].replace('\n','')])
			print(contents[i*2].replace('\n',''))
		return ls

def dl(input_ls):
	print('请求视频源中，请等待（若网速慢可能需要等待2分钟左右)...')
	for j in range(len(input_ls)):
		with open(input_ls[j][0]+".mp4","wb") as current_video:
			i=1
			while i<30:
				try: 
					url =input_ls[j][1].format(str(i))
					print('当前下载地址：'+url)
					f = requests.get(url)
					print(f)
					st=urllib.request.urlopen(url).status
					print('HTTP Status '+str(st))
					print('Downloading Source File From '+url)
					current_video.write(f.content)
				except:
					print('END OF LIST')
					break
			current_video.close()
			print(input_ls[j][0]+" 下载完成")
			
def main():
	dl(dllist())

main()
