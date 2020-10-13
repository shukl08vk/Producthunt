from datetime import datetime
from datetime import date

#
# Complete the 'dateandtime' function below.
#
# The function accepts INTEGER val as parameter.
# The return type must be LIST.
#

def dateandtime(val,tup):
    # Write your code here
    a=[]
    if val is 1:
        a.append(date(tup[0],tup[1],tup[2]))
        a.append(datetime(tup[0],tup[1],tup[2]).strftime("%d/%m/%Y"))
    if val is 2:
        ac=date.fromtimestamp(tup[0])
        a.append(ac)
    if val is 3:
        a.append(time(tup[0],tup[1],tup[2]))
        a.append(datetime.time(tup[0],tup[1],tup[2]).strftime('%I'))
    if val is 4:
        ab=date(tup[0],tup[1],tup[2])
        a.append(ab.weekday())
        a.append(ab.strftime('%b'))
        a.append(ab.timetuple().tm_yday)
    if val is 5:
        a.append(datetime(tup[0],tup[1],tup[2],tup[3],tup[4],tup[5]))        
    
    return a 


    