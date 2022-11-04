def print_element_text(elem, page: int):
    unique = []
    profiles = 0
    duplicates = 0
    for item in elem:
        elem_text = ' '.join(item.text.split())
        if elem_text and "г." in elem_text:
            profiles += 1
            if elem_text not in unique:
                print(profiles, elem_text)
                unique.append(elem_text)
            else:
                duplicates += 1
                print(f"{duplicates} Копия: {elem_text}")
    print(f"\n Страница: {page+1} Всего: {profiles} Уникальные: {len(unique)} Копий: {duplicates}")
    

for i in range(4):
    from bs4 import BeautifulSoup
    import requests
    
    url = f"https://doska.israelinfo.co.il/mes/8/?p={i}"    
    requests = requests.get(url)
    requests.encoding = 'cp1251'
    soup = BeautifulSoup(requests.text, "html.parser")
    parsed_elements = soup.find_all("p", class_="p10")
    
    print(f"\n ============== \n СТРАНИЦА: {i+1} \n ============== \n")
    print_element_text(parsed_elements, i)

