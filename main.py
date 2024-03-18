

hotfile="./hot.csv"

def gethotdata(name):
    data={}
    with open(name,"r")as f:
        datas=f.readlines()[1:]
        for line in datas:
            item=line.split(",")
            data[item[0]]=int(item[1].strip())
    return data

def utilizehot(data:dict):
    hotdatas=list(data.values())
    datasum=sum(hotdatas)
    datalen=len(hotdatas)
    
    newdata={}
    
    for item in data:
        newdata[item]=data[item]*datalen/datasum
        
    newdatas=list(newdata.values())
    datasum=sum(newdatas)
    assert(round(datasum)==datalen)
        
    return newdata


AVERAGE=29/22

def getfinalprice(data:list, average:int):
    newdatas={}
    
    for item in data:
        newdatas[item]=round(data[item]*average+0.005,2)
        
    return newdatas


def writeresult(data:dict,outputfile):
    with open(outputfile,"w")as f:
        for item in data:
            f.write(item+","+str(data[item])+"\n")
            
      
if __name__=="__main__":      
    data=gethotdata(hotfile)
    print(data)
    newdata=utilizehot(data)
    print(newdata)

    finalprices=getfinalprice(newdata,average=AVERAGE)
    print(finalprices)
    writeresult(finalprices,"price.csv")
