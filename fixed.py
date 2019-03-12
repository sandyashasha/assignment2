import mysql.connector
class fixed:
    def file1(self):
        emp_no,f_name,l_name="","",""
        f = open('IBM_Dataset.prn','r')
        line = f.readline()
        while line:
            line = f.readline()
            x = line
            chunks, chunk_size = len(x), int(len(x) / 1)
            if chunk_size != 0:
                i=[x[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
                s=str(i)
                self.emp_no,self.f_name,self.l_name=s[2:10],s[10:20],s[20:24]
                e=self.emp_no.strip()
                f1=self.f_name.strip()
                l=self.l_name.strip()
                db = mysql.connector.connect(host="localhost",user="root",password="root",db="casestudy2",port="3306" )
                cursor = db.cursor()
                q='insert into employee(emp_id,f_name,l_name)values( "{}","{}","{}");'.format(e,f1,l)
                q1='insert into dept(emp_id,f_name,l_name)values( "{}","{}","{}");'.format(e, f1, l)
                print q

                cursor.execute(q)
                cursor.execute(q1)
                db.commit()
        db.close()
    
if __name__ == "__main__":
    obj1=fixed()
    obj1.file1()
