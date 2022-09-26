import sqlite3

connect = sqlite3.connect('./Patients.db')

db = connect.cursor()

db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit()

#table creation
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            streetaddress CHAR(25) NOT NULL,
            zipcode CHAR(25) NOT NULL,
            contactinformation VARCHAR(25) NOT NULL
        ); """

db.execute(table)
connect.commit()

db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, streetaddress, zipcode, contactinformation) values('27868', 'Joe', 'Simpson', '07/05/2004', '689 Commerce St', '98765', '578-387-2867')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, streetaddress, zipcode, contactinformation) values('59879', 'John', 'Cena', '03/20/2002', '127 Cycle Rd', '38975','187-257-1975')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, streetaddress, zipcode, contactinformation) values('23984', 'Mabel', 'Swanson', '06/05/1994', '14 April Rd', '59783', '578-397-2865')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, streetaddress, zipcode, contactinformation) values('12485', 'Lucy', 'Sam', '12/22/1989', '157 Flushing Rd', '29859', '917-478-2784')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, streetaddress, zipcode, contactinformation) values('23985', 'Andy', 'Schrank', '08/19/2001', '12 Simple Ave', '34256', '646-375-3871')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, streetaddress, zipcode, contactinformation) values('10957', 'Terrence', 'Chen', '02/26/2002', '792 Rainy St', '14872', '123-456-7890')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, streetaddress, zipcode, contactinformation) values('09538', 'Sally', 'May', '06/23/1997', '292 Storm Rd', '11356', '987-654-3212')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, streetaddress, zipcode, contactinformation) values('12256', 'Grace', 'Castillo', '10/30/2000', '21 Beta Ave', '58937', '578-389-1567')")

connect.commit()
connect.close()

