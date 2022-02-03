from config import config
cursor = config.cursor()
list1 = []

class databases:
    def create_table():
        creating_table = """
        CREATE TABLE IF NOT EXISTS works(
        id VARCHAR(10),
        person_name VARCHAR(25),
        company_name VARCHAR(12),
        salary INTEGER
        )
        """
        cursor.execute(creating_table)
        config.commit()


    def quiring_data_from_table():
        cursor.execute("SELECT * FROM works")
        data = cursor.fetchall()
        return data


    def inserting_into_table(id, person_name, company_name, salary):
        cursor.execute(f"INSERT INTO works VALUES('{id}', '{person_name}', '{company_name}', {salary})")
        config.commit()


    def updating_table():
        cursor.execute("UPDATE Staff SET name ='ajnfmla' WHERE id = 'akfal'")
        config.commit()


    def deleting_from_table():
        cursor.execute("DELETE FROM works WHERE name = 'Nurali'")
        config.commit()


    def deleting_table():
        cursor.execute("DROP TABLE IF EXISTS Staff")
        config.commit()

    def counter():
        cursor.execute("SELECT COUNT(*) as count FROM works")
        data = cursor.fetchall()
        for i in data:
            for object in i:
                data = object
        cursor.execute("SELECT SUM (salary) from works")
        data2 = cursor.fetchall()
        for i in data2:
            for object in i:
                data2 = object
        data3 = data2/data
        cursor.execute("SELECT salary from works")
        data5 = cursor.fetchall()
        for i in data5:
            for object in i:
                data5 = object
                if data5 > data3:
                    cursor.execute("SELECT ID FROM works")
                    data4 = cursor.fetchall()
                    cursor.execute("SELECT person_name FROM works")
                    data6 = cursor.fetchall()
                    return data4, data6

