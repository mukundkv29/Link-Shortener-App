from flask import Flask, jsonify
import mysql.connector as sql
import random, string, validators

class urldata:
    originalURL = None
    shortURL = None
    def __init__(self):
        self.db = sql.connect(
            host = "127.0.0.1",
            port = 3306,
            user = "root",
            password = "mkv29123",
            database = "link",
        )


    def generate(self):
        length = 6
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choices(characters, k=length))
        return random_string


    def validate(self, url):
        if validators.url(url):
            return True
        else:
            return False


    def validateAlias(self, alias):
        return alias.isalnum()

    
    def checkAlias(self, alias):
        cursor = self.db.cursor(dictionary = True)
        cursor.execute("SELECT shortURL FROM urls WHERE shortURL=%s", (alias,))
        row = cursor.fetchone()
        if not row:
            return True
        else:
            return False


    def shorten(self, url):
        cursor = self.db.cursor(dictionary = True)
        shortURL = self.generate()

        while True:
            cursor.execute("SELECT shortURL FROM urls WHERE shortURL=%s", (shortURL,))
            row = cursor.fetchone()
            if not row:
                break
            else:
                shortURL = self.generate()

        cursor.execute("INSERT INTO urls VALUES(%s, %s)", (url, shortURL,))
        self.db.commit()
        self.shortURL = shortURL


    def shortenWithAlias(self, url, alias):
        cursor = self.db.cursor(dictionary = True)
        cursor.execute("INSERT INTO urls VALUES(%s, %s)", (url, alias,))
        self.db.commit()
        self.shortURL = alias


    def getURL(self, alias):
        cursor = self.db.cursor(dictionary = True)
        cursor.execute("SELECT originalURL from urls WHERE shortURL=%s", (alias,))
        row = cursor.fetchone()
        if not row:
            self.originalURL = None
        else:
            originalURL = row['originalURL']
            self.originalURL = originalURL
            self.shortURL = alias
