import sys,os;

kilobytes = 1024;
megabytes = kilobytes*1024;
chunksize = int(10*megabytes);

def split(fromfile,todir,chunksize=chunksize):
    
    if not os.path.exists(todir):
        os.mkdir(todir)
    '''    
    else:
        for fname in os.listdir(todir):
            os.remove(os.path.join(todir,fname))
    '''
    srcFileName, ext=os.path.splitext(fromfile) 
    srcFileName = srcFileName.split('\\')[-1]
    partnum = 0
    inputfile = open(fromfile,"rb")
    while True:
        chunk = inputfile.read(chunksize)
        if not chunk:
            inputfile.close()
            break
        partnum += 1
        filename = os.path.join(todir, srcFileName+("cut%04d"%partnum)+ext)
        print("我要显示的文件名称："+filename)
        fileobj = open(filename, "wb")
        fileobj.write(chunk)
        fileobj.close()
    return partnum

if __name__=="__main__":

    fromfile = "D:\\test\\1\\123.flv"
    
    todir = "D:\\test\\2"
    
    #chunksize = int(5000000)
    
    absfrom,absto = map(os.path.abspath,[fromfile,todir])
    
    print('分割：',absfrom,'to',absto,'by',chunksize)

    try:
    
        parts = split(fromfile,todir,chunksize)
    
    except:
        print('Error during split:')
        print(sys.exc_info()[0],sys.exc_info()[1])
    else:
        print('分割完成:',parts,'parts are in',absto)

