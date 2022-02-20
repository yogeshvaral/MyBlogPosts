import uuid
import datetime
from model.post import Post 
from database import Database
class Blog():
    def __init__(self,author,title,description,id=None):
        self.author= author
        self.title = title
        self.description =description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Please enter title for the post")
        content = input("Please enter the content for the post")
        date = input("Please enter the date in format {}  else keep it blank".format("ddmmYYYY"))
        if date=="":
            date = datetime.datetime.utcnow()
        else :
            date=datetime.datetime.strptime(date,'%d%m%Y')
        post = Post(self.id, title, content, self.author,date=date)
        post.saveto_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def saveto_mongo(self):
        Database.insert('blogs', data=self.json())

    def json(self):
        return {
            "author" : self.author,
            "title" : self.title,
            "description" : self.description,
            "id" : self.id
        }
    @classmethod
    def from_mongo(cls,id):
        blog_data = Database.find_one(collection='blogs', query={'id':id})
        return cls(id = blog_data['id'],author=blog_data['author'], title=blog_data['title'], description= blog_data['description'])