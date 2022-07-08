import re

address = "78 Hi l1 89 Main, 4th Cross, 123, Road, Marathalli, 5678 Bangalore,56002367893"


add_nos = re.findall(R'\d', address)
print(f'sorting the only nums from address{add_nos}')

add_nos1 = re.findall(R'\d+', address)
print(f'sorting the only nums from address{add_nos1}')

add_dig = re.findall(r'\d{2}',address)
print(f'sorting the only nums from address{add_dig}')

add_dig1 = re.findall(r'\d{1,6}',address)
print(f'sorting the only nums from address{add_dig1}')

s ='''
<html>
<head>
</head>
<body>
IP Address are 172.45.78.189
LoopBack Address: 127.0.0.1
Computer 1: 10.67.89.101
Computer 2: 11.67.98.102
Computer 3: 12.68.98.102
</body>
</html>
'''
ip1 = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',s)
print(f"'ip's are : {ip1}")
d = " ip's are: 10.67.89.101 , 12.68.98.102"


ip = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',d)
print(f"'ip's are : {ip}")

pincode = re.findall(r'\d{11}',address)
print(f" pincode:{pincode}")

ip_s1 = re.findall(r'1[0-1]\.\d{1,3}\.\d{1,3}\.\d{1,3}',s)
print(f'ip address',ip_s1)

ip_s2 = re.findall(r'1[0|1].\d{1,3}.\d{1,3}.\d{1,3}',s)
print(f'ip address {ip_s2}')

ip_s3 = re.findall(r'10.\d{1,3}.\d{1,3}.\d{1,3}',s)
print(f' ip address: {ip_s3}')


e = "purple alice@google.com     abcde helloab@adc.com"
emails = re.findall(r'[A-Za-z]+@\w+\.\w+',e)
print(emails)

target_string = 'Emma is a python developer and also knows ML and AI'
result = re.search(r'\w{2}$',target_string)
print(result.group())

result1 = re.search(r'^\w{4}',target_string)
print(result1.group())

result3 = re.search('a',target_string)
print(f'type is object {result3}')

r =re.split(" ",target_string)
print(r)

r1 = re.split("e",target_string)
print(r1)

r2 = re.sub("e","E",target_string)
print(r2)


