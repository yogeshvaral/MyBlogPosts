from database import Database
import datetime
import uuid
class Post():

    def __init__(self,blog_id,title,content ,author,date = datetime.datetime.utcnow(),id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id

    def json(self):
        return {
            "id" : self.id,
            "blog_id" : self.blog_id,
            "title" : self.title,
            "content" : self.content,
            "author" : self.author,
            "created_date" : self.created_date
        }

    
    def saveto_mongo(self):
        Database.insert(collection='posts',data=self.json())

    @classmethod
    def from_mongo(cls,id):
        post_data = Database.find_one('posts',{'id' : id})
        return cls(blog_id=post_data['post_data'],title=post_data['title'],content=post_data['content'] ,author =post_data['author'] ,
        date =post_data['date'],id=post_data['id'])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find('posts',{'blog_id':id})]