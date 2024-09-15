#TO REPLACE MANIPULATE DATA WHILE RUNTIME KIND OF A METHOD YOU KNOW
letter='''dear <|name|>,
you ar awesome!
         <|date|>'''
print(letter.replace("<|name|>","vinay").replace("<|date|>","12 june 2204"))         
print(letter.replace("<|name|>","vinay"))
         
#to format string within print function

name=input("enter the NAME")
print(f"good afternoon {name}")
print(name.find("na"))
print(name.replace("na","me"))