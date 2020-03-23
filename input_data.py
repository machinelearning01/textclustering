from file_mgmt import read_excel

input_data2 = ['queen is always referred to a godess',
               'queen is looking like a godess',
               'queen was once a young girl',
               'a stronger person can become king in any kingdom',
               'a weeker person cannot become a king because he can be killed anytime',
                'king can be killed anytime so we need make him strong',
               'our prince is as strong as rock',
                'prince is a boy will be king',
                'princess is a girl will be queen',
               'queen is always referred to a godess',
               'queen is looking like a godess',
               'queen was once a young girl',
               'a stronger person can become king in any kingdom',
               'a smart lady can become queen in any kingdom',
               'a intelligent woman can become anything in any kingdom',
               'a weeker person cannot become a king because he can be killed anytime',
               'our prince is as strong as rock',
               'queen is always referred to a godess',
               'queen is looking like a godess',
               'queen was once a young girl',
               'a stronger person can become king in any kingdom',
               'a weeker person cannot become a king because he can be killed anytime',
                'king can be killed anytime so we need make him strong',
               'our prince is as strong as rock',
                'prince is a boy will be king',
                'princess is a girl will be queen',
               'queen is always referred to a godess',
               'queen is looking like a godess',
               'queen was once a young girl',
               'a stronger person can become king in any kingdom',
               'a weeker person cannot become a king because he can be killed anytime',
               'our prince is as strong as rock'
               ]

input_data1=['reset my windows password',
             'reset my mac password',
             'reset my system password',
             'reset my ntid',
             'reset my password',
             'reset my machine',
             'reset my windows password',
             'reset my mac password',
             'reset my system password',
             'reset my ntid',
             'reset my password',
             'reset my machine',
             'reset my windows password']

excel_file_path = ""
def input_data():
    excel_data = read_excel(excel_file_path)
    return input_data2