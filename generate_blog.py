import os
import re
from datetime import datetime


POST_FOLDER = "blog/posts"
INDEX_FILE = "blog/index.html"
RSS_FILE = "blog/feed.xml"


posts = []


# Find posts
for filename in os.listdir(POST_FOLDER):

    if filename.endswith(".html"):

        path = os.path.join(POST_FOLDER, filename)

        with open(path, "r", encoding="utf-8") as file:
            content = file.read()


        title = re.search(r"TITLE:\s*(.*)", content)
        date = re.search(r"DATE:\s*(.*)", content)
        description = re.search(r"DESCRIPTION:\s*(.*)", content)


        if title and date:

            posts.append({
                "title": title.group(1),
                "date": date.group(1),
                "description": description.group(1) if description else "",
                "file": filename
            })


# Sort newest first
posts.sort(
    key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"),
    reverse=True
)


# Generate HTML index

html = """
<!DOCTYPE html>
<html>
<head>
  <link rel="icon" type="image/x-icon" href="images/Icon/Me_ico.png">
  <meta charset="UTF-8">
  <title>READ MY THOUGGHTTS!!</title>
  <link rel="stylesheet" href="blog_style.css">
</head>

<body>

  <div id="content-wrapper">
  <nav class="navbar"><ul class="menu">
    <li><a href="../index.html">Home</a></li>
    <li><a href="blogindex.html">Other Entries</a></li>
  </ul></nav>

 


  <img src="../images/rainbar.gif" alt="Animated bar" width="950">
  <div class="cutsey">
    <div id="content-wrapper-innie">
     <center><h1> Blog Entries </h1>
    <h4>text underneath</h4></center>
    </div>
 
<table>
"""


for post in posts:

    html += f"""
<tr>
<td id="cutsey">{post["date"]}</td>

<td id="cutsey">
<a href="posts/{post["file"]}">
{post["title"]}
</a>
</td>

</tr>
"""


html += """
<!-- Procedural end -->
</table>

  <img src="../images/rainbar.gif" alt="Animated bar" width="950">


 </div>

<script src="https://utteranc.es/client.js"
        repo="BossKnightYT/Main"
        issue-term="pathname"
        theme="dark-blue"
        crossorigin="anonymous"
        async>
</script>
</body>
</html>
<style>


body::before {
content: " ";
display: block;
position: fixed;
top: 0;
left: 0;
bottom: 0;
right: 0;
background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%);
z-index: 2;
background-size: 100% 2px, 3px 100%;
pointer-events: none;
}
.logo {
filter: sepia(100%) hue-rotate(221deg) saturate(0);

</style><style>
</style><style>

p {
  font-family: creepster;
  color: black;
  text-shadow: 0px 0px 4px pink;
}

.blog-entry .title {
  font-family: creepster;
  font-size: 40px;
  color: black; 
  text-spacing: normal;
  text-shadow: 0px 0px 10px #ffffff;
}

.count {
  color: black;
  text-shadow: 0px 0px 4px white ;
}

.article .edit-info .author-details h4, a, label, .blog-entry .comments .heading h4, .logout-btn {
  font-family: creepster;
  color: white;
}

button {
  font-family: creepster;
}

.blog-entry .kudos-btn {
  font-family: creepster;
  text-shadow: 0px 0px 4px black;
  box-shadow: none ;
}


main {
  border-radius: 30px;
  border: 12px solid black;
  background-color: rgb(235, 143, 196);
}

main .left, main .right {
  color: white;
  text-shadow: 0px 0px 4px black;
}

.blog-entry .content {
  padding: 10px;
  font-family: creepster;
}

body{
  background: url(https://ih1.redbubble.net/image.4956547621.5859/flat,750x1000,075,t.jpg);
  background-attachment: fixed;
}

footer {
  background-color: transparent;
  color: #ffffff;
}

nav {
  background-image: url(https://cdn.discordapp.com/attachments/1135706097534128138/1165097724069298238/image0.jpg?ex=65459ccf&is=653327cf&hm=a91836be251a3e2fd1fa9c2b7340cc15afbb584bec8c7bbd92881ae09353669b&);
  background-attachment: fixed;
  color: #ffffff;
  font-family: creepster;
  border-radius: 12px;
}

nav .links {
  background-color: rgba(0, 0, 0, 0.3);
  font-family: creepster;
  color: #ffffff;
  text-shadow: 0 0 5px #000000 ;
  font-size: max(11px) ;
}

nav .links a {
  text-shadow: 0 0 5px #000000 ;
  font-size: max(11px) ;
}

.edit-info {
  background-image: url(https://www.itl.cat/pngfile/big/13-133710_skull-wallpapers-for-iphone-4-skull-and-crossbones.jpg);
  background-attachment: fixed;
  border: 2px solid rgb(227, 50, 148);
  border-radius: 12px;
  box-shadow: 0px 0px 10px white;
}

.comments-table{
  display: block;
  height: auto;
  overflow-y: scroll;
  Border-radius: 15px; 
  border: 2px solid rgb(227, 50, 148);
  text-shadow: 0px 0px 4px #000000, 0 0 25px #000000, 0 0 3px #000000; 
  box-shadow: 0px 0px 15px #ffffff;
}

.comments-table td{
  padding: 10px;
}

.comment-replies {
  border: 2px solid rgb(227, 50, 148);
  border-radius: 12px;
  margin: 0px 0px 10px 0px;
}

.comments-table .pinned{
  color: white;
  text-shadow: 0px 0px 4px black;
  font-family: 'potta one';
}

img {
  border-radius: 12px;
  border: solid 2px rgb(227, 50, 148);
  box-shadow: 0px 0px 12px white;
}

nav .top .left img {
  border: none  ;
  box-shadow: none  ;
}

.icon {
  border: none  ;
  box-shadow: none  ;
}

.blog-entry .profile-pic img {
  box-shadow: none  ;
}


:root {
    --logo-blue: transparent;
    --darker-blue: white;
    --lighter-blue: rgb(227, 50, 148);
    --even-lighter-blue: ;
    --lightest-blue: ;
    --dark-orange: black;
    --light-orange: rgb(227, 50, 148)  ;
    --even-lighter-orange: #ff4fb0;
    --green: white;
	        --table-header: #white;
	--table-color: white;
	--link-text: white;
	--main-text: white;
}
}
</style>


"""


with open(INDEX_FILE, "w", encoding="utf-8") as file:
    file.write(html)



# Generate RSS, no clue how to actually test this LOL

rss = """<?xml version="1.0" encoding="UTF-8"?>

<rss version="2.0">

<channel>

<title>My Blog</title>

<link>https://BossKnightYT.github.io/main/</link>

<description>My updates</description>

"""


for post in posts:

    rss += f"""

<item>

<title>{post["title"]}</title>

<link>
https://BossKnightYT.github.io/main/blog/posts/{post["file"]}
</link>

<description>
{post["description"]}
</description>

<pubDate>
{post["date"]}
</pubDate>

</item>

"""


rss += """

</channel>

</rss>

"""


with open(RSS_FILE, "w", encoding="utf-8") as file:
    file.write(rss)


print(f"Generated {len(posts)} posts.")