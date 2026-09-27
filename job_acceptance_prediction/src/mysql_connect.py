import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
conn=mysql.connector.connect(host=os.getenv('MYSQL_HOST','localhost'),port=int(os.getenv('MYSQL_PORT','3306')),user=os.getenv('MYSQL_USER','root'),password=os.getenv('MYSQL_PASSWORD',''),database=os.getenv('MYSQL_DATABASE','job_acceptance_db'))
print('MySQL connected successfully!')
conn.close()
