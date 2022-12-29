

#solution
user={}
name=input("what is your name:")
age=input("what is your age:")
fav_movies=input("what is your fav movies:").split(",")
fav_songs=input("what is your fav songs:").split(",")
user['name']=name
user['age']=age
user['fav_movies']=fav_movies
user['fav_songs']=fav_songs
print(user)