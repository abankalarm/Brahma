from color import *
import time
# this is for automation of the process of recon 
import argparse
import sys 
from multiprocessing import Process
import os

  
def amass(domain): 
    print("running amass")
    start = time.time() 
    cmd1 = "sudo amass enum -d {} -o sub_amass_{}".format(domain,domain)
    """ 
    run amass
    """
    time.sleep(5)
    os.system(cmd1)
    end = time.time() 
    print("finished amass in", end - start)
    
  
def subfinder(domain): 
    print("starting subfinder")
    start = time.time() 
    cmd2 = "subfinder -d {} -o sub_subfinder_{}".format(domain,domain)
    """ 
    run subfinder
    """
    time.sleep(5)
    os.system(cmd2)
    end = time.time()
    print("finished subfinder in", end - start)

def github_domain(domain): 
    print("starting github domain")
    start = time.time() 
    cmd2 = "python3 github_domain -d {0} YOUR SETTINGS HERE".format(domain)
    """ 
    run git dom
    """
    os.system(cmd2)
    end = time.time()
    print("finished git dom in", end - start)   

def nuclei(domain): 
    print("starting nuclei with all templates")
    start = time.time() 
    cmd2 = "nuclei -l domains_{} -t templates/ -o {}_nessus".format(domain,domain)
    """ 
    run git dom
    """
    os.system(cmd2)
    end = time.time()
    print("finished git dom in", end - start)   

def proof(x, outfile):
    for i in range(0,200000):
        print(x, i,'hello world', outfile)

def workers(domain,x):
    if (x==0):
        amass(domain)
    if (x==1):
        subfinder(domain)
    if (x==2):
        github_domain(domain)

if __name__ == '__main__': 
    
    # keeping all required tools in the same folder
    
    # first we input the domain to be reconned
    parser = argparse.ArgumentParser(description='starting')
    parser.add_argument("a", nargs='?', default="check_string_for_empty")
    #parser.add_argument("-l", "--level", type=int, help="increase level", default="2")
    parser.add_argument("-r", "--rain", action="store_true", default=False, help="Do you want to brute force for default passwords?")
    parser.add_argument("-n", "--nuclei", help="do you want to run nuclei as well with all templates", action="store_true",default=False)
    parser.add_argument("-j", "--js", help="scan js",action="store_true", default=False)
    parser.add_argument("-e", "--enumerate", help="scan for subdomains",action="store_true", default=False)
    args = parser.parse_args()

    if args.a == 'check_string_for_empty':
        print(Base.FAIL,r"""\

▀█████████▄     ▄████████    ▄████████    ▄█    █▄      ▄▄▄▄███▄▄▄▄      ▄████████ 
  ███    ███   ███    ███   ███    ███   ███    ███   ▄██▀▀▀███▀▀▀██▄   ███    ███ 
  ███    ███   ███    ███   ███    ███   ███    ███   ███   ███   ███   ███    ███ 
 ▄███▄▄▄██▀   ▄███▄▄▄▄██▀   ███    ███  ▄███▄▄▄▄███▄▄ ███   ███   ███   ███    ███ 
▀▀███▀▀▀██▄  ▀▀███▀▀▀▀▀   ▀███████████ ▀▀███▀▀▀▀███▀  ███   ███   ███ ▀███████████ 
  ███    ██▄ ▀███████████   ███    ███   ███    ███   ███   ███   ███   ███    ███ 
  ███    ███   ███    ███   ███    ███   ███    ███   ███   ███   ███   ███    ███ 
▄█████████▀    ███    ███   ███    █▀    ███    █▀     ▀█   ███   █▀    ███    █▀  
               ███    ███                                         by abankalarm
            """, Base.END)
        print('I can tell that no argument was given and I cant deal with that here.')
        print('supply domain as arguement')
        #print('Level - 1          only amass')
        print('please mention -e or --enumerate to enumerate subdomains for the domain supplied')
        #print('Level - 2(default) amass as well as subfinder')
        #print('Level - 3(beta)    github domain scanner')
        print('please mention -n or --nuclei to run nuclei as well')
        print('please mention -r or --rain to brute force results as well')
        print('please mention -j or --js to scan js files for furted subdomains')
        sys.exit("no domain :(")
    print("we are in buisness, running your settings")
    domain = args.a
    print("scan inline?",args.js)
    if args.enumerate == True:
        NUM_THREADS = 2 #removed level option
        process_list = []
        for x in range(NUM_THREADS):
            try:
                print ("trying thread"+str(x+1)) 
                p = Process(target=workers, args =(domain,x)) 
                p.start()
                process_list.append(p)
            except:
                raise
                print("Error: unable to start thread", x)

        # wait for processes to finish
        for process in process_list:
            process.join()
        
        # both threads completely executed 
        print("subdomains enumerated!, joining files now") 
        cmd_join = "sort -u sub_amass_{} sub_subfinder_{} > domains_{}".format(domain,domain,domain)
        os.system(cmd_join)
        print("combined and saved with domains_site")
    else:
        cmd_join = "echo {} > domains_{}".format(domain,domain)
        os.system(cmd_join)

    if (args.js != False):
        print("running a scan on these for even more -!!!these arent passed ahead!!!")
        cmd_aizer = "python3 SubDomainizer/SubDomainizer.py -l domains_{} -o advanced_{}.txt".format(domain,domain)
        os.system(cmd_aizer)

    if (args.nuclei != False):
        nuclei(domain)

    print("starting port scan now")
    print(os.getcwd())
    cmd_resolve = "sudo bash dnsmasscan.sh domains_{} dns_{}.xml -p1-65535 --rate 1800 -oG scan_{}.xml".format(domain,domain,domain)
    os.system(cmd_resolve)

    if (args.rain == True):
        print("proceeding to bruteforce for default creds")
        cmd_brute = "python3 brutespray/brutespray.py --file scan_{}.xml".format(domain)
        os.system(cmd_brute)

