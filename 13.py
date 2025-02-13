from ipaddress import *
for mask in range(30,1,-1):
    ip='203.75.227.102'
    net = ip_network(f'{ip}/{mask}',0)
    if str(net)==f'203.75.224.0/{mask}':
        print(net, '1'* mask + '0'*(32-mask))
