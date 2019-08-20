import requests


list_result = []
list1 = ['UCN-2003-09-18-2.html', 'UCN-2003-09-19.html', 'UCN-2003-09-22-1.txt', 'UCN-2003-09-23-1.txt', 'UCN-2003-09-23-2.txt', 'UCN-2003-09-23-3.txt', 'UCN-2003-09-23-4.txt', 'UCN-2003-09-23-5.txt']
for i in list1:
    list_result.append('http://www.ukcert.org.uk/repository/archive/db/%s' % i)

i= 0
for m in list_result:
    strm = list1[i]
    print(strm)
    html = requests.get(m)
    r = html.content
    with open(strm, 'wb') as f:
        f.write(r)
    i += 1
    print('%s/%s'%(i,len(list1)))

print("finished mission.")