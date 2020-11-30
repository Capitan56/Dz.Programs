import pymysql.cursors
connect = pymysql.connect(host='localhost',
                          user='root',
                          password='Wqb6abec1',
                          db='mydb',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor
                          )
with connect.cursor() as cursor:
    cursor.execute("""show tables""")
    print(cursor.fetchall())
    cursor.execute("""insert into studentslist (`ID`,`Name`,`Group`) values ('1','Василий','A');""")
    cursor.execute("""insert into studentslist (`ID`,`Name`,`Group`) values ('2','Сергей','B');""")
    cursor.execute("""insert into studentslist (`ID`,`Name`,`Group`) values ('3','Борис','B');""")
    cursor.execute("""insert into studentslist (`ID`,`Name`,`Group`) values ('4','Геннадий','C');""")
    cursor.execute("""insert into studentslist (`ID`,`Name`,`Group`) values ('5','Яков','B');""")
    cursor.execute("""insert into studentslist (`ID`,`Name`,`Group`) values ('6','Артём','A');""")
    cursor.execute("""insert into studentslist (`ID`,`Name`,`Group`) values ('7','Никита','A');""")
    cursor.execute("""insert into studentslist (`ID`,`Name`,`Group`) values ('8','Анастасия','C');""")
    cursor.execute("""insert into studentslist (`ID`,`Name`,`Group`) values ('9','Леонид','B');""")
    cursor.execute("""insert into studentslist (`ID`,`Name`,`Group`) values ('10','Вероника','B');""")

    cursor.execute("""update studentslist  set `Name` = 'Яна', `Group` = 'A'  where (`ID` = '2') and (`Name` = 'Сергей') and (`Group` = 'B');""")
    cursor.execute("""update studentslist  set `Name` = 'Ксения', `Group` = 'С'  where (`ID` = '7') and (`Name` = 'Никита') and (`Group` = 'A');""")
    cursor.execute("""update studentslist  set `Name` = 'Денис', `Group` = 'A'  where (`ID` = '9') and (`Name` = 'Леонид') and (`Group` = 'B');""")
connect.commit()
with connect.cursor() as cursor:
    cursor.execute("""select * from studentslist;""")
    print(cursor.fetchall())
connect.close()