# bind-block
For Bind9

Parse DNS query log and allow you to block futur query for a domain

## Usage
```
Usage: bindblock [options]

Options:
  -h, --help            show this help message and exit
  -p LOGPATH, --logpath=LOGPATH
                        Path of the bind query logs
  -b BINDPATH, --bindpath=BINDPATH
                        Path of the bind confing folder
  --all                 Block all domain
  -z ZONESPATH, --zonespath=ZONESPATH
                        Path of the blacklist zone
  -4 IPV4, --ip4=IPV4   IPv4 that is going to replace all dns entries
  -6 IPV6, --ip6=IPV6   IPv6 that is going to replace all dns entries
``