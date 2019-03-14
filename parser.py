from dateutil import parser
#import  dateutil
import mysql.connector
class fixed:
    def file1(self):
        emp_no, f_name, l_name = "", "", ""
        f = open('rawdata.prn', 'r')
        line = f.readline()
        db = mysql.connector.connect(host="localhost", user="root", password="root", db="casestudy2",
                                     port="3306")
        cursor = db.cursor()
        while line:
            line = f.readline()
            x = line
            chunks, chunk_size = len(x), int(len(x) / 1)
            if chunks != 0:
                i = [x[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
                s = str(i)
                self.OnBoadDate = s[58:71]
                ob = self.OnBoadDate.strip()
                dt = parser.parse(ob).date()
                print dt

        db.close()
if __name__ == "__main__":
    obj1 = fixed()
    obj1.file1()
