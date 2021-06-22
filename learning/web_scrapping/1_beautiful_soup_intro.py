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
        <li class="green">JavaScript</li>
        <li class="green">Python</li>
    </ol>

    <p>1. HTML - HyperText Markup Language</p>
    <p>2. CSS - Cascading Style Sheets</p>
    <p>3. JavaScript</p>
    <p>4. Python</p>

</body>
</html>
"""

parsed_html = BeautifulSoup(html_string, 'html.parser')

print(parsed_html)
print(type(parsed_html))
print(parsed_html.body.ol.li)
print(parsed_html.find('li'))
print(type(parsed_html.find('li')))
print(parsed_html.find_all('li'))
print(type(parsed_html.find_all('li')))
print(parsed_html.find(id="css-li"))
print(parsed_html.select('#css-li')[0])  # without index return list
print(parsed_html.find_all(class_="green"))
print(parsed_html.select(".green")[1])
print(parsed_html.select("li"))
print(parsed_html.select("li")[3])
