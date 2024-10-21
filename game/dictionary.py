# tieng anh: tieng viet
# Hay nhap tieng anh: Hello
# Hap nhap tieng viet: Xin chao
# lay gia tri tieng anh, tieng viet => luu vao file

# Luu vao file
# add.toExcel

# 1. Nhap du lieu, 2. Đóng chương trình


from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("index.html")

mock_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "coding"],
    "scores": [85, 92, 78],
}

html = template.render(data=mock_data)

# Save the HTML file
with open("output.html", "w") as f:
    f.write(html)
