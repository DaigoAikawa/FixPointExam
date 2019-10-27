#!/usr/bin/python
# coding: UTF-8
import pandas as pd

df = pd.DataFrame(columns=['remote-host','client','user','date time','request',' status','size','Referer','User-Agent'])

print('集計対象のログファイルの数：', end="")
N = input()
N = int(N)
files=[]

for n in range(N):
	print(str(n+1) + "個目のファイル名：", end="")
	file = input()
	files.append(file)

for filename in files:
	handle = open(filename)
	log = handle.readline()
	print(filename +'をログファイルを読み込んでいます')
	while log :
		#print(x)
		line = log.split('"', 4)
		line2 = line[0].split(' ', 3)
		line3 = line[2].split()
		parts = []
		for i in range(4):
			parts.append(line2[i])
		parts.append(line[1])
		for j in range(2):
			parts.append(line3[j])
		for k in range(2):
			if (line[k+3]):
				parts.append(line[k+3])
			else :
				parts.append(null)

		parts[3] = parts[3].strip("[")
		parts[3] = parts[3].strip("] ")
		parts[8] = parts[8].strip("\n")
		parts[8] = parts[8].strip(' "')
		#parts[3] = parts[3].strip(' +0900')
		parts[3] = parts[3].split(":",1)
		tmp_se = pd.Series([parts[0],parts[1],parts[2],pd.to_datetime(parts[3][0]+" "+parts[3][1]),parts[4],parts[5],parts[6],parts[7],parts[8]], index=df.columns)
		df = df.append(tmp_se, ignore_index=True)
		log = handle.readline()
	handle.close()

print("集計するデータの時間帯を入力します")
print("範囲の’始点’を記入してください")
print("年：", end="")
sy=input()
print("月：", end="")
sm=input()
print("日：", end="")
sd=input()
print("時：", end="")
sh=input()
print("分：", end="")
smin=input()
print("秒：", end="")
ss=input()
print("範囲の’終点’を記入してください")
print("年：", end="")
ey=input()
print("月：", end="")
em=input()
print("日：", end="")
ed=input()
print("時：", end="")
eh=input()
print("分：", end="")
emin=input()
print("秒：", end="")
es=input()
trimdf = df[(df["date time"] >= pd.to_datetime(sd+"/"+sm+"/"+sy+" "+sh+":"+smin+":"+ss+" +0900"))&(df["date time"] <= pd.to_datetime(ed+"/"+em+"/"+ey+" "+eh+":"+emin+":"+es+" +0900"))]
print(sd+"/"+sm+"/"+sy+" "+sh+":"+smin+":"+ss+"から"+ed+"/"+em+"/"+ey+" "+eh+":"+emin+":"+es+"までのアクセス数：")
print(len(trimdf))

print(sd+"/"+sm+"/"+sy+" "+sh+":"+smin+":"+ss+"から"+ed+"/"+em+"/"+ey+" "+eh+":"+emin+":"+es+"までにアクセスしたホスト別の回数を表示します．")
print("表示件数を入力してください：", end="")
kensu = input()
vc = trimdf['remote-host'].value_counts()
print("リモートホスト名　　　　アクセス回数")
print(vc.head(int(kensu)))
print("")
print("プログラムを終了します")