import json

data = '''
[General Information]
-------------------
[Hostname]: Jakobs-MBP.home
[OS Version]: 14.0
[Kernel Version]: Darwin Jakobs-MBP.home 23.0.0 Darwin Kernel Version 23.0.0: Fri Sep 15 14:42:57 PDT 2023; root:xnu-10002.1.13~1/RELEASE_ARM64_T8112 arm64


[Hardware Information]
-------------------
[CPU Information]: Apple M2
[Memory (RAM)]: 8 GB
[Disk Usage]: 12Gi | 5%
[GPU Information]:       Chipset Model: Apple M2


[Load and Performance]
-------------------
[CPU Usage]: 17.7%
[Memory Usage]: 7.34961 MB
[Network Information]:
Sent - 245409478 | Received - 10073248
Sent - 245409478 | Received - 10073248
Sent - 245409478 | Received - 10073248


[Network Configuration]
-------------------
[IP Addresses]: 10.110.1.106
[Network Interfaces]: Port:
en3
Address:
en7
Address:
Port:
en4
Address:
bridge0
Address:
en0
Address:
en1
Address:
en2
Address:
[Routing Table]: Routing tables

Internet:
Destination        Gateway            Flags               Netif Expire
default            10.110.1.1         UGScg                 en0       
10.110.1/24        link#13            UCS                   en0      !
10.110.1.1/32      link#13            UCS                   en0      !
10.110.1.1         58:ef:68:58:68:20  UHLWIir               en0   1199
10.110.1.106/32    link#13            UCS                   en0      !
10.110.1.255       ff:ff:ff:ff:ff:ff  UHLWbI                en0      !
127                127.0.0.1          UCS                   lo0       
127.0.0.1          127.0.0.1          UH                    lo0       
169.254            link#13            UCS                   en0      !
169.254.169.254    link#13            UHLSW                 en0      !
224.0.0/4          link#13            UmCS                  en0      !
224.0.0.251        1:0:5e:0:0:fb      UHmLWI                en0       
239.255.255.250    1:0:5e:7f:ff:fa    UHmLWI                en0       
255.255.255.255/32 link#13            UCS                   en0      !

Internet6:
Destination                             Gateway                                 Flags               Netif Expire
default                                 fe80::%utun0                            UGcIg               utun0       
default                                 fe80::%utun1                            UGcIg               utun1       
default                                 fe80::%utun2                            UGcIg               utun2       
default                                 fe80::%utun3                            UGcIg               utun3       
default                                 fe80::%utun4                            UGcIg               utun4       
::1                                     ::1                                     UHL                   lo0       
fe80::%lo0/64                           fe80::1%lo0                             UcI                   lo0       
fe80::1%lo0                             link#1                                  UHLI                  lo0       
fe80::%ap1/64                           link#12                                 UCI                   ap1       
fe80::bc3e:53ff:fe8f:e00d%ap1           be:3e:53:8f:e0:d                        UHLI                  lo0       
fe80::%en0/64                           link#13                                 UCI                   en0       
fe80::802:8e91:9d75:d7d7%en0            82:47:2f:d3:3:af                        UHLWIi                en0       
fe80::1012:95fb:c33d:89c9%en0           9c:3e:53:8f:e0:d                        UHLI                  lo0       
fe80::d0b7:1fff:fef6:c9cc%awdl0         d2:b7:1f:f6:c9:cc                       UHLI                  lo0       
fe80::d0b7:1fff:fef6:c9cc%llw0          d2:b7:1f:f6:c9:cc                       UHLI                  lo0       
fe80::%utun0/64                         fe80::e5b5:8aff:3fa0:2057%utun0         UcI                 utun0       
fe80::e5b5:8aff:3fa0:2057%utun0         link#16                                 UHLI                  lo0       
fe80::%utun1/64                         fe80::ab9f:6ef:5eab:7397%utun1          UcI                 utun1       
fe80::ab9f:6ef:5eab:7397%utun1          link#17                                 UHLI                  lo0       
fe80::%utun2/64                         fe80::ce81:b1c:bd2c:69e%utun2           UcI                 utun2       
fe80::ce81:b1c:bd2c:69e%utun2           link#18                                 UHLI                  lo0       
fe80::%utun3/64                         fe80::92d5:d17a:444d:d284%utun3         UcI                 utun3       
fe80::92d5:d17a:444d:d284%utun3         link#19                                 UHLI                  lo0       
fe80::%utun4/64                         fe80::811f:3abc:9a2c:1e56%utun4         UcI                 utun4       
fe80::811f:3abc:9a2c:1e56%utun4         link#20                                 UHLI                  lo0       
ff00::/8                                ::1                                     UmCI                  lo0       
ff00::/8                                link#12                                 UmCI                  ap1       
ff00::/8                                link#13                                 UmCI                  en0       
ff00::/8                                link#14                                 UmCI                awdl0       
ff00::/8                                link#15                                 UmCI                 llw0       
ff00::/8                                fe80::e5b5:8aff:3fa0:2057%utun0         UmCI                utun0       
ff00::/8                                fe80::ab9f:6ef:5eab:7397%utun1          UmCI                utun1       
ff00::/8                                fe80::ce81:b1c:bd2c:69e%utun2           UmCI                utun2       
ff00::/8                                fe80::92d5:d17a:444d:d284%utun3         UmCI                utun3       
ff00::/8                                fe80::811f:3abc:9a2c:1e56%utun4         UmCI                utun4       
ff01::%lo0/32                           ::1                                     UmCI                  lo0       
ff01::%ap1/32                           link#12                                 UmCI                  ap1       
ff01::%en0/32                           link#13                                 UmCI                  en0       
ff01::%utun0/32                         fe80::e5b5:8aff:3fa0:2057%utun0         UmCI                utun0       
ff01::%utun1/32                         fe80::ab9f:6ef:5eab:7397%utun1          UmCI                utun1       
ff01::%utun2/32                         fe80::ce81:b1c:bd2c:69e%utun2           UmCI                utun2       
ff01::%utun3/32                         fe80::92d5:d17a:444d:d284%utun3         UmCI                utun3       
ff01::%utun4/32                         fe80::811f:3abc:9a2c:1e56%utun4         UmCI                utun4       
'''

def read_log_file(file_path='/Users/jbalkovec/Desktop/Projects/System/bash/system_info_macos.log'):
  with open(file_path, 'r') as f:
    data = f.read()
  return data

def parse_data(data):
  sections = data.split('\n\n')
  parsed_data = {}
  
  for section in sections:
    lines = section.strip().split('\n')
    section_name = lines[0].strip('[]')
    section_data = {}
    
    for line in lines[2:]:
      if ':' in line:
        key, value = map(str.strip, line.split(':', 1))
        section_data[key] = value
    
    parsed_data[section_name] = section_data
  
  return parsed_data

def write_parsed_to_file(data, out_file_path='/Users/jbalkovec/Desktop/Projects/System/python/output.json'):
  with open(out_file_path, 'w') as f:
    f.write(data)
    
file_data = read_log_file()

parsed_data = parse_data(file_data)
json_data = json.dumps(parsed_data, indent=4)
write_parsed_to_file(json_data)



