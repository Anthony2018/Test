""" pylint verion function test_create_dataframe that takes as input:
(a) a pandas DataFrame
(b) a list of column names. """
import requests

def save_file(url, file_name):
    """
    save file
    input: url, file name
    no return
    """
    r_file = requests.get(url)
    with open(file_name, 'wb') as f_name:
        f_name.write(r_file.content)

# save_file(
#         'https://inventory.data.gov/dataset/cedbc0ee-d679-4ebf-8b00-502dc0de5738/\
#         resource/ef734bd0-0aff-4687-9b8a-fc69b937be63/\
#         download/userssharedsdfratebrthsyaw1819raceethncty20002012.csv',
#         'data.csv'
#         )
# DATA_FRAME = pd.read_csv('data.csv')

def test_create_dataframe(dataframe, colomnname):
    """
    test funciton to find if the input is legal
    input: dataframe, colomnname
    return true or flase
    """
    if dataframe.shape[0] < 10:
        return False
    namels = dataframe.columns.values.tolist()
    if namels != colomnname:
        return False
    rember_class = {}
    for ls_name in colomnname:
        rember_class[ls_name] = type(dataframe[ls_name][0])
        #print(rember_class)
        for i in range(dataframe.shape[0]):
            i_name = type(dataframe[ls_name][i])
            if i_name != rember_class[ls_name]:
                return False
    return True
