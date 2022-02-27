import csv,time



cycle=200
def put1 (a):
    aa="PDATA.csv"
    with open(aa,mode='w',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerow(a) 
        csvfile.close()
        
def put2 (a):
    aa="VDATA.csv"
    with open(aa,mode='w',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerow(a) 
        csvfile.close()

    
while True:
    with open("RAWDATA.csv",mode='r') as csvfile :     #feeding each values to csv
        data=list(csv.reader(csvfile))
        
    l=len(data)
    xx=[]
    yy=[]
    for a in range (0,cycle):
        xx.append(data[l-cycle+a][0])
        yy.append(data[l-cycle+a][1])
        
      
    put1(xx)
    put2(yy)
    time.sleep(0.01)  
  