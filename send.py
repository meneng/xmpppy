import sys, os, xmpp

msg = "Hello World!"
jid = "pengguna@domain.tld"
pwd = "rahasia"

recipient = "tujuan@domain.tld"
jid = xmpp.protocol.JID(jid)
cl = xmpp.Client(jid.getDomain(), debug = [])

if cl.connect() == "":
    print("Tidak terkoneksi")
    sys.exit(0)

if cl.auth(jid.getNode(), pwd) == None:
    print("Otentikasi gagal")
    sys.exit(0)

cl.send(xmpp.protocol.Message(recipient, msg))

cl.disconnect()
