from tkinter import messagebox as msg
import tkinter as tk
import random
base = tk.Tk()
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
def genRand(dataset):
	factor = 10 ** max([len(str(dataset[i]).split('.')[-1]) for i in dataset])
	samples = []
	for i in dataset:
		for j in range(int(dataset[i] * factor)):
			samples.append(i)
	return random.choice(samples)
class basic:
        def __init__(self,w,h,peopleCount,initalPatients,infectRate):
                self.w = w
                self.h = h
                self.infectRate = infectRate
                self.people = []
                self.death = []
                self.newDeathCnts = [0]
                self.deathCnts = [0]
                self.curedCnts = [0]
                self.newCuredCnts = [0]
                self.infectedTotalCnts = [initalPatients]
                self.infectedCnts = [initalPatients]
                self.newInfectCnts = [initalPatients]
                self.flag = True
                for i in range(initalPatients):
                        self.people.append([False,random.randint(0,w),random.randint(0,h)])
                for i in range(peopleCount - initalPatients):
                        self.people.append([True,random.randint(0,w),random.randint(0,h)])
        def canInfect(self,index):
                _,x,y = self.people[index]
                newPatients = []
                for i in range(len(self.people)):
                        _,_x,_y = self.people[i]
                        if(abs(_x - x) <= 3 and abs(_y - y) <= 3 and self.people[i][0]):
                                newPatients.append(i)
                return newPatients
        def move(self,index,x,y):
                _,_x,_y = self.people[index]
                _x,_y = _x + x,_y + y
                _x,_y = min(_x,self.w),min(_x,self.h)
                self.people[index] = [_,_x,_y]
                ls = self.canInfect(index)
                for i in ls:
                        if(genRand({1:self.infectRate,0:eliminateError(1 - self.infectRate,self.infectRate)})):
                                self.infectedTotalCnts[-1] += 1
                                self.infectedCnts[-1] += 1
                                self.newInfectCnts[-1] += 1
                                self.people[i][0] = False
        def cure(self,index):
                self.people[index][0] = True
                self.curedCnts[-1] += 1
                self.newCuredCnts[-1] += 1
        def dead(self,index):
                self.deathCnts[-1] += 1
                try:
                        self.people.pop(index)
                except:
                        pass
                self.death.append(index)
        def plot(self):
                ax1 = plt.subplot(211)
                gx,gy = [],[]
                rx,ry = [],[]
                for i in self.people:
                        if(i[0]):
                                gx.append(i[1])
                                gy.append(i[2])
                        else:
                                rx.append(i[1])
                                ry.append(i[2])
                ax1.scatter(gx,gy,c='g',marker='.')
                ax1.scatter(rx,ry,c='r',marker='.')
                ax2 = plt.subplot(212)
                ax2.plot([i for i in range(len(self.newDeathCnts))],self.newDeathCnts,color='c',label='新增死亡人数')
                ax2.plot([i for i in range(len(self.deathCnts))],self.deathCnts,color='k',label='死亡人数总计')
                ax2.plot([i for i in range(len(self.curedCnts))],self.curedCnts,color='b',label='治愈人数总计')
                ax2.plot([i for i in range(len(self.newCuredCnts))],self.newCuredCnts,color='g',label='新增治愈人数')
                ax2.plot([i for i in range(len(self.infectedTotalCnts))],self.infectedTotalCnts,color='y',label='感染人数总计(包含已治愈的)')
                ax2.plot([i for i in range(len(self.infectedCnts))],self.infectedCnts,color='m',label='感染人数总计(不包含已治愈的)')
                ax2.plot([i for i in range(len(self.newInfectCnts))],self.newInfectCnts,color='r',label='新增感染人数')
                if(self.flag):
                        self.flag = False
                        font = fm.FontProperties(fname=r'songti SC.TTF')
                        ax2.legend(prop=font,
                                   title='',
                                   loc='upper left',
                                   shadow=False,
                                   facecolor='white',
                                   edgecolor='black',
                                   ncol=1,
                                   markerfirst=True)
                self.newDeathCnts.append(0)
                self.deathCnts.append(self.deathCnts[-1])
                self.curedCnts.append(self.curedCnts[-1])
                self.newCuredCnts.append(0)
                self.infectedTotalCnts.append(self.infectedTotalCnts[-1])
                self.infectedCnts.append(max(self.infectedCnts[-1] - self.newCuredCnts[-2],0))
                self.newInfectCnts.append(0)
                plt.pause(0.05)
curePreOnce = 10
cureRate = 0.8
infectRate = 0.9
moveRate = 1
deadRate = 0.1
initalPatients = 30
peopleCount = 450
width,height = 300,300
b = basic(width,height,peopleCount,initalPatients,infectRate)
tk.Label(base,text='bed count:').grid(row=0,column=0)
tk.Label(base,text='cure rate:').grid(row=1,column=0)
tk.Label(base,text='infect rate:').grid(row=2,column=0)
tk.Label(base,text='move rate:').grid(row=3,column=0)
tk.Label(base,text='dead rate:').grid(row=4,column=0)
tk.Label(base,text='inital patients:').grid(row=5,column=0)
tk.Label(base,text='people count:').grid(row=6,column=0)
tk.Label(base,text='width:').grid(row=7,column=0)
tk.Label(base,text='height:').grid(row=8,column=0)
e1 = tk.Entry(base)
e2 = tk.Entry(base)
e3 = tk.Entry(base)
e4 = tk.Entry(base)
e5 = tk.Entry(base)
e6 = tk.Entry(base)
e7 = tk.Entry(base)
e8 = tk.Entry(base)
e9 = tk.Entry(base)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)
e6.grid(row=5,column=1)
e7.grid(row=6,column=1)
e8.grid(row=7,column=1)
e9.grid(row=8,column=1)
def submit():
        global e1,e2,e3,e4,e5,e6,e7,e8,e9
        global curePreOnce,cureRate,infectRate,moveRate,deadRate,initalPatients,peopleCount,width,height
        global b,base
        try:
                v1 = int(e1.get())
                v2 = float(e2.get())
                v3 = float(e3.get())
                v4 = float(e4.get())
                v5 = float(e5.get())
                v6 = int(e6.get())
                v7 = int(e7.get())
                v8,v9 = int(e8.get()),int(e9.get())
        except:
                msg.showerror('wrong format','wrong input format')
                return
        curePreOnce,cureRate,infectRate,moveRate,deadRate,initalPatients,peopleCount,width,height = v1,v2,v3,v4,v5,v6,v7,v8,v9
        b = basic(width,height,peopleCount,initalPatients,infectRate)
        base.destroy()
tk.Button(base,text='submit',command=submit).grid(row=9,column=0)
def eliminateError(real,operand):
        if(float(operand).is_integer()):
                precision = 0
        else:
                precision = len(str(operand).split('.')[1])
        return round(real,precision)
def run():
        global base,b
        while(1):
                try:
                        base.update()
                        continue
                except:
                        b.plot()
                for i in range(len(b.people)):
                        move = genRand({(0,0):eliminateError(1 - moveRate,moveRate),
                                        (1,0):moveRate / 8.0,
                                        (1,-1):moveRate / 8.0,
                                        (0,-1):moveRate / 8.0,
                                        (-1,-1):moveRate / 8.0,
                                        (-1,0):moveRate / 8.0,
                                        (-1,1):moveRate / 8.0,
                                        (0,1):moveRate / 8.0,
                                        (1,1):moveRate / 8.0})
                        b.move(i,*move)
                patients = []
                for i in range(len(b.people)):
                        if(not b.people[i][0]):
                                patients.append(i)
                for i in range(curePreOnce):
                        try:
                                i = random.choice(patients)
                        except:
                                break
                        if(genRand({1:cureRate,0:eliminateError(1 - cureRate,cureRate)})):
                                b.cure(i)
                                patients.remove(i)
                for i in range(len(patients) - 1):
                        i = random.choice(patients)
                        if(genRand({1:deadRate,0:eliminateError(1 - deadRate,deadRate)})):
                                b.dead(i)
if(__name__ == '__main__'):
        run()
