import mysql.connector 
from mysql.connector import Error

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(emp_id, name, photo, biodataFile):
    print("Inserting BLOB into BDM.PHOTO_TEST table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='bdm',
                                            user='root',
                                            password='23Vela@@')
        if connection.is_connected():
            cursor = connection.cursor()
            sql_insert_blob_query = """ INSERT INTO BDM.PHOTO_TEST
                            (IDPHOTO, IDUSER, PHOTO, PHOTO_DET) VALUES (%s,%s,%s,%s)"""

            empPicture = convertToBinaryData(photo)
            file = convertToBinaryData(biodataFile)

            # Convert data into tuple format
            insert_blob_tuple = (emp_id, name, empPicture, file)
            result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
            connection.commit()
            print("Image and file inserted successfully as a BLOB into python_employee table", result)


    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB(1, 1, "C:\\Users\\brand\\OneDrive\\Imágenes\\250px-Pattar.png",
           "C:\\Users\\brand\\OneDrive\\Imágenes\\250px-Pattar.png")