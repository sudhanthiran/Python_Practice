## 5 funsctions, no external storgae, speed is the key O()
### add, remove, friend and unfriend. info for (Social connectivity)
## add (Name, City)
## remove(Name)
### friend (Name1, target_Name)
#### unfriend (target_name)
### info(Name)
import typing


class person():
    def __init__(self,Name : str, City : str):
        self.Name = Name
        self.City = City
        self.user_list = []
    def add(self, Name, user_name):
        self.user_list.append(user_name.Name)  ## need to handle duplicates
    def remove(self, user_to_remove):
        index_to_del = self.user_list.index(user_to_remove)
        self.user_list.__delitem__(index_to_del)


class FB_Dummy(person):
    def __init__(self,Name, City):
        super().__init__(Name,City)
        self.friend_list = []
    def add(self,object : person):
        super().add(self.Name,object.Name)
    def friend(self, friend_to_add: person):
        self.friend_list.append(friend_to_add.Name)  ## need to handle duplicates
    def unfriend(self, friend_to_remove: person):
        index_to_del = self.friend_list.index(friend_to_remove.Name)
        self.friend_list.__delitem__(index_to_del)

    def info(self):
        return "Name: "+self.Name+" City: "+self.City


obj1 = FB_Dummy("tom","nyc")
obj2 = FB_Dummy("sam","tokyo")
obj3 = FB_Dummy("nikhil","RJ")
#obj3 = FB_Dummy("bob","london")

obj1.friend(obj2)
obj1.friend(obj3)
#obj1.add("bob")


print(obj1.friend_list)
obj1.unfriend(obj3)
print(obj1.friend_list)

