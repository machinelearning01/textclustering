from file_mgmt import read_excel

input_data2 = [
    'queen IS Always referred to a godess visit_002@gmail.com',
    "i want to order a pizza",
    'queen is looking like a 5 star godess',
    'queen IS Always referred to a godess visit_002@gmail.com',
    "i want to order a pizza",
    'queen is looking like a 5 star godess',
    'reset my 10 windows password',
    'reset my mac password',
    'queen was once a queen young girl queen',
    'reset my windows password and my id is jinraj_234',
    'a stronger person can become king in any kingdom',
    'reset my system password',
    'reset my ntid',
    'a weeker person cannot become a king because he can be killed anytime',
    'reset my password',
    'reset my machine',
    'king can be killed anytime so we need make him strong',
    'our prince is as strong as rock',
    'prince is a boy will be king',
    'princess is a girl will be queen',
    'queen is looking like a godess',
    'queen was once a young girl',
    'a smart lady can become queen in any kingdom',
    'a intelligent woman can become anything in any kingdom'
]


def input_data(file_path):
    if file_path!="":
        excel_data=read_excel(file_path)
    else:
        excel_data=input_data2
    return excel_data