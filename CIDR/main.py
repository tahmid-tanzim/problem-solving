from ipaddr import IPNetwork

if __name__ == '__main__':
    n1 = IPNetwork('10.0.0.0/16')
    n2 = IPNetwork('10.1.0.0/16')
    print('CIDR Overlap? - ', n1.overlaps(n2))
    print('CIDR Overlap? - ', n2.overlaps(n1))
