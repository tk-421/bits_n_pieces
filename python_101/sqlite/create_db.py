import sqlite3

conn = sqlite3.connect("mydatabase.db")

cursor = conn.cursor()

#create table
cursor.execute("""CREATE TABLE albums
                    (title text, artist text, release_date text,
                     publisher text, media_type text)
                """)

#insert new single record
cursor.execute("""
INSERT INTO albums
    VALUES('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3')
    """
    )
conn.commit()

#insert multiple Records
albums=[('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
        ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
        ('The End is Where We Begin', 'Thousand Foot Krutch', '4/7/2012', 'TF\Kmusic', 'CD'),
        ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
conn.commit()
