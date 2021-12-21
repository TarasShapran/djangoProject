import json
from typing import Optional

db = 'dataBase.json'


class DBtest:
    @staticmethod
    def read_db() -> list[dict]:
        try:
            with open(db) as file:
                return json.load(file)
        except Exception as ex:
            print(ex)
            return []

    @classmethod
    def create(cls, user: dict) -> dict:
        users = cls.read_db()
        new_user = {'id': users[-1].get('id') + 1 if users else 1, **user}
        users.append(new_user)
        with open(db, 'w') as file:
            json.dump(users, file)
        return new_user

    @classmethod
    def update(cls, data: dict, pk: int) -> Optional[dict]:
        users = cls.read_db()
        for user in users:
            if user.get('id') == pk:
                user.update(**data, id=pk)
                with open(db, 'w') as file:
                    json.dump(users, file)
                return user

    @classmethod
    def delete(cls, pk: int) -> Optional[bool]:
        users = cls.read_db()
        for user in users:
            if user.get('id') == pk:
                users.remove(user)
                with open(db, 'w') as file:
                    json.dump(users,file)
                return True
