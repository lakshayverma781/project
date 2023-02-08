# import pandas as pd
# import getpass
# import oracledb

# pw = getpass.getpass("Enter password: ")

# con = cx_Oracle.connect('shashank/shashank@orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com:1521/ORCL')

# connection = oracledb.connect(
#     user="dedec22_lakshay",
#     password=pw,
#     dsn="orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com:1521/ORCL")

# print("Successfully connected to Oracle Database")
# print(connection.version)
import pandas as pd
import oracledb
import sqlalchemy
from databases import Database

# DATABASE_URL = "sqlite:///chapter6_sqlalchemy.db"
# DATABASE_URL = "shashank/shashank@orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com:1521/ORCL"
# # DATABASE_URL = "mysql+pymysql://root:Aroha123@172.17.0.2/Aroha"
# # DATABASE_URL = "mysql+pymysql://admin:7f06EX0Tk2vUSMun966j@spicemoney-db-host/lotuspay"
# DATABASE_SERVER = 'database-server'

# DATABASE_URL = (DATABASE_SERVER, 'database-url', DATABASE_SERVER + 'database-url not configured')
# database = Database(DATABASE_URL)
# connection = oracledb.connect(
#     user="dedec22_lakshay",
#     password="dedec22_lakshay",
#     dsn="orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com:1521/ORCL")
sqlalchemy_engine = sqlalchemy.create_engine("oracle://dedec22_lakshay/dedec22_lakshay@orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com:1521/ORCL")
# sqlalchemy_engine.connect()
print("succusfully connect")
query = 'SELECT * FROM resort'
df=pd.read_sql(query,sqlalchemy_engine)
print(df)

# def get_database() -> Database:
#     return database
 