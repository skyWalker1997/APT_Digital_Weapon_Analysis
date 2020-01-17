import pprint
from jsonmerge import merge


#
# list1 = [{'type': 'WH_MSGFILTER', 'method': 'SetWindowsHook', 'success': True}, {'type': 'WH_CBT', 'method': 'SetWindowsHook', 'success': True}]
# list2 = [{'type': 'WH_SHELL', 'method': 'SetWindowsHook', 'success': True}, {'type': 'WH_GETMESSAGE', 'method': 'SetWindowsHook', 'success': True}, {'type': 'WH_CBT', 'method': 'SetWindowsHook', 'success': True}, {'type': 'WH_KEYBOARD', 'method': 'SetWindowsHook', 'success': True}, {'type': 'WH_MOUSE', 'method': 'SetWindowsHook', 'success': True}]
# list_test = list2
#
# for element in list1:
#     if element not in list2:
#         list_test.append(element)
# print(list_test)
# print(len(list_test))

# [dict(t) for t in  set([tuple(d.items())  for  d  in  li])]


#  解释
# li 是原始列表
# d  是列表中的一个字典
# t  是从字典中创建的元组之一

dit = [{'url': 'http://www.iptrackeronline.com/', 'method': 'GET', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}, {'url': 'http://ip-api.com/json/', 'method': 'GET', 'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:48.0) Gecko/20100101 Firefox/48.0'}, {'url': 'http://www.iptrackeronline.com/', 'method': 'GET', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}, {'url': 'http://ip-api.com/json/', 'method': 'GET', 'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:48.0) Gecko/20100101 Firefox/48.0'}, {'url': 'http://www.iptrackeronline.com/', 'method': 'GET', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}, {'url': 'http://ip-api.com/json/', 'method': 'GET', 'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:48.0) Gecko/20100101 Firefox/48.0'}]




seen = set()
new_dit = []
for d in dit:
    t = tuple(d.items())
    if t not in seen:
        seen.add(t)
        new_dit.append(d)
print(new_dit)