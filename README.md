# Brahma (for linux only, can easily be modified for windows tho)
This my own built from scratch automation recon framework.

## heres the work flow 

I am quiet impatient so i like threading - feel free to modify this and push commits 

1. You put a base website, example razer.com, you can enumerate for subdomains using -e
2. This gets divided into two threads- one of amass and other subfinder which output files seperately ( subdomains lots of subdomains)
3. As soon as both these outputs are recieved. A simple script combines both to achieve a single file
### for those who run with -n or -nuclei
4. this output is sent to nuclei and output in txt form


5. A DNS resolver script converts the obtained subdomains into ip addresses and then inputs them into massscan
   After the mass scan result output
### for those who run this with -r or --rain 
6. brutespray takes these results and tries to brute force them for default credentials
### for those who run this with -j or --js 
7. Subdomainizer takes the sub domains obtained in step 3 and searches for more interesting secret inline ( inline secrets )


## things to be implemented - 
1. I have added option for github search but it hasnt been fully incorporated yet ( it will add extra thread so no time waste)
2. <s>I would join nucle as well with options to run template - a detailed output of all services run by every subdomain would be a nice addition</s>(implemented)
3. All dead websites will automatically be sent to try for subdomain takeover(tho less and less common now - but i would like to have a nice view at certs)

## bugs
1. Dead websites with no ip address, can mess up masscan results 

## REQUIREMENTS
1. i have created folders for the tools i am not using symlinks for, please download and place them in proper location
2. masscan
3. amass
4. subfinder



# note :
I am not a big believer of licenses, so feel free to use it any way you like - if you want even, go ahead and push your own modifications.

If you dont like what i am doing here, please move on
This tool is in no way supposed to hack for you, it helps you wield a very big gun in a much better way tho. 
how you use this is upto you, happy hacking
