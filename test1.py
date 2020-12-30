f = open('test.txt')

data = {}

for s in f:
    if "Testing" in s:
        st, en = s.find(' set')+5, s.find('(')
        title = s[st:en-1]
        st, en = s.find('MAE: ')+5, s.find('MSE: ')
        mae = float(s[st:en-2])
        mse = float(s[en+5:-1])
        # nums_str = string[1:len(string)-1].split(', ')
        if not data.get(title):
            data[title] = []
        
        data[title].append((mae,mse))
 

for k, v in data.items():
    mae = [i[0] for i in v]
    mse = [i[1] for i in v]
    print(k, sum(mae)/len(mae), sum(mse)/len(mse))