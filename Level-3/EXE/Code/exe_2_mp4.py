
f=open('..\\input\\exe.mpfour','rb')
target=[open('..\\output\\other1.mp','wb')
        ,open('..\\output\\other2.mp','wb')
        ,open('..\\output\\other3.mp','wb')
        ,open('..\\output\\other4.mp','wb')
        ,open('..\\output\\other5.mp','wb')
        ,open('..\\output\\other6.mp','wb')
        ,open('..\\output\\other7.mp','wb')
        ,open('..\\output\\other8.mp','wb')
        ,open('..\\output\\other9.mp','wb')
        ,open('..\\output\\other10.mp','wb')
        ,open('..\\output\\other11.mp','wb')
        ,open('..\\output\\other12.mp','wb')
        ,open('..\\output\\other13.mp','wb')
        ,open('..\\output\\other14.mp','wb')
        ,open('..\\output\\other15.mp','wb')
        ,open('..\\output\\other16.mp','wb')
        ,open('..\\output\\other17.mp','wb')
        ]
pattern=list()
d=17
count=0
try:
        byte=f.read()
        lst=byte.split(b'\xFF'*98)
        for b in range(0, len(lst)):                                                                                                                                                                                                                                                                                                                        #        file.close()                                    
                target[count].write(lst[b])
                count+=1
                count%=d
finally:
    f.close()
    for i in range(17):
            target[i].close()


