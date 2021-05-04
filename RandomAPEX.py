from time import sleep
import random
import tkinter as tk
import threading as th
import re

memberlist = ""
weaponlist = ""
legendslist = ""

def initui():
	#place
	root.title(u"RandomApex")
	root.geometry("500x190")
	lbMen.place(x=10, y=8)
	lbLck.place(x=115, y=8)
	lbWep.place(x=165, y=8)
	lbleg.place(x=330, y=8)
	mem1.place(x=10, y=30)
	wep1.place(x=165, y=30)
	leg1.place(x=330, y=30)
	bt1.place(x=460, y=27)
	mem2.place(x=10, y=70)
	wep2.place(x=165, y=70)
	leg2.place(x=330, y=70)
	bt2.place(x=460, y=67)
	mem3.place(x=10, y=110)
	wep3.place(x=165, y=110)
	leg3.place(x=330, y=110)
	bt3.place(x=460, y=107)
	btAll.place(x=410, y=150)
	btClr.place(x=340, y=150)
	btRe.place(x=10, y=150)
	sai.place(x=92, y=153)
	lbUI11.place(x=143, y=28)
	lbUI12.place(x=143, y=68)
	lbUI13.place(x=143, y=108)
	lbUI21.place(x=315, y=28)
	lbUI22.place(x=315, y=68)
	lbUI23.place(x=315, y=108)
	lbUI24.place(x=78, y=151)
	lbLck.place(x=115, y=8)
	ch1.place(x=118, y=27)
	ch2.place(x=118, y=67)
	ch3.place(x=118, y=107)

def clearUI():
	if not chv1.get():
		mem1.delete("0", tk.END)
	if not chv2.get():
		mem2.delete("0", tk.END)
	if not chv3.get():
		mem3.delete("0", tk.END)
	wep1.delete(1.0, tk.END)
	wep2.delete(1.0, tk.END)
	wep3.delete(1.0, tk.END)
	leg1.delete("0", tk.END)
	leg2.delete("0", tk.END)
	leg3.delete("0", tk.END)
	sai.delete("0", tk.END)

def clearUIAll():
	mem1.delete("0", tk.END)
	mem2.delete("0", tk.END)
	mem3.delete("0", tk.END)
	wep1.delete(1.0, tk.END)
	wep2.delete(1.0, tk.END)
	wep3.delete(1.0, tk.END)
	leg1.delete("0", tk.END)
	leg2.delete("0", tk.END)
	leg3.delete("0", tk.END)
	sai.delete("0", tk.END)

def Run():
	try:
		readFile()
		chkState()
		selectMembers()
		selectlegends()
		selectWeapons()
		txtout()
	except Exception as e:
		clearUIAll()
		wep1.insert(1.0, e)

def readFile():
	memberpath = "member.txt"
	weaponpath = "weapon.txt"
	legendspath = "legends.txt"
	global memberlist
	global Weaponlist
	global legendslist
	try:
		with open(memberpath,'r',encoding="utf-8_sig") as f:
			memberlist = f.readlines()
			f.close()
		with open(weaponpath,'r',encoding="utf-8_sig") as f:
			Weaponlist = f.readlines()
			f.close()
		with open(legendspath,'r',encoding="utf-8_sig") as f:
			legendslist = f.readlines()
			f.close()
	except Exception as e:
		print(e)

def chkState():
	global memberlist
	try:
		if len(memberlist) == 0:
			raise  Exception('member.txtを確認して')
	except Exception as e:
		raise

def selectMembers():
	clearMember()
	if len(memberlist) > 0:
		if not chv1.get():
			selectMember(1)
	if len(memberlist) > 1:
		if not chv2.get():
			selectMember(2)
	if len(memberlist) > 2:
		if not chv3.get():
			selectMember(3)

def clearMember():
	if not chv1.get():
		mem1.delete("0", tk.END)
	if not chv2.get():
		mem2.delete("0", tk.END)
	if not chv3.get():
		mem3.delete("0", tk.END)

def selectMember(mem):
	global memberlist
	if mem==1:
		mem1.delete("0", tk.END)
	elif mem==2:
		mem2.delete("0", tk.END)
	elif mem==3:
		mem3.delete("0", tk.END)
	str1 = mem1.get()
	str2 = mem2.get()
	str3 = mem3.get()
	ml = random.sample(memberlist,1)
	while ml[0] == mem1.get() or ml[0] == mem2.get() or ml[0] == mem3.get():
		ml = random.sample(memberlist,1)
	if mem==1:
		mem1.insert(tk.END, ml[0])
	elif mem==2:
		mem2.insert(tk.END, ml[0])
	elif mem==3:
		mem3.insert(tk.END, ml[0])

def selectWeapons():
	if len(memberlist) > 0:
		selectWeapon(1)
	if len(memberlist) > 1:
		selectWeapon(2)
	if len(memberlist) > 2:
		selectWeapon(3)

def selectWeapon(mem):
	global Weaponlist
	wl = random.choices(Weaponlist,k=2)
	if mem==1:
		wep1.delete(1.0, tk.END)
		wep1.insert(1.0, wl[0])
		wep1.insert(1.0, wl[1])
	elif mem==2:
		wep2.delete(1.0, tk.END)
		wep2.insert(1.0, wl[0])
		wep2.insert(1.0, wl[1])
	elif mem==3:
		wep3.delete(1.0, tk.END)
		wep3.insert(1.0, wl[0])
		wep3.insert(1.0, wl[1])

def selectlegends():
	if len(memberlist) > 0:
		selectlegend(1)
	if len(memberlist) > 1:
		selectlegend(2)
	if len(memberlist) > 2:
		selectlegend(3)

def selectlegend(mem):
	global legendslist
	
	str1 = leg1.get()
	str2 = leg2.get()
	str3 = leg3.get()
	ll = random.sample(legendslist,1)
	while ll[0] == leg1.get() or ll[0] == leg2.get() or ll[0] == leg3.get():
		ll = random.sample(legendslist,1)
	if mem==1:
		leg1.delete("0", tk.END)
		leg1.insert(tk.END, ll[0])
	elif mem==2:
		leg2.delete("0", tk.END)
		leg2.insert(tk.END, ll[0])
	elif mem==3:
		leg3.delete("0", tk.END)
		leg3.insert(tk.END, ll[0])

def reSelectLegend(mem):
	selectlegend(mem)
	txtout()

def saichusen():
	if sai.get() == "":
		sailist = ["そのまま再戦","再抽選"]
		sl = random.sample(sailist,1)
		sai.insert(tk.END, sl[0])
	else:
		sai.delete("0", tk.END)

def txtout():
	outFile = "outtext.txt"
	txmem1 = mem1.get()
	txmem2 = mem2.get()
	txmem3 = mem3.get()
	txwep1 = wep1.get("1.0", "end -1c")
	txwep2 = wep2.get("1.0", "end -1c")
	txwep3 = wep3.get("1.0", "end -1c")
	txleg1 = leg1.get()
	txleg2 = leg2.get()
	txleg3 = leg3.get()
	txmem1 = re.sub("\n", "", txmem1)
	txmem2 = re.sub("\n", "", txmem2)
	txmem3 = re.sub("\n", "", txmem3)
	txwep1 = re.sub("  $", "", re.sub("\n", "\n  ", re.sub("^", "  ", txwep1)))
	txwep2 = re.sub("  $", "", re.sub("\n", "\n  ", re.sub("^", "  ", txwep2)))
	txwep3 = re.sub("  $", "", re.sub("\n", "\n  ", re.sub("^", "  ", txwep3)))
	txleg1 = re.sub("^", "  ", txleg1)
	txleg2 = re.sub("^", "  ", txleg2)
	txleg3 = re.sub("^", "  ", txleg3)

	with open(outFile, 'w', encoding='utf-8') as outf:
		outf.write("【 " + txmem1 + " 】\n")
		outf.write(">Weapons\n")
		outf.write(txwep1)
		outf.write(">Legend\n")
		outf.write(txleg1)
		outf.write("\n")
		outf.write("【 " + txmem2 + " 】\n")
		outf.write(">Weapons\n")
		outf.write(txwep2)
		outf.write(">Legend\n")
		outf.write(txleg2)
		outf.write("\n")
		outf.write("【 " + txmem3 + " 】\n")
		outf.write(">Weapons\n")
		outf.write(txwep3)
		outf.write(">Legend\n")
		outf.write(txleg3)
		outf.write("\n")

if __name__=='__main__':
	root = tk.Tk()
	lbMen = tk.Label(root,text=u'メンバー')
	mem1 = tk.Entry(root,width=17)
	mem2 = tk.Entry(root,width=17)
	mem3 = tk.Entry(root,width=17)
	lbWep = tk.Label(root,text=u'指定銃器')
	wep1 = tk.Text(root,width=20,height=2)
	wep2 = tk.Text(root,width=20,height=2)
	wep3 = tk.Text(root,width=20,height=2)
	lbleg = tk.Label(root,text=u'レジェンド')
	leg1 = tk.Entry(root,width=20)
	leg2 = tk.Entry(root,width=20)
	leg3 = tk.Entry(root,width=20)
	btAll = tk.Button(root, text='抽選', width=10, command=lambda: Run())
	bt1 = tk.Button(root, text="再", width=2, command=lambda: reSelectLegend(1))
	bt2 = tk.Button(root, text="再", width=2, command=lambda: reSelectLegend(2))
	bt3 = tk.Button(root, text="再", width=2, command=lambda: reSelectLegend(3))
	btRe = tk.Button(root, text="再戦判定", width=8, command=lambda: saichusen())
	sai = tk.Entry(root,width=15)
	btClr = tk.Button(root, text="クリア", width=8, command=lambda: clearUI())
	lbUI11 = tk.Label(root,width=2,text=u">>")
	lbUI12 = tk.Label(root,width=2,text=u">>")
	lbUI13 = tk.Label(root,width=2,text=u">>")
	lbUI21 = tk.Label(root,width=1,text=u":")
	lbUI22 = tk.Label(root,width=1,text=u":")
	lbUI23 = tk.Label(root,width=1,text=u":")
	lbUI24 = tk.Label(root,width=1,text=u":")
	lbLck = tk.Label(root,text=u'固定')
	chv1 = tk.BooleanVar(value = False)
	chv2 = tk.BooleanVar(value = False)
	chv3 = tk.BooleanVar(value = False)
	ch1 = tk.Checkbutton(root,variable = chv1)
	ch2 = tk.Checkbutton(root,variable = chv2)
	ch3 = tk.Checkbutton(root,variable = chv3)

	readFile()
	initui()
	root.mainloop()

