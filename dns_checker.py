import dns.resolver
import whois
import sys

#file with hostnames
hostFile = "dns_file.txt"

#read sys.argv
arg=sys.argv


#convert txt file to array
def toArray(file):
  f = open("dns_file.txt", "r")
  arr = [fileLine.strip() for fileLine in f]
  f.close()
  return arr

hostnames = toArray(hostFile)

def getMX():
  for i in range(len(hostnames)):
    try:
      answer = dns.resolver.query(hostnames[i],'MX')
      print ("=============================================================")
      print ("Hostname: {0}".format(hostnames[i]))
      for rdata in answer:
        print ("MX record: {0} has preference(priority): {1}".format(rdata.exchange,rdata.preference))
    except dns.resolver.NoAnswer:
         print ("=============================================================")
         print ("Hostname {0} doesn\'t contain MX record(s)".format(hostnames[i]))


def getA():
  for i in range(len(hostnames)):
    try:
      answer = dns.resolver.query(hostnames[i],'A')
      print ("=============================================================")
      print ("Hostname: {0}".format(hostnames[i]))
      for rdata in answer:
        print ("A record(IPv4): {0}".format(rdata.to_text()))
    except dns.resolver.NoAnswer:
         print ("=============================================================")
         print ("Hostname {0} doesn\'t contain A record(s)".format(hostnames[i]))


def getAAAA():
   for i in range(len(hostnames)):
     try:
       answer = dns.resolver.query(hostnames[i],'AAAA')
       print ("=============================================================")
       print ("Hostname: {0}".format(hostnames[i]))
       for rdata in answer:
         print ("AAAA record(IPv6): {0}".format(rdata.to_text()))
     except dns.resolver.NoAnswer:
         print ("=============================================================")
         print ("Hostname {0} doesn\'t contain AAAA record(s)".format(hostnames[i]))


def getCNAME():
  for i in range(len(hostnames)):
    try:
      answer = dns.resolver.query(hostnames[i],'CNAME')
      print ("=============================================================")
      print ("Hostname: {0}".format(hostnames[i]))
      for rdata in answer:
        print ("CNAME record: {0}".format(rdata.target))
    except dns.resolver.NoAnswer:
        print ("=============================================================")
        print ("Hostname {0} doesn\'t contain CNAME record(s)".format(hostnames[i]))


def getNS():
  for i in range(len(hostnames)):
    try:
      answer = dns.resolver.query(hostnames[i],'NS')
      print ("=============================================================")
      print ("Hostname: {0}".format(hostnames[i]))
      for rdata in answer:
        print ("NS record: {0}".format(rdata.target))
    except dns.resolver.NoAnswer:
        print ("=============================================================")
        print ("Hostname {0} doesn\'t contain NS record(s)".format(hostnames[i]))

def getTXT():
  for i in range(len(hostnames)):
    try:
      answer = dns.resolver.query(hostnames[i],'TXT')
      print ("=============================================================")
      print ("Hostname: {0}".format(hostnames[i]))
      for rdata in answer:
        print ("TXT record: {0}".format(rdata.to_text()))
    except dns.resolver.NoAnswer:
        print ("=============================================================")
        print ("Hostname {0} doesn\'t contain TXT record(s)".format(hostnames[i]))


def getSOA():
  for i in range(len(hostnames)):
    try:
      answer = dns.resolver.query(hostnames[i],'SOA')
      print ("=============================================================")
      print ("Hostname: {0}".format(hostnames[i]))
      for rdata in answer:
        print ("SOA record: {0}".format(rdata.to_text()))
    except dns.resolver.NoAnswer:
        print ("=============================================================")
        print ("Hostname {0} doesn\'t contain SOA record(s)".format(hostnames[i]))


def getPTR():
  for i in range(len(hostnames)):
    try:
      answer = dns.resolver.query(hostnames[i],'PTR')
      print ("=============================================================")
      print ("Hostname: {0}".format(hostnames[i]))
      for rdata in answer:
        print ("PTR record: {0}".format(rdata.to_text()))
    except dns.resolver.NoAnswer:
        print ("=============================================================")
        print ("Hostname {0} doesn\'t contain PTR record(s)".format(hostnames[i]))


def is_registered(hostname):
  """
  This function that returns a boolean value
  if a `domain_name` is registered
  """
  try:
    w = whois.whois(hostname)
  except Exception:
    print ("This domain {0} isn\'t registered".format(hostname))
    return False
  else:
    return bool(w.domain_name)


def domainStatus():
#check if domain is registered
  for i in range(len(hostnames)):
    if is_registered(hostnames[i]) == True:
      print ("=============================================================")
      print ("This domain {0} is registered".format(hostnames[i]))
      w = whois.whois(hostnames[i]).status
      print("Status of this domain:{0}".format(w))
    else:
      print ("=============================================================")
      print ("This domain {0} is not registered".format(hostnames[i]))


def getRegistrar():
#check if domain is registered
  for i in range(len(hostnames)):
    if is_registered(hostnames[i]) == True:
      print ("=============================================================")
      print ("This domain {0} is registered".format(hostnames[i]))
      w = whois.whois(hostnames[i]).registrar
      print("Registrar of this domain:{0}".format(w))
    else:
      print ("=============================================================")
      print ("This domain {0} is not registered".format(hostnames[i]))


def getDate():
#check if domain is registered
  for i in range(len(hostnames)):
    if is_registered(hostnames[i]) == True:
      print ("=============================================================")
      print ("This domain {0} is registered".format(hostnames[i]))
      w_update = whois.whois(hostnames[i]).updated_date
      w_creation = whois.whois(hostnames[i]).creation_date
      w_expiration = whois.whois(hostnames[i]).expiration_date
      print("Update date of this domain:{0}".format(w_update))
      print("Creation date of this domain:{0}".format(w_creation))
      print("Expiration date of this domain:{0}".format(w_expiration))
    else:
      print ("=============================================================")
      print ("This domain {0} is not registered".format(hostnames[i]))


def resolver():
  if len(arg) <= 1:
    print ("DNS record isn\'t found!")
  elif arg[1] == "MX" or arg[1] == "mx":
    getMX()
  elif arg[1] == "A" or arg[1] == "a":
    getA()
  elif arg[1] == "CNAME" or arg[1] == "cname":
    getCNAME()
  elif arg[1] == "AAAA" or arg[1] == "aaaa":
    getAAAA()
  elif arg[1] == "NS" or arg[1] == "ns":
    getNS()
  elif arg[1] == "TXT" or arg[1] == "txt":
    getTXT()
  elif arg[1] == "SOA" or arg[1] == "soa":
    getSOA()
  elif arg[1] == "PTR" or arg[1] == "ptr":
    getPTR()
  elif arg[1] == "STATUS" or arg[1] == "status":
    domainStatus()
  elif arg[1] == "REG" or arg[1] == "reg":
    getRegistrar()
  elif arg[1] == "DATE" or arg[1] == "date":
    getDate()
  else:
    print ("You have entered incorrect DNS-record")

if __name__ == "__main__":
  resolver()
