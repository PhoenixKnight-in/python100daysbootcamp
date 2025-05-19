class User:
    def __init__(self,user_id="000",username="unknown"):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self,user):
        user.followers += 1
        self.following += 1
user_1 = User("011","anglea")
print(user_1.username)
user_2 = User('101','sachin')
print(user_2.username)
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
