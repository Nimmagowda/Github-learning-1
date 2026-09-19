import pandas as pd
data = {
    "name":["prabhu","prashanth","kotti","lakshman","teja","suraj","prajwal","Ayyappa"],
    "age":["20","17","21","21","22","22","19","18"],
    "city":["talikoti","bapparagi","hubli","uttur","indupur","kadur","davangere","shabrimala"],
    "character":['student','student','student','student','student','student','student','God']
}

df=pd.DataFrame(data)
print(df)
df.to_excel("3_outout.xlsx")