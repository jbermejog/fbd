import psycopg2

def postgres_test():

    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='127.0.0.1' password='miclavesecreta' connect_timeout=1 ")
        conn.close()
        return True
    except:
        return False

if __name__ == '__main__':
    print(postgres_test())