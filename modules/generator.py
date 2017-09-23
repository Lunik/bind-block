import random
import string

def string (N):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

def blacklistZone (domains, database):
	text = ""

	for domain in domains:
		text += "zone \"{domain}\" {obr}type master; file \"{database}\";{cbr};\n".format(
				obr="{",
				cbr="}",
				domain=domain,
				database=database)

	return text

def dnsDB (ipv4, ipv6):
	return  """
$TTL    3600
@       IN      SOA     ns.banana basynga.banana (
                            2014052101         ; Serial
                                  7200         ; Refresh
                                   120         ; Retry
                               2419200         ; Expire
                                  3600)        ; Default TTL
;
                A       {ipv4} ; Redirect all domains
*       IN      A       {ipv4} ; Redirect all subdomains
                AAAA    {ipv6} ; Same for IPv6
*       IN      AAAA    {ipv6} ; Same for IPv6
""".format(ipv4=ipv4, ipv6=ipv6)
