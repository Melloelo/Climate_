from tkinter import*
import requests
from PIL import ImageTk,Image
from tkinter import messagebox
from time import strftime
import math
from datetime import datetime


w=Tk()
w.geometry('800x400')
w.iconbitmap('icon.ico')
w.title("Climate")
w.resizable(0,0)

try:
     
     
     def weather_data(query):
                     res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&appid=06c921750b9a82d8f5d1294e1586276f');
                     return res.json();
  


     #Body UI
     Frame(w,width=800,height=50,bg='#353535').place(x=0,y=0)

     #serach bar
     img1 = ImageTk.PhotoImage(Image.open("search.png"))
     def on_enter(e):
             e1.delete(0,'end')    
     def on_leave(e):
          if e1.get()=='':   
               e1.insert(0,'Procure a cidade')

         
     e1 =Entry(w,width=21,fg='white',bg="#353535",border=0)
     e1.config(font=('Calibri (Body)',12))
     e1.bind("<FocusIn>", on_enter)
     e1.bind("<FocusOut>", on_leave)
     e1.insert(0,'Procure a cidade')
     e1.place(x=620,y=15)


     a=datetime.today().strftime('%B')
     b=(a.upper())
     q = datetime.now().month
    
     now = datetime.now()

     c=now.strftime('%B')
     month=c[0:3]
   

     today = datetime.today()

     date = today.strftime("%d")

     def label(a):
          
          Frame(width=500,height=50,bg="#353535").place(x=0,y=0)
          
          
          l2=Label(w, text=str(a),bg="#353535",fg="white")# upper border
          l2.config(font=("Microsoft JhengHei UI Light", 18))
          l2.place(x=20,y=8)

          city=a
          query='q='+city
          w_data=weather_data(query)
          result=w_data
          try:
               check="{}".format(result['main']['temp'])
               celsius="{}".format(result['main']['temp'])
         
          except:
               messagebox.showinfo("", "    cidade não encontrada    ")

          c=(int(float(check)))-273
          descp=("{}".format(result['weather'][0]['description']))
          weather=("{}".format(result['weather'][0]['main']))

          global img

          if c>10 and weather=="Haze" or weather=="Clear":
               Frame(w,width=800,height=350,bg="#f78954").place(x=0,y=50)          
               img = ImageTk.PhotoImage(Image.open("sol.png"))
               Label(w,image=img,border=0).place(x=170,y=130)
               bcolor="#f78954"
               fcolor="white"

          elif c>10 and weather=="Clouds":
               Frame(w,width=800,height=350,bg="#7492b3").place(x=0,y=50)
               img = ImageTk.PhotoImage(Image.open("nuvem.png"))
               Label(w,image=img,border=0).place(x=170,y=130)
               bcolor="#7492b3"
               fcolor="white"

          elif c<=10 and weather=="Clouds":
               Frame(w,width=800,height=350,bg="#7492b3").place(x=0,y=50)
               img = ImageTk.PhotoImage(Image.open("cloudcold.png"))
               Label(w,image=img,border=0).place(x=170,y=130)
               bcolor="#7492b3"
               fcolor="white"

          elif c>10 and weather=="Rain":
               Frame(w,width=800,height=350,bg="#60789e").place(x=0,y=50)
               img = ImageTk.PhotoImage(Image.open("chuva.png"))
               Label(w,image=img,border=0).place(x=170,y=130)
               bcolor="#60789e"
               fcolor="white"

          elif c<=10 and weather=="Fog" or weather=="Clear":
               Frame(w,width=800,height=350,bg="white").place(x=0,y=50)          
               img = ImageTk.PhotoImage(Image.open("frio.png"))
               Label(w,image=img,border=0).place(x=170,y=130)
               bcolor="white"
               fcolor="black"
                    
          else:
               Frame(w,width=800,height=350,bg="white").place(x=0,y=50)
              
               label=Label(w,text=weather,border=0,bg='white')
               label.configure(font=(("Microsoft JhengHei UI Light", 18)))
               label.place(x=160,y=130)
               bcolor="white"
               fcolor="black"

          w_data=weather_data(query)
          result=w_data


          e=("Umidade: {}".format(result['main']['humidity']))
          f=("Pressão: {}".format(result['main']['pressure']))
          g=("Temperatura Maxima: {}".format(result['main']['temp_max']))
          h=("Temperatura Minima: {}".format(result['main']['temp_min']))
          b1=b=("Velocidade do Vento: {} m/s".format(result['wind']['speed']))
          
          
          l5=Label(w, text=str(month+"  "+ date),bg=bcolor,fg=fcolor)
          l5.config(font=("Microsoft JhengHei UI Light", 25))
          l5.place(x=330,y=335)          

          l4=Label(w, text=str(str(e+"%")),bg=bcolor,fg=fcolor)
          l4.config(font=("Microsoft JhengHei UI Light", 11))
          l4.place(x=510,y=135)

          

          l4=Label(w, text=str(str(f+" hPa")),bg=bcolor,fg=fcolor)
          l4.config(font=("Microsoft JhengHei UI Light", 11))
          l4.place(x=510,y=175)

          l4=Label(w, text=str(str(b1)),bg=bcolor,fg=fcolor)
          l4.config(font=("Microsoft JhengHei UI Light", 11))
          l4.place(x=510,y=215)
          

          l3=Label(w, text=str(str(c) +"°C"),bg=bcolor,fg=fcolor)
          l3.config(font=("Microsoft JhengHei UI Light", 40))
          l3.place(x=330,y=150)
               
     label(a="Delhi")

     def cmd1():
          b=str(e1.get())
          label(str(b))
                
     Button(w,image=img1,command=cmd1,border=0).place(x=750,y=10)

except:
     
     Frame(w,width=800,height=400,bg='white').place(x=0,y=0)
     global imgx
     imgx = ImageTk.PhotoImage(Image.open("nointernet.png"))

     Label(w,image=imgx,border=0).pack(expand=True)
     
w.mainloop()
