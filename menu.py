from database import Database
from model.blog import Blog 
class Menu:
    def __init__(self):
        self.user = input("Please enter author name:")
        self.user_blog=None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one(collection='blogs', query={'author':self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False
    
    def _prompt_user_for_account(self):
        title = input("Please enter title for blog")
        description = input("Please enter description for blog")
        blog = Blog(self.user, title, description)
        blog.saveto_mongo()
        self.user_blog = blog

    def run_menu(self):
        user_preference = input("Enter 'W' for write or 'R' to read blogs")
        if user_preference == 'W':
            self.user_blog.new_post()
        elif user_preference == 'R':
            self._list_blogs()
            self._view_blogs()
            
        else :
            print("Thanks for blogginh")

    def _list_blogs(self):
        blogs = Database.find('blogs', {})
        for blog in blogs:
            print("blog_ID :{} blog title:{} Blog_description:{} blog_author:{}".format(blog['id'],blog['title'],blog['description'],blog['author']))

    def _view_blogs(self):
        blog_id = input("Please enter blog_id to view blog")
        blog_toView = Blog.from_mongo(blog_id)
        blogs_posts =blog_toView.get_posts()

        for post in blogs_posts:
            print(post)
