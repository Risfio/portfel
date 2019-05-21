import unittest
import os
import pandas as pd

from portfel.bws import FileLoaderQUIK


def print_info(msg):
    print("*" *10, "\r\n", msg, "\r\n", "*" *10)


class TestBWS(unittest.TestCase):
    def test_complex(self):
        """
        Complex testing. Removed msut.
        :return:
        """
        dir_path = os.path.join(os.path.expanduser('~'), "documents", "projects", "BWS", "tests", "TEMP")


    def test_read_data(self):
        directory = os.path.join(os.path.expanduser('~'), "documents", "projects", "BWS", "tests", "TEMP")
        quik = FileLoaderQUIK()
        quik.directory = directory
        file_name1 = "emitents_20052019"
        file_name2 = "emitents_21052019"
        main_file_name = "emitents"
        main_file_path = os.path.join(directory, "".join([main_file_name, ".txt"]))

        data1 = quik.read_data(file_name=file_name1)
        data2 = quik.read_data(file_name=file_name2)

        # Add new data (data2) to main data(data1)
        # data2[1:] - ignore first row what is column names
        data1 = data1.append(data2[1:], ignore_index=True)
        
        # Uncomment string below if need to merge 2 files(not update main file)
        # data1.to_csv(main_file_path, index=False)

        main_data = pd.read_csv(main_file_path)
        main_data = main_data.append(data1[1:], ignore_index=True)
        print_info(main_data['Name'].size)

    def test_fileload(self):
        columns = tuple(['Name', 'Date', 'Code', 'ISIN', 'Min', 'Max', 'Open', 'Close', 'Volume'])
        directory = os.path.join(os.path.expanduser('~'), "documents", "projects", "BWS", "tests", "TEMP")
        file_name = "emitents_08052019.txt"
        quik = FileLoaderQUIK(directory=directory, file_name="emitents_08052019", names=columns)
        data = quik.read_data()

    def test_wrong_num_columns(self):
        # Указываем неверное количество колонок(8 вместо 9)
        # Но ничего непроисходит , потому что колонки вручную прописаны уже в FileLoaderQUIK
        columns = tuple(['Name', 'Date', 'Code', 'ISIN', 'Min', 'Max', 'Open', 'Close', 'Volume'])
        directory = os.path.join(os.path.expanduser('~'), "documents", "projects", "BWS", "tests", "TEMP")
        file_name = "emitents_08052019.txt"
        quik = FileLoaderQUIK(directory=directory, file_name="emitents_08052019", names=columns[1:])
        data = quik.read_data()
        # Test columns names espetional for QUIK file loader
        self.assertEqual(columns, tuple(data.columns.tolist()))

    def test_change_names(self):
        import re
        pat = re.compile('\[+.+\]')
        directory = os.path.join(os.path.expanduser('~'), "documents", "projects", "BWS", "tests", "TEMP")
        file_name = "emitents_08052019"
        quik = FileLoaderQUIK(directory=directory, file_name=file_name)
        data  = quik.read_data()
        s = data['Name'][0]

        def func(word):
            pat = re.compile('\[+.+\]')
            name = pat.split(word)[0].strip()
            if word.count(name) == 0:
                raise Exception("Troubles construct correct name from string {0}!".format(word))
            return name

        self.assertEqual(u'Сбербанк', func(s))
        self.assertEqual(len(func(s)), 8)

        data['Name'] = data['Name'].map(func)


if __name__ == '__main__':
    unittest.all()

