#!/usr/bin/env python3

from matplotlib import pyplot as plt
import shelve

def makeBarChart():
    shelvef = shelve.open("access.s")
    ip_ls = [(val, key) for key, val in shelvef.items()]
    ip_ls.sort()
    ips = [i[1] for i in ip_ls]
    bytes_sent = [i[0] for i in ip_ls]
    plt.bar(ips, bytes_sent)
    plt.xlabel('IPs')
    plt.ylabel('Bytes')
    plt.title('Bytes Sent Graph')
    plt.xticks(rotation=45 ,fontsize=8) 
    plt.savefig('log_plot.png') 

if __name__ == "__main__":
    makeBarChart()