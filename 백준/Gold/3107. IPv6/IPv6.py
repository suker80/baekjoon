ip = input()

ip.count('')
if ip.count('::') == 0:
    ip_split = ip.split(':')
    for i in range(8):
        ip_split[i] = ('0000' + ip_split[i])[-4:]
else:
    ip_split = ip.split(':')

    count = 0
    for s in ip_split:
        if s:
            count += 1

    for i in range(len(ip_split)):
        if not ip_split[i]:
            ip_split = ip_split[:i] + ['0000'] * (8 - count) + ip_split[i+1:]
            break
    ip_split = [ip for ip in ip_split if ip]
    for i in range(8):
        ip_split[i] = ('0000' + ip_split[i])[-4:]

print(':'.join(ip_split))
