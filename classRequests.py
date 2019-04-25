import pymysql
import pymysql.cursors

class botRequest:

    def __init__(self, host = 'localhost', user = 'mcdb', pw = 'marina',
                 db = 'promodataia', char = 'utf8mb4', cursclass = pymysql.cursors.DictCursor):
        self.host = host
        self.user = user
        self.pw = pw
        self.db = db
        self.char = char
        self.cursclass = cursclass


    def selectRequest(self, data, dataTable, whereCol="NULL", whereVal="NULL"):

        connection = pymysql.connect(host=self.host,
                                     user=self.user,
                                     password=self.pw,
                                     db=self.db,
                                     charset=self.char,
                                     cursorclass=self.cursclass)

        try:

            with connection.cursor() as cursor:
                if whereCol == "NULL":
                    sql = """SELECT `%s` FROM `%s`""" % (data, dataTable)
                else:
                    sql = """SELECT `%s` FROM `%s` WHERE `%s` = %s""" % (data, dataTable, whereCol, whereVal)
                cursor.execute(sql)
                dataList = cursor.fetchall()
                liste = []
                for elt in dataList:
                    liste.append(elt[data])
                return liste


        finally:
            connection.close()

"""
test = botRequest()
simpleRequest = test.selectRequest('prenom', 'Students')
print("simpleRequest =", simpleRequest)
whereRequest = test.selectRequest('astro', 'Students', 'prenom', "'Marina'")
print("whereRequest =", whereRequest)
"""