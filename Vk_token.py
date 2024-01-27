import requests
token='vk1.a.qtvgEEtXeN-BvjK3CzC6neXfSQ5wh57tOQ4p1k1HQ7IhMYdWjhIdQfYSs8xkuBDVu179LFPUhsg2JMBTcbnMRbYoqR8YlgspuOUew2mz0rmdrMAYN_JuBxF782ovokKxwvP3JKC7u-iySsWak-1tOyDb4bUUqvB4H5cwti07WqVkRUsPKbXpT03xwv8_BQcdt8P-o3nuN5eKbKFANtKQ4A'
version=5.199
class Vkconnect:
    def __init__(self,version,token) -> None:
        self.version=version
        self.token=token
        self.url=f"https://api.vk/com?method/"
    def usersget(self):
        return requests.get(
            f'{self.url}users.get?access_token={self.token}&v={self.version}').json()
vk=Vkconnect(version,token)
print(vk.usersget())
            

