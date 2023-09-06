from config import CONN, CURSOR

class Song:
    def __init__(self, name, album) -> None:
        self.name = name
        self.album = album
        
        
    @classmethod  
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS songs (
                id INT PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        
        '''
        
        CURSOR.execute(sql)
        
    
    def save(self):
        sql = '''
        INSERT INTO songs (name, album)
        VALUES(?, ?)
        '''
        CURSOR.execute(sql, (self.name, self.album))