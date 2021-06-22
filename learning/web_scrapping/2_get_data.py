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

html_elem = parsed_html.select("li")[3]
print(html_elem.get_text())

html_elem_list = parsed_html.select("li")
for html_elem in html_elem_list:
    print(html_elem.get_text())

green_class_elem_list = parsed_html.select(".green")
for html_elem in green_class_elem_list:
    print(html_elem.get_text())
for html_elem in green_class_elem_list:
    print(html_elem.name)

html_elem_list = parsed_html.select("li")
for html_elem in html_elem_list:
    print(html_elem.attrs)  # get attributes

html_elem_list = parsed_html.select("li")[3]
print(html_elem.attrs["class"], html_elem["class"])  # get attribute
print(html_elem.attrs["id"], html_elem["id"])
