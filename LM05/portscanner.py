import nmap
begin = 50
end = 80

target = '127.0.0.1'

scanner = nmap.PortScanner()

for i in range(begin,end+1):
    res = scanner.scan(target,str(i))

    res = res['scan'][target]['tcp'][i]['state']

    print(f'port {i} is {res}')