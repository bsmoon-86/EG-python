select_online = "SELECT * FROM online"
select_offline = "SELECT * FROM offline"
delete_online = "DELETE FROM online where crym = %s"
create_dummy2 = """
    CREATE TABLE 
    IF NOT EXISTS
    dummy2(
        email varchar(32) primary key, 
        date DATE
    )
    """
insert_dummy2 = "INSERT INTO dummy2 VALUES (%s, %s)"