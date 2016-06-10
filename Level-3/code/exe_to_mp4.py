
f=open('..\\input\\exe.mp4','rb')
target=[open('..\\output\\other1.mp4','wb')
        ,open('..\\output\\other2.mp4','wb')
        ,open('..\\output\\other3.mp4','wb')
        ,open('..\\output\\other4.mp4','wb')
        ,open('..\\output\\other5.mp4','wb')
        ,open('..\\output\\other6.mp4','wb')
        ,open('..\\output\\other7.mp4','wb')
        ,open('..\\output\\other8.mp4','wb')
        ,open('..\\output\\other9.mp4','wb')
        ,open('..\\output\\other10.mp4','wb')
        ,open('..\\output\\other11.mp4','wb')
        ,open('..\\output\\other12.mp4','wb')
        ,open('..\\output\\other13.mp4','wb')
        ,open('..\\output\\other14.mp4','wb')
        ,open('..\\output\\other15.mp4','wb')
        ,open('..\\output\\other16.mp4','wb')
        ,open('..\\output\\other17.mp4','wb')
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


