from model.post import Post 
from model.blog import Blog 
from database import Database
from menu import Menu
# from blog import Blog
Database.initialise()
# test = input("enter name")
# print(test)

##post
# post1 = Post("4", "My post4", "this is my first post", "Yogesh Varal")

# post1.saveto_mongo()

# post2 = Post.from_mongo('854d4185f14c431f88bc685b9b1f5d68')
# print(post2)

# for post in Post.from_blog("4"):
#     print(post)

# ##Blogs

# blog = Blog(author="Yogesh ",title = 'Blog2',description="first blog")
# blog.new_post()
# blog.saveto_mongo()

# blog_post = blog.from_mongo(blog.id)
# print(blog_post.get_posts())

m = Menu()
m.run_menu()