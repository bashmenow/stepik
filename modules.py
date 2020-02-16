import datetime
text = str(input().replace('-', ' '))
days = int(input())
current = datetime.datetime.strptime(text, '%Y %m %d')
newdate = (current + datetime.timedelta(days)).strftime('%Y %-m %-d')
print(newdate)
