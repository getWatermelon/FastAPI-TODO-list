from databases import Database


class CRUDDatabase:
    def __init__(self, database: Database):
        self.database = database
