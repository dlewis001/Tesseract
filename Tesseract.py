import __main__
# import Tesseract
# from tkinter import *
## Make sure to uncomment the comments!

def create(code,amount):
    with open(__main__.__file__, 'r+') as f:
        lines = f.readlines()
        LF=f'{code.format(i=1)}'.replace(' ','').replace('\\n',
        '').replace('\\t','').replace(',','').replace("''",
        "").replace('\t','').replace('\n','')
        parse=f'{lines}'.replace(' ','').replace('\\n',
        '').replace('\\t','').replace(',','').replace("''","")
        TF=parse.find(f'{LF}')
        if TF>-1:
            x=False
        else: x=True
    if x == False:
        print(f'The code: "{code}" has already been created...',
            '\n You can delete them and try again or create a new code!')
    else:
        with open(__main__.__file__, 'r+') as f:
            lines = f.readlines()
            for j, line in enumerate(lines):
                if line.startswith('Tesseract'):
                    for i in range(1,amount+1):
                        value=code.format(i=i)
                        lines[j] = lines[j].strip() + f'\n\n{value}\n\n'
            f.seek(0)
            for line in lines:
                f.write(line)
                print('Your Code has been made!')

##add a tesseract.destroy() function

# #use: 
# w=Tk()
# w.after(1000)
# w.title("Tesseract Sample")
# w.configure(bg='#1d1d1d')
# w.attributes('-alpha', 1)
# y=int(round(w.winfo_screenheight() / 4))
# x=int(round(w.winfo_screenwidth() / 4))
# height=int(round(w.winfo_screenheight() / 2))
# width=int(round(w.winfo_screenwidth() / 2))
# w.geometry(f'{width}x{height}+{x}+{y}')

# Tesseract.create('def boxfunc{i}():\n\tentrybox{i}=Entry(w,bg="#3d3d3d",fg="white",border=0,text="Now we are Multiboxing!")\n\tentrybox{i}.place(x=0,y=25*{i})\nboxfunc{i}()',1)
# #this is where the code will show up at!
# w.mainloop()
