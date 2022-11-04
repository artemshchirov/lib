from bs4 import BeautifulSoup


html_string = """
<!Doctype html>
<html>
<head>
    <title>Web Development Page</title>
    <style type="text/css">

        h1{
            color: magenta;
            background: grey;
        }

        li{
            color: grey
        }

        #css-li{
            color: blue;
        }

        .green{
            color: green;
        }

    </style>
</head>
<body>
    <h1>Web Development</h1>
    <h1 class="green">Web</h1>
    <h3> Programming languages </h3>

    <ol>
        <li>HTML</li>
        <li id="css-li">CSS</li>
        <li class="green bold">JavaScript</li>
        <li class="green" id="python_li">Python</li>
    </ol>

    <p>1. HTML - HyperText Markup Language</p>
    <p>2. CSS - Cascading Style Sheets</p>
    <p>3. JavaScript</p>
    <p>4. Python</p>

</body>
</html>
"""

parsed_html = BeautifulSoup(html_string, 'html.parser')

data1 = parsed_html.body.contents[7].contents
print(data1)

data2 = parsed_html.body.contents[1].next_sibling.next_sibling
print(data2)

data3 = parsed_html.find(id="css-li").parent.parent
print(data3)

data4 = parsed_html.find(id="css-li").parent.previous_sibling.previous_sibling
print(data4)

data5 = parsed_html.find(id="css-li").find_next_sibling().find_next_sibling()
print(data5)

data6 = parsed_html.find(id="css-li").find_next_sibling(id="python_li")
print(data6)

data6 = parsed_html.find(id="css-li").find_next_sibling(class_="bold")
print(data6)

data7 = parsed_html.find(id="css-li").find_next_sibling(class_="bold").find_parent().find_parent()
print(data7)

data8 = parsed_html.body.findChildren()[2].find_next_sibling()
print(data8)
