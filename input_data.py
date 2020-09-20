from file_mgmt import read_excel

input_data2 = [
    'a weeker person cannot become a king because he can be killed anytime',
    'reset my @ % & password',
    'reset my machine _ !!',
    'king can be killed anytime so we need make him strong',
    'our prince is as strong as rock',
    'your prince was as weak as feather',
    'queen is always a young girl',
    'prince is a boy will be king',
    'princess is a girl will be queen',
    'queen is looking like a godess',
    'queen was once a young girl',
    'reset my passcode',
    'a smart lady can become queen in any kingdom',
    'reset my win password',
    "1.She doesn’t study German on Monday.",
    "2.Does she live in Paris?",
    "3.He doesn’t teach math.",
    "4.Cats hate water.",
    "5.Every child likes an ice cream.",
    "6.My brother takes out the trash.",
    "7.The course starts next Sunday.",
    "8.She swims every morning.",
    "9.I don’t wash the dishes.",
    "10.We see them every week.",
    "11.I don’t like tea.",
    "12.When does the train usually leave?",
    "13.She always forgets her purse.",
    "14.You don’t have children.",
    "15.I and my sister don’t see each other anymore.",
    "16.They don’t go to school tomorrow.",
    "17.He loves to play basketball.",
    "18.He goes to school.",
    "19.The Earth is spherical",
    "20.Julie talks very fast.",
    "21.My brother’s dog barks a lot."]


def input_data(file_path):
    if file_path!="":
        excel_data=read_excel(file_path)
    else:
        excel_data=input_data2
    return excel_data