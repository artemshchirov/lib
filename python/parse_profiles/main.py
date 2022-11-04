import csv

def write_csv(filename: str, text: str):

    # with open('countries.csv', 'w', encoding='UTF8') as f:
    #     writer = csv.writer(f)

    #     # write the header
    #     writer.writerow(header)

    #     # write the data
    #     writer.writerow(data)
    
    with open(filename, 'w') as f:
        for line in text:
            f.write(line)
            f.write('\n')

def find_on_page(elem: str, page: int):
    
    unique = []
    profiles = 0
    duplicates = 0
    text = []
    for item in elem:
        # print(item.text, '\n- - - - - - -')
        text.append(f"\n{item.text}\n- - - - - - -")
        if item.text:
            profiles += 1
            if item.text not in unique:
                text.append(f"\n№{profiles}: {item.text}")
                # print(f"№{profiles}: {item.text}")
                unique.append(item.text)
            else:
                duplicates += 1
                # print(f"{duplicates} Копия: {item.text}")
                text.append(f"\n{duplicates} Копия: {item.text}")

    # print(f"\n Страница: {page+1} Всего: {profiles} Уникальные: {len(unique)} Копий: {duplicates}")
    text.append(f"\n Страница: {page+1} Всего: {profiles} Уникальные: {len(unique)} Копий: {duplicates}")
    
    write_csv('test_result.txt', text)

def parse_page(url: str, page_num: int):
    from bs4 import BeautifulSoup
    import requests

    url += str(page_num)
    requests = requests.get(url)
    requests.encoding = 'utf-8'
    soup = BeautifulSoup(requests.text, "html.parser")
    parsed_elements = soup.find_all("div", class_="tovar_info")

    # print(f"\n ============== \n СТРАНИЦА: {page_num+1} \n ============== \n")
    find_on_page(parsed_elements, page_num)

def main():
    url = "https://israelbusinessguide.com/catalog/?type=expert&page="
    pages = 1
    for page in range(pages):
        print(f"page: {page+1}")
        parse_page(url, page)


if __name__ == "__main__":
    main()
