from jinja2 import Environment, FileSystemLoader
import json


def export_html(data):
    print(data)
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("index.html")

    html = template.render(data=data)

    # Save the HTML file
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html)


def save_to_storage(data):
    json_data = []
    with open("data.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)

    # Processing file
    json_data.append(data)

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)


# tieng anh: tieng viet
# Hay nhap tieng anh: Hello
# Hap nhap tieng viet: Xin chao
# lay gia tri tieng anh, tieng viet => luu vao file

# Luu vao file
# add.toExcel

# 1. Nhap du lieu, 2. Đóng chương trình

MODE = {"Input": 1, "Export": 2, "Exit": 3}


def main():
    run = True
    model = [
        {"vocabulary": "familiar", "mean": "quen"},
        {"vocabulary": "author", "mean": "tác giả"},
        {"vocabulary": "detail", "mean": "chi tiết"},
    ]

    while run:
        print("Nhập từ vựng mỗi ngày!")
        print("Hãy chọn phương thức mong muốn:")
        print(
            "1: Nhập dữ liệu ----- 2: Trích xuất dữ liệu(csv, html, pdf) ----- 3: Đóng Chương Trình"
        )
        mode = int(input("Chọn phương thức: "))

        if mode == MODE["Exit"]:
            run = False
            break

        if mode == MODE["Input"]:
            vocabulary = input("Vocabulary: ")
            mean = input("Mean: ")

            save_to_storage({"vocabulary": vocabulary, "mean": mean})
            print("Success save to storage")
            continue

        if mode == MODE["Export"]:
            json_data = []
            with open("data.json", "r", encoding="utf-8") as f:
                json_data = json.load(f)
            export_html(json_data)


if __name__ == "__main__":
    main()
