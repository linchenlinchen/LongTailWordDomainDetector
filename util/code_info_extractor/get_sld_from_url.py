def get_sld(url):
    special = {"com.cn", "net.cn", "net.com", 'gov.cn'}
    i = url
    if len(i.split("/")[2].split(".")) == 2:
        return i.split("/")[2]
    elif len(i.split("/")[2].split(".")) >= 3 and '.'.join(i.split("/")[2].split(".")[-2:]) not in special:
        return '.'.join(i.split("/")[2].split(".")[-2:])
    elif len(i.split("/")[2].split(".")) >= 3:
        return '.'.join(i.split("/")[2].split(".")[-3:])
    else:
        return i
def test():
    s = {}
    special = {"com.cn","net.cn","net.com",'gov.cn'}
    l = set()
    for i in s:
        if len(i.split("/")[2].split(".")) == 2:
            l.add(i.split("/")[2])
        elif len(i.split("/")[2].split(".")) >= 3 and '.'.join(i.split("/")[2].split(".")[-2:]) not in special:
            l.add('.'.join(i.split("/")[2].split(".")[-2:]))
        elif len(i.split("/")[2].split(".")) >= 3:
            l.add('.'.join(i.split("/")[2].split(".")[-3:]))
        else:
            l.add(i)
    print(l)