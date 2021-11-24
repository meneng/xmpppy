import sys
import os
import xmpp
import signal
import time

def messageCB(conn, msg):
    print("Pengirim: \t" + str(msg.getFrom()))
    print("Isi: \t" + str(msg.getBody()))
    print(msg)

def stepOn(conn):
    try:
        conn.Process(1)
    except KeyboardInterrupt:
        return 0
    return 1

def goOn(conn):
    while stepOn(conn):
        pass

def main():
    jid = "pengguna@domain.tld"
    pwd = "rahasia"
    
    jid = xmpp.protocol.JID(jid)
    
    cl = xmpp.Client(jid.getDomain(), debug = [])
    if cl.connect() == "":
        print("Tidak terkoneksi")
        sys.exit(0)
    if cl.auth(jid.getNode(), pwd) == None:
        print("Otentikasi gagal")
        sys.exit(0)
    cl.RegisterHandler('message', messageCB)
    cl.sendInitPresence()
    goOn(cl)

main()
