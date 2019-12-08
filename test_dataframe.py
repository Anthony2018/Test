""" pylint verion test_dataframe to test the csv file and data frame """
import pandas as pd
import numpy as np
import requests
import function
def save_file(url, file_name):
    """
    save file
    input: url and file name
    return: no return
    """
    r_file = requests.get(url)
    with open(file_name, 'wb') as f_name:
        f_name.write(r_file.content)

#Check for nan values:
def check_nan(data_frame):
    """
    check nan: if there are nan in dataframe, input is dataframe
    input: data frame
    return: true or false
    """
    flag = 0
    for col in data_frame.columns:
        # print('col',col)
        # print('col len',df[col].count())
        if data_frame[col].count() != len(data_frame):
            if data_frame[col].isnull().values:
                loc = data_frame[col][data_frame[col].isnull().values].index.tolist()
                flag = 1
                print('columname: "{}", row name: {} is nan'.format(col, loc))
    if flag == 0:
        print('pass the nan check')
        return True
    return False

def check_row(data_frame):
    """
    Verify that the dataframe has at least one row, input is dataframe
    input: data frame
    return: true or false
    """
    row = data_frame.shape[0]
    if row <= 1:
        print('not pass the row check, row is', row)
        return False
    print('pass the row check, row is', row)
    return True

def check_type(dataframe, colomnname):
    """
    Check that all columns have values of the corect type. input is dataframe
    input: data frame
    return: true or false
    """
    rember_class = {}
    for ls_name in colomnname:
        rember_class[ls_name] = type(dataframe[ls_name][0])
        #print(rember_class)
        for i in range(dataframe.shape[0]):
            type_name = type(dataframe[ls_name][i])
            if type_name != rember_class[ls_name]:
                print('not pass the type check')
                return False
    print('pass the type check')
    return True


DATA_FRAME = pd.DataFrame(
    np.arange(200).reshape(20, 10),
    index=list('abcdefghijklmnopqrst'),
    columns=list('abcdefghij')
    )
DATA1 = pd.DataFrame(np.arange(2).reshape(2, 1), index=list('ab'), columns=list('a'))
DATA2 = pd.DataFrame(
    np.arange(200).reshape(20, 10),
    index=list('abcdefghijklmnopqrst'),
    columns=list('abcdefghij')
    )
DATA2.loc['a', 'd'] = None
#print(type(data2.loc['a','d']),type(data2.loc['b','d'] ))
#print(data)
#print(function.test_create_dataframe(df,df.columns.values.tolist()))
try:
    assert (
        check_nan(DATA_FRAME) ==
        function.test_create_dataframe(DATA_FRAME, DATA_FRAME.columns.values.tolist())
        )
    assert (
        check_row(DATA_FRAME) ==
        function.test_create_dataframe(DATA_FRAME, DATA_FRAME.columns.values.tolist())
        )
    assert (
        check_type(DATA_FRAME, DATA_FRAME.columns.values.tolist()) ==
        function.test_create_dataframe(DATA_FRAME, DATA_FRAME.columns.values.tolist())
        )
    DATA2.loc['a', 'd'] = 'test'
    assert (
        check_type(DATA2, DATA2.columns.values.tolist()) ==
        function.test_create_dataframe(DATA2, DATA2.columns.values.tolist())
        )
except AssertionError:
    print('AssertionError')
else:
    print('minitest pass')

save_file(
    'https://inventory.data.gov/dataset/cedbc0ee-d679-4ebf-8b00-502dc0de5738/\
resource/ef734bd0-0aff-4687-9b8a-fc69b937be63/\
download/userssharedsdfratebrthsyaw1819raceethncty20002012.csv',
    'data.csv'
        )
DATA_FRAME = pd.read_csv('data.csv')
try:
    assert (
        check_nan(DATA_FRAME) ==
        function.test_create_dataframe(DATA_FRAME, DATA_FRAME.columns.values.tolist())
        )
    assert (
        check_row(DATA_FRAME) ==
        function.test_create_dataframe(DATA_FRAME, DATA_FRAME.columns.values.tolist())
        )
    assert (
        check_type(DATA_FRAME, DATA_FRAME.columns.values.tolist()) ==
        function.test_create_dataframe(DATA_FRAME, DATA_FRAME.columns.values.tolist())
        )
except AssertionError:
    print('AssertionError')
else:
    print('test is same with my function test')
