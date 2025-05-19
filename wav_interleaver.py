import sys
import os
import argparse
import math
import subprocess

parser = argparse.ArgumentParser(usage="%(prog)s <folder> [options]")
parser.add_argument('folder', nargs='?',help="the folder where all the .WAV files are located. The final XA will take that folder's title as its' name.")
parser.add_argument('-f', '--frequency', nargs='?', default='37800', required=False, help='the frequency each individual XA, and the final interleaved one, will get')
parser.add_argument('-m', '--mode', nargs='?', default='1', required=False, help='the sector mode xainterleave will use. 0 for full raw sectors, 1 just for XA.')
parser.add_argument( '-o', '--overwrite', action=argparse.BooleanOptionalAction, help='If this option is used, we will overwrite pre-existing .wav files')


args = parser.parse_args()
print(args)


if (args.folder == None):
    parser.print_help()
    exit(1)




with open("interleave.txt", "w") as interleave_file:
    channel_count = 0
    xa_cur = ""

    with os.scandir(args.folder) as iterator:
        
        for entry in iterator:
            
            if entry.name.endswith('.wav'):
                print(entry.name)
                xa_cur = os.path.join(args.folder,str(channel_count) + ".xa")
                
                if args.overwrite or not (os.path.isfile(xa_cur)):
                    subprocess.check_call([os.path.join(os.getcwd(), 'psxavenc'), '-t', 'xa', '-f', args.frequency, entry.path, xa_cur], shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)
                else:
                    print("already exists, skipping")
                interleave_file.write(f"1 xa {xa_cur} 1 {channel_count} \n")
                channel_count += 1
                
    null_line = "1 null\n"
    
    while not math.sqrt(channel_count).is_integer:
        
        interleave_file.write(null_line)
        channel_count += 1
        
    interleave_file.truncate()
        
destination = os.path.basename(args.folder) + '.XA' 
print(destination)
subprocess.check_call([os.path.join(os.getcwd(), 'xainterleave'), args.mode, f"{os.path.join(os.getcwd(),'interleave.txt')}", destination ], shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)
        
        