import bluetooth
import time

def decode(msg):
    f = open('log.dat',  'a')
    lenght = len(msg)
    listMsg = list(msg)
    #msgWrds = enumerate(msg)
    if lenght > 6:
        lenWrd = ord(listMsg[0])
        chkWrd = ord(listMsg[1])
        stWrd  = ord(listMsg[2])
        hrtWrd = ord(listMsg[4])
        # Add the other words
        #print 'Hear rate: ' , int(hrtWrd, 16)
        print '[' , time.strftime('%X %x') , ']' , ' Hear rate: ' , hrtWrd
        f.write('[' + time.strftime('%X %x') + ']' + ' Hear rate: ' + str(hrtWrd) + '\n')
        #date = time.strftime('%X %x')
        #f.write(date + str(hrtWrd) )
        f.close()

bd_addr = "00:22:D0:02:D3:DB"
port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

#sock.send("hello!!")

print "connected.  type stuff"
while True:
    #inData = raw_input()
    #if len(inData) == 0: break
    #sock.send(inData)

    data = sock.recv(80)
    #print hex(int(data, base=16))
    #print 'lenght: ' , len(data)
    
    #for i,c in enumerate(data):
    #    print hex(ord(c))

    decode(data)
    
    #print " ".join("0x%s"%data[i:i+2] for i in range(0,len(data),2))
    #my_hex = data.decode('hex')
    #print my_hex
    #print data

    

sock.close()


       
    

