import unittest
import main

import csv
class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.tested=[]
        with open('new.csv', 'r',encoding='utf8') as self.csv_file:
            reader = csv.reader(self.csv_file,delimiter="$")
            next(reader)
            for row in reader:
                self.tested.append(row)
    def tearDown(self):
        self.csv_file.close()

    def test_size(self):
        self.assertEqual(len(main.row1), len(main.row0))
    def test_no_data(self):
        for buff in range(0, 700):
            self.assertEqual(self.tested[buff][0], main.tab[0][buff])
    def test_vol_data(self):
        for buff in range(0, 700):
            self.assertEqual(self.tested[buff][1], main.tab[1][buff])
    def test_article_no_data(self):
        for buff in range(0, 700):
            self.assertEqual(self.tested[buff][2], main.tab[2][buff])
    def test_pages_in_range_data(self):
        for buff in range(0, 700):
            self.assertEqual(self.tested[buff][3], main.tab[3][buff])
    def test_publisher_location_data(self):
        for buff in range(0, 700):
            self.assertEqual(self.tested[buff][4], main.tab[4][buff])
    def test_publisher_year_data(self):
        for buff in range(0, 700):
            self.assertEqual(self.tested[buff][5], main.tab[5][buff])
    def test_publisher_name(self):
        for buff in range(0, 700):
            self.assertEqual(self.tested[buff][6], main.tab[6][buff])
if __name__ == '__main__':
    unittest.main()
