file_obj=open("server_data.txt",'r')
file_write=open("server_data_out.txt","w+")
# print file_obj
array=[0]*86400
def_day=29
def_hr=23
def_min=53
def_sec=25
def_second1s=23*3600+(53*60)+(25)
for line in file_obj:
    line=line.split('[')
    line=line[1]
    line=line.split(']')
    line=line[0]
    line=line.split(':')
    day=(int)(line[0])
    hr=(int)(line[1])
    if day>def_day:
        hr=hr+24
    
    minute=(int)(line[2])
    sec=(int)(line[3])
    def_seconds2=hr*3600+(minute*60)+(sec)
    index=def_seconds2-def_second1s
    # print index
    array[index]=array[index]+1
    # file_write.write( str(day)+str(hr)+str(minute)+str(sec)+"   ")
    # file_write.write( str(index)+"   "+str(array[index])+"\n")
for element in array:
    file_write.write( str(element)+"\n")
file_write.close()
file_write=open("server_data_out.txt","r")

print file_write
for line1 in file_write:
    print str(line1)