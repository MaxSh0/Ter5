
from math import *
from tkinter import *
from array import array
import math 
root = Tk()
w=root.winfo_screenwidth()
h = root.winfo_screenheight()
canv = Canvas(root, width = w, height = 1500)
x0=40
y0=h-200#for class comp h-100
xm=w-50
ym=40
xc=xm/2

#Деление на интервалы
def divideByIntervals(arr_x,arr_n,n,begin,end,middle,count):
        i=0
        print (arr_x)
        print (arr_n)
        #Деление X
        h=(arr_x[len(arr_x)-1]-arr_x[0])/n
        begin.append(arr_x[0])
        while i<n-1:
                end.append(round(begin[i]+h,2))
                middle.append(round((begin[i]+end[i])/2,2))
                i+=1
                begin.append(round(end[i-1],2))
        end.append(arr_x[len(arr_x)-1])
        middle.append(round((begin[i]+end[i])/2,2))
        i=0
        j=0
        print (end)
        #Деление N
        sumInInterval=0
        while i<len(arr_x):
                if arr_x[i]<end[j]:
                        sumInInterval+=arr_n[i]
                #Добавить число появлений последнего элемента в последний элемент массива появлений на интервале
                elif j==n-1 and i==len(arr_x)-1:
                        sumInInterval+=arr_n[i]
                        count.append(sumInInterval)
                else:
                        count.append(sumInInterval)
                        sumInInterval=0
                        j+=1
                        i-=1
                i+=1
        
        print(count)
#Создание массива средних значений
def makeMiddleArray(arr_begin,arr_end,arr_middle):
        i=0
        while i<len(arr_begin):
                arr_middle.append(float((arr_begin[i]+arr_end[i])/2))
                i+=1
                
#Начертить оси координат
def coord (x0, y0, xm, ym, fil_color,x,y):
        canv = Canvas(root, width = w, height = 1500)
        canv.pack()
        canv.create_line(x0,y0,xm+13,y0,fill=fil_color,arrow=LAST)
        canv.create_line(xc,y0,xc,ym,fill=fil_color,arrow=LAST)
        canv.create_text(xm+20,y0,text=str(x))
        canv.create_text(xc,ym-10,text=str(y))

#Записать в массив с файла        
def openFile (fileName, arr):
        with open(str(fileName)) as f:
            for line in f:
                    arr.append([float(x) for x in line.split(" ")])

#Создание статистического ряда из вариационного
def separate (arr, arr_x, arr_n):
        i=0
        currentValue=arr[0]
        cnt = 0
        while i<len(arr):
                if currentValue == arr[i]:
                        cnt += 1
                else:
                        arr_x.append(arr[i-1])
                        arr_n.append(cnt)
                        cnt = 1
                        currentValue = arr[i]
                i+=1
        if cnt!=0:
                arr_x.append(arr[i-1])
        arr_n.append(cnt)
                
#Показать полигон
def showNumbers(arr_x,arr_n,denominator,firstColumn, secondColumn):
        i=0
        print("|",firstColumn,"\t|",secondColumn,"\t|")
        while i<len(arr_x):
                print("|",arr_x[i],"\t|",arr_n[i]/denominator,"\t|")
                i+=1

#Показать интервальный ряд                
def showInterval(begin,end,arr_n,denominator):
        print("|xi-xi+1\t|ni\t|")
        i=0
        while int(i)<int(len(begin)):
                print("|",begin[i],"-",end[i],"\t|",round(float(arr_n[i]/denominator),2),"\t|")
                i+=1
        
#Показать эмпирическую функцию
def showEmpFunc(arr_x,arr_sum,denominator):
        i=0
        print("F*(x)=0 при x<=",arr_x[0])
        while i<len(arr_x)-1:
             print("F*(x)=",arr_sum[i]/denominator," при",arr_x[i],"<x<=",arr_x[i+1])
             i+=1
        print("F*(x)=1 при x>",arr_x[i])

#Начертить полигон частот
def makePoligon(arr_x,arr_n,x,y,max_x, max_y,color,denominator):
        canv = Canvas(root, width = w, height = 1500)
        canv.pack()
        #root.geometry("500x100") #Width x Height
        canv.create_line(x0,y0,xm+13,y0,fill="#000",arrow=LAST)
        canv.create_line(xc,y0,xc,ym,fill="#000",arrow=LAST)
        canv.create_text(xm+20,y0,text=str(x))
        canv.create_text(xc,ym-10,text=str(y))
        i=0
        while i<len(arr_x)-1:
                canv.create_line(xc+(arr_x[i]*xc/max_x), y0-(arr_n[i]*400/max_y), xc+(arr_x[i+1]*xc/max_x), y0-(arr_n[i+1]*400/max_y), width=3,fill=color)
                canv.create_line(xc+(arr_x[i]*xc/max_x),y0, xc+(arr_x[i]*xc/max_x), y0-(arr_n[i]*400/max_y), dash=(4, 2), width=1)
                canv.create_line(xc,y0-(arr_n[i]*400/max_y), xc+(arr_x[i]*xc/max_x), y0-(arr_n[i]*400/max_y), dash=(4, 2), width=1)
                canv.create_text(xc+(arr_x[i]*xc/max_x),y0+10,text=str(round(arr_x[i],2)))
                canv.create_text(xc-10,y0-(arr_n[i]*400/max_y),text=str(round(float(arr_n[i]/denominator),4)))
                i+=1
        canv.create_line(xc+(arr_x[i]*xc/max_x),y0, xc+(arr_x[i]*xc/max_x), y0-(arr_n[i]*400/max_y), dash=(4, 2), width=1)
        canv.create_line(xc,y0-(arr_n[i]*400/max_y), xc+(arr_x[i]*xc/max_x), y0-(arr_n[i]*400/max_y), dash=(4, 2), width=1)
        canv.create_text(xc+(arr_x[i]*xc/max_x),y0+10,text=str(round(arr_x[i],2)))
        canv.create_text(xc-10,y0-(arr_n[i]*400/max_y),text=str(round(float(arr_n[i]/denominator),4)))
        root.mainloop()

#Создание массива префиксной суммы
def makeSumArray(arr_begin, arr_result):
        arr_result.append(arr_begin[0])
        i=1
        while i<len(arr_begin):
                arr_result.append(arr_result[i-1]+arr_begin[i])
                i+=1

#Начеритить эмипирическую функцию
def makeEmpFunc(arr_x,arr_n,x,y,max_x, max_y,color,denominator):
        canv = Canvas(root, width = w, height = 1500)
        canv.pack()
        canv.create_line(x0,y0,xm+13,y0,fill="#000",arrow=LAST)
        canv.create_line(xc,y0,xc,ym,fill="#000",arrow=LAST)
        canv.create_text(xm+20,y0,text=str(x))
        canv.create_text(xc,ym-10,text=str(y))
        i=0
        while i<len(arr_x)-1:
                canv.create_line(xc+(arr_x[i]*(xc-50)/max_x), y0-(arr_n[i]/denominator*400), xc+(arr_x[i+1]*(xc-50)/max_x), y0-(arr_n[i]/denominator*400), width=3,fill=color)
                canv.create_line(xc+(arr_x[i]*(xc-50)/max_x),y0, xc+(arr_x[i]*(xc-50)/max_x), y0-(arr_n[i]*400/denominator), dash=(4, 2), width=1)
                canv.create_line(xc,y0-(arr_n[i]*400/denominator), xc+(arr_x[i]*(xc-50)/max_x), y0-(arr_n[i]*400/denominator), dash=(4, 2), width=1)
                canv.create_text(xc+(arr_x[i]*(xc-50)/max_x),y0+10,text=str(round(arr_x[i],2)))
                canv.create_text(xc-10,y0-(arr_n[i]*400/denominator),text=str(round(arr_n[i]/denominator,4)))
                i+=1
        canv.create_line(xc+(arr_x[i]*(xc-50)/max_x), y0-(arr_n[i]*400/denominator), xm, y0-(arr_n[i]*400/denominator), width=3,fill=color)
        canv.create_line(xc+(arr_x[i]*(xc-50)/max_x),y0, xc+(arr_x[i]*(xc-50)/max_x), y0-(arr_n[i]*400/denominator), dash=(4, 2), width=1)
        canv.create_line(xc,y0-(arr_n[i]*400/denominator), xc+(arr_x[i]*(xc-50)/max_x), y0-(arr_n[i]*400/denominator), dash=(4, 2), width=1)
        canv.create_text(xc+(arr_x[i]*(xc-50)/max_x),y0+10,text=str(round(arr_x[i],2)))
        canv.create_text(xc-10,y0-(arr_n[i]*400/denominator),text=str(round(arr_n[i]/denominator,4)))
        root.mainloop()

#Расчет точечных характеристик
def math(arr_x,arr_n,n):
        i=0
        Xb=0
        Db=0
        while i<len(arr_x):
               Xb+=arr_x[i]*arr_n[i]
               i+=1
        Xb=Xb/n
        i=0
        while i<len(arr_x):
                Db+=pow((arr_x[i]-Xb),2)
                i+=1
        Db=Db/n
        print("Выборочное среднее:")
        print("Хв=(x0*n0+...+xn*nn)/n=",Xb)
        print("Выборочная диспресия:")
        print("Dв=((x0*Xb)^2*n0+...+(xn*Xb)^2*nn)/n=",Db)
        print("Исправленная дисперсия:")
        print("S^2=n/(n-1)*Db=",round(Db*n/(n-1),4))
        print("Среднее квадратическое:")
        print("S=sqrt(S^2)=",round(pow(Db*n/(n-1),0.5),4))

#Ввод данных с клавиатуры
def interNumbers(arr_begin,arr_end, arr_n):
        i=0
        print("Введите число интервалов")
        n=int(input())
        while i<n:
                print("Введите начало ", i+1," интервала: ")
                arr_begin.append(float(input()))
                print("Введите конец ", i+1," интервала: ")
                arr_end.append(float(input()))
                print("Введите число появлений на ", i+1," интервале: ")
                arr_n.append(float(input()))
                i+=1
choose = 1
while choose != 0:
        print("1.Обработка данных из файла (до 100 значений)")
        print("2.Обработка данных из файла (более 100 значений)")
        print("3.Обработка данных, введенных с клавиатуры")
        print("0.Выход")
        choose=int(input("Выберите режим: "))
        if int(choose)==1:
                arrFromFile=[]
                openFile("under100.txt",arrFromFile)
                arrFromFile[0].sort()
                arr_x=[]
                arr_n=[]
                separate(arrFromFile[0],arr_x,arr_n)
                max_x=max(arr_x)
                max_n=float(max(arr_n))
                sum_n=sum(arr_n)
                while choose!=0:
                        print()
                        print("1.1. Вариационный ряд")
                        print("1.2. Статистический ряд частот,построение полигона")
                        print("1.3. Статистический ряд относительных частот,построение полигона")
                        print("1.4. Эмпирическая функция распределения")
                        print("1.5. Просмотр числовых характеристик")
                        print("1.0. Выход")
                        choose=int(input("Выберите режим: "))
                        if choose==1:
                                print("Вариационный ряд")
                                print(arrFromFile[0])
                        elif choose==2:
                                print("Статистический ряд частот")
                                showNumbers(arr_x,arr_n,1,"x","n")
                                root=Tk()
                                makePoligon(arr_x,arr_n,"X","N",max_x,max_n,"#caf",1)
                        elif choose==3:
                                print("Статистический ряд относительных частот")
                                showNumbers(arr_x,arr_n,sum_n,"x","w")
                                root = Tk()
                                makePoligon(arr_x,arr_n,"X","W",max_x,max_n,"#caf",sum_n)
                        elif choose==4:
                                print("Эмпирическая функция распределения")
                                arr_sum_n=[]
                                makeSumArray(arr_n,arr_sum_n)
                                showEmpFunc(arr_x,arr_sum_n,sum_n)
                                root=Tk()
                                makeEmpFunc(arr_x,arr_sum_n,"X","F*(x)",max_x, 1,"#bcc",sum_n)
                        elif choose==5:
                                math(arr_x,arr_n,sum_n)
                        elif choose!=0:
                                print("Введите корректный номер")
                choose=1
        elif choose==2:
                arrFromFile=[]
                openFile("over100.txt",arrFromFile)
                arrFromFile[0].sort()
                arr_x=[]
                arr_n=[]
                separate(arrFromFile[0],arr_x,arr_n)
                n=int(input("Задайте количество интервалов:"))
                begin=[]
                end=[]
                count=[]
                middle=[]
                divideByIntervals(arr_x,arr_n,n,begin,end,middle,count)  
                while choose!=0:
                        print()
                        print("2.1. Интервальный ряд распределения частот")
                        print("2.2. Интервальный ряд распределения относительных частот")
                        print("2.3. Группированный ряд распределения частот,построение полигона")
                        print("2.4. Группированный ряд распределения относительных частот,построение полигона")
                        print("2.5. Эмпирическая функция распределения интервального ряда")
                        print("2.6. Эмпирическая функция распределения группированного ряда")
                        print("2.7. Просмотр числовых характеристик")
                        print("2.0. Выход")
                        choose=int(input("Выберите режим: "))
                        if choose==1:
                                print("Интервальный ряд распределения частот")
                                showInterval(begin,end,count,1)
                        elif choose==2:
                                print("Интервальный ряд распределения относительных частот")
                                showInterval(begin,end,count,sum(arr_n))
                        elif choose==3:
                                print("Группированный ряд распределения частот")
                                showNumbers(middle,count,1,"xi+1","ni")
                                input("Для просмотра полигона частот нажмите Enter")
                                root = Tk()
                                makePoligon(middle,count,"X","N",max(middle),max(count),"#abc",1)
                        elif choose==4:
                                print("Группированный ряд распределения относительных частот")
                                showNumbers(middle,count,sum(count),"xi+1","wi")
                                input("Для просмотра полигона частот нажмите Enter")
                                root = Tk()
                                makePoligon(middle,count,"X","W",max(middle),max(count),"#abc",sum(count))
                        elif choose==5:                                
                                print("Эмпирическая функция распределения интервального ряда")
                                arr_sum_n=[]
                                makeSumArray(count,arr_sum_n)
                                showEmpFunc(end,arr_sum_n,sum(count))
                                root = Tk()
                                makeEmpFunc(end,arr_sum_n,"N","F*(x)",max(end),1,"#abc",sum(count))
                        elif choose==6:
                                print("Эмпирическая функция распределения группированного ряда")
                                showEmpFunc(middle,arr_sum_n,sum(count))
                                root = Tk()
                                makeEmpFunc(middle,arr_sum_n,"N","F*(x)",max(middle),1,"#abc",sum(count))
                        elif choose==7:
                                math(middle,count,sum(count))
                        elif choose!=0:
                                print("Введите корректный номер")
                choose=2
        elif choose==3:
                begin=[]
                end=[]
                arr_n=[]
                interNumbers(begin,end,arr_n)
                middle=[]
                makeMiddleArray(begin,end,middle)  
                while choose!=0:
                        print()
                        print("2.1. Интервальный ряд распределения частот")
                        print("2.2. Интервальный ряд распределения относительных частот")
                        print("2.3. Группированный ряд распределения частот(с полигоном)")
                        print("2.4. Группированный ряд распределения относительных частот(с полигоном)")
                        print("2.5. Эмпирическая функция распределения интервального ряда")
                        print("2.6. Эмпирическая функция распределения группированного ряда")
                        print("2.7. Вывод числовых характерисик")
                        print("2.0. Выход")
                        choose=int(input("Выберите: "))
                        if choose==1:
                                print("Интервальный ряд распределения частот")
                                showInterval(begin,end,arr_n,1)
                        elif choose==2:
                                print("Интервальный ряд распределения относительных частот")
                                showInterval(begin,end,arr_n,sum(arr_n))
                        elif choose==3:
                                print("Группированный ряд распределения частот")
                                showNumbers(middle,arr_n,1,"xi+1","ni")
                                input("Нажмите любую клавишу, чтобы увидеть полигон частот")
                                root = Tk()
                                makePoligon(middle,arr_n,"X","N",max(middle),max(arr_n),"#abc",1)
                        elif choose==4:
                                print("Группированный ряд распределения относительных частот")
                                showNumbers(middle,arr_n,sum(arr_n),"xi+1","wi")
                                input("Нажмите любую клавишу, чтобы увидеть полигон частот")
                                root = Tk()
                                makePoligon(middle,arr_n,"X","W",max(middle),max(arr_n),"#abc",sum(arr_n))
                        elif choose==5:
                                print("Эмпирическая функция распределения интервального ряда")
                                arr_sum_n=[]
                                makeSumArray(arr_n,arr_sum_n)
                                showEmpFunc(end,arr_sum_n,sum(arr_n))
                                root = Tk()
                                makeEmpFunc(end,arr_sum_n,"N","F*(x)",max(end),1,"#abc",sum(arr_n))
                        elif choose==6:
                                print("Эмпирическая функция распределения группированного ряда")
                                showEmpFunc(middle,arr_sum_n,sum(arr_n))
                                root = Tk()
                                makeEmpFunc(middle,arr_sum_n,"N","F*(x)",max(middle),1,"#abc",sum(arr_n))
                        elif choose==7:
                                math(middle,arr_n,sum(arr_n))
                        elif choose!=0:
                                
                                print("Введите корректный номер")
                choose=3
