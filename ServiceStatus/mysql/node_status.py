import sys
import os
import logging
import MySQLdb
import telnetlib,socket
import traceback
def is_host_availiable(ip):
    try:
        log="PING Host %s" % ip
        logging.info(log)
        #commond="(sleep 2 && echo 'gaohonglei' && sleep 1 && echo '123' && sleep 1) | " + "telnet " + str(ip) + " 2>/dev/null"
        commond="ping "+ ip +" -c 1 -W 1"
        result=os.popen(commond).readlines()
        if len(result) == 6:
            log="success ping %s" % (ip)
            logging.warning(log)
            return 1
        else:
            return 0
    except Exception,e:
        logging.error(e)
        log="faild ping %s" % (ip)
        logging.error(log)
        return 0
    
def is_port_availiable(ip,port):
    # log="telneting %s %s" % (ip,port)
    # logging.info(log)
    # commond="telnet " + str(ip) +' ' + str(port) + " 2>/dev/null"
    # result=os.popen(commond).readlines()
    fd = socket.socket()
    try:
        fd.connect((ip,port))
        logging.info("Success connect to {0}:{1}".format(ip, port))
        return 1
    except socket.error,ex:
        logging.error("Faild connect to {0}:{1}".format(ip,port))
        return 0

def is_mysqld_availiable(ip,port,user,passwd,var=""):
    try:
        conn=MySQLdb.connect(host=ip,port=int(port),user=user,passwd=passwd,)
        cur=conn.cursor()
        cur.execute("select version()")
        data=cur.fetchone()
        conn.close()
        logging.info("Success connect to MysqlServer {0}:{1}".format(ip, port))
        return 1
    except Exception,e:
        logging.info("Faild connect to MysqlServer {0}:{1}".format(ip, port))
        return 0
if __name__=="__main__":
    is_port_availiable("172.16.10.164",8000)



