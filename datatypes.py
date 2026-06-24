#int->float
a=10
print(float(a)) #10.0
#int->str
a=10
print(str(a)) #'10'
#int->bool
a=10
print(bool(a)) #True
#int->list
list(10) #gives type error
#int->tuple
tuple(10)#gives type error
#float->int
a=10.8
print(int(a)) #10
#float->str
a=10.8
print(str(a)) #'10.8'
#float → bool
a=10.8
print(bool(a)) #True
#float->list
list(10.8) #gives type error
#float->tuple
tuple(10.8) #gives type error
#str->int
a="25"
print(int(a)) #25
#str → float
a="25.5"
print(float(a)) #25.5
#str->bool
a="25"
print(bool(a)) #True
#str->list
a="Python"
print(list(a)) #['P','y','t','h','o','n']
#str->tuple
a="Python"
print(tuple(a))#('P','y','t','h','o','n')
#bool->int
print(int(True)) #1
print(int(False)) #0
#bool->float
print(float(True)) #1.0
#bool->str
print(str(True)) #'True'
#bool->list
list(True)#TyprError
#bool->tuple
tuple(True)#TyprError
#list->tuple
a=[1,2,3]
print(tuple(a)) #(1,2,3)
#lisr->str
a=[1,2,3]
print(str(a)) #'(1,2,3)'
#tuple->list
a=(1,2,3)
print(list(a)) #[1,2,3]
#tuple->str
a=(1,2,3)
print(str(a)) #'[1,2,3]'