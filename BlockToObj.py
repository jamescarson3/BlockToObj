# imports
import sys, os

# assign input filename and output directory
arguments = len(sys.argv) - 1
if arguments!=2:
    print("Format: python3 Block2Obj.py <input_filename> <output_foldername>")
    sys.exit(0)

input_filename=sys.argv[1]
output_foldername=sys.argv[2]

# open tab separated value file
f=open(input_filename,'r')

# read header and verify the correct number of columns and tab delimited
header=f.readline()
hs=header.split('\t')
if len(hs)!=12:
    print(header)
    print(hs)
    print(hs[0])
    print("Expecting input file with 12 tab delimited columns, got "+str(len(hs))+" i.e.:")
    print("CenterID	DonorID	OrganID	SuborganID	BlockID	Label	X	Y	Z	deltaX	deltaY	deltaZ")
    print("Aborting")
    sys.exit(0)

# move to output folder and create it if necessary
try:
    os.chdir(output_foldername)
except:
    os.mkdir(output_foldername)
    os.chdir(output_foldername)

# iterrate line by line in tsv file
l=f.readline()
if len(l)>0:
    not_done=1
else:
    not_done=0

while(not_done):
    # parse line by tabs
    lst=l.split('\t')

    # assign coordinate and delta variables
    x1,y1,z1,dx,dy,dz=float(lst[6]),float(lst[7]),float(lst[8]),float(lst[9]),float(lst[10]),float(lst[11])

    # calculate X2, Y2, Y3
    x2,y2,z2=x1+dx,y1+dy,z1+dz

    # generate output filename
    output_filename=lst[1]+'_'+lst[2]+'_'+lst[3]+'_'+lst[4]+'.obj'

    # open output file
    fout=open(output_filename,'w+')

    # write output header
    fout.write("# "+output_filename+"\n")
    fout.write("# Source: "+lst[0]+"\n")
    fout.write("# Label: "+lst[5]+"\n")
    fout.write("#\n\ng cube\n\n")
    
    # write vertices
    fout.write("v "+str(x1)+" "+str(y1)+" "+str(z1)+"\n")
    fout.write("v "+str(x1)+" "+str(y1)+" "+str(z2)+"\n")
    fout.write("v "+str(x1)+" "+str(y2)+" "+str(z1)+"\n")
    fout.write("v "+str(x1)+" "+str(y2)+" "+str(z2)+"\n")
    fout.write("v "+str(x2)+" "+str(y1)+" "+str(z1)+"\n")
    fout.write("v "+str(x2)+" "+str(y1)+" "+str(z2)+"\n")
    fout.write("v "+str(x2)+" "+str(y2)+" "+str(z1)+"\n")
    fout.write("v "+str(x2)+" "+str(y2)+" "+str(z2)+"\n\n")

    # write vn and f lines
    fout.write("vn  0.0  0.0  1.0\n")
    fout.write("vn  0.0  0.0  -1.0\n")
    fout.write("vn  0.0  1.0  0.0\n")
    fout.write("vn  0.0  -1.0  0.0\n")
    fout.write("vn  1.0  0.0  0.0\n")
    fout.write("vn  -0.0  0.0  0.0\n\n")

    fout.write("f  1//6 2//6 4//6 3//6\n")
    fout.write("f  1//2 3//2 7//2 5//2\n")
    fout.write("f  1//4 5//4 6//4 2//4\n")
    fout.write("f  8//5 7//5 5//5 6//5\n")  
    fout.write("f  8//1 6//1 2//1 4//1\n")
    fout.write("f  8//3 4//3 3//3 7//3\n")

    # close output file
    fout.close()

    # read line
    l=f.readline()
    if len(l)==0:
        not_done=0

# end program
f.close()
