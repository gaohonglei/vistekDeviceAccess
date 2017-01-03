import sys
import os
import logging,traceback
def remove_ip(fd,host,ip,start_pos):
    pass

def remove_host(filename,start_pos,host={}):
    if len(host) ==0:
        return 0
    string="Waiting remove hosts:\n"
    for k,v in host.items():
        string += k
        string +=":"
        for ip in v:
            string +=ip
            string += ";"
        string +="\n"
        logging.warning(string)
        string =""
    fd=open(filename,'r+')
    lines=fd.readlines()
    fd.close()
    lines_tmp=[]
    string=''
    for line in lines[0:start_pos]:
        string += line
    for line in lines[start_pos:]:
        lines_tmp.append(line)
        domain=line.strip("\n").split("\t")[0]
        for k,v in host.items():
            ip=line.strip("\n").split("\t")[3]
            if ip in v and domain==k:
                log="Removed %s ip:%s" % (domain,ip)
                logging.warning(log)
                lines_tmp.remove(line)
                break
    for line in lines_tmp:
        string +=line
    fd=open(filename,'w+')
    fd.write(string)
    logging.info("success remove faild host")
    fd.close()


def add_ip(fd,host,ip):
    pass

def add_host(filename,start_pos,host={}):
    if len(host) ==0:
        return 0
    string="Waiting recovery hosts:\n"
    for k,v in host.items():
        string += k
        string +=":"
        for ip in v:
            string +=ip
            string += ";"
        string +="\n"
        logging.warning(string)
    fd=open(filename,'a+')
    for k,v in host.items():
        for ip in v:
            fd.write(k+'\t'+"IN"+'\t'+"A"+'\t'+ip+'\n')
            log="Recoveried %s ip:%s" % (k,ip)
            logging.info(log)

    fd.close()

def restart_bind9():
    pass

def reload_bind9():
    logging.info("reloading bind9..........")
    result=os.popen('service bind9 reload').readlines()
    return 1
    # try:
    #     pos=result[1].find("done")
    #     if pos == -1:
    #         logging.error("Failed to load bind9......")
    #         return -1
    #     logging.warning("Success reload bind9")
    # except Exception,e:
    #     traceback.print_exc()
    #     return 0;
     
    
    
def reload_config_file(filename,host_dict,start_pos):
    fd=open(filename,'r')
    lines=fd.readlines()
    string=""
    for n in range(0,start_pos):
        string +=lines[n]
    fd.close()
    fd=open(filename,'w+')
    fd.write(string)
    for k,v in host_dict.items():
        if k=="global":continue
        domain=v["domain"]
        ips=v["ips"]
        ip_list=ips.split(";")
        for ip in ip_list:
            fd.write(domain+'\t'+"IN"+'\t'+"A"+'\t'+ip.split(":")[0]+'\n')
        
    fd.flush()
    fd.close()    
    reload_bind9()

