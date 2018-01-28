import sys,os

def joinfile(fromdir,filename,todir):

if not os.path.exists(todir):

os.mkdir(todir)

if not os.path.exists(fromdir):

print("合拼文件路径错误！")



outfile = open(os.path.join(todir,filename),"wb")

files = os.listdir(fromdir)

files.sort()

for file in files:

filepath = os.path.join(fromdir,file)

infile = open(filepath,"rb")

data = infile.read()

outfile.write(data)

infile.close()



outfile.close()





if __name__=="__main__":

fromdir = "F:\\split_parts\\"

todir = "F:\\split_parts\\"

filename = "abc.mp4"



try:

joinfile(fromdir,filename,todir)

except:

print("错误的连接文件：")

print(sys.exc_info()[0],sys.exc_info()[1])