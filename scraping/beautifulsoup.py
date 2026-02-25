from bs4 import BeautifulSoup
import requests

class QuoteScrape:

    def __init__(self,total_pages):
        self.full_data = []
        self.top_10_tags = []
        self.total_pages = total_pages
        self.authors = set()
        self.author_details = []

    def scrape_logic(self):
        for i in range(1, self.total_pages+1):
            url = f"https://quotes.toscrape.com/page/{i}/"
            data = requests.get(url)
            soup_data = BeautifulSoup(data.text, "html.parser")
            quote_box = soup_data.find_all("div", class_="quote")

            for box in quote_box:
                quote = box.find("span", class_="text").text
                author = box.find("small", class_="author").text
                tag_box = box.find_all("a", class_="tag")
                tags = [tag.text for tag in tag_box]
                self.full_data.append({"author": author,"quote": quote,"tags": tags})
                self.authors.add(author.replace(" ", "-"))
        top_tags_box = soup_data.find_all('span',class_='tag-item')

        for tags in top_tags_box:
            top_tags = tags.find('a',class_='tag')
            self.top_10_tags.append(top_tags.text)
                
        print(self.full_data)
    
    def scrape_author_details(self):
        for author_name in self.authors:
            url = f"https://quotes.toscrape.com/author/{author_name}/"
            data = requests.get(url)
            soup_data = BeautifulSoup(data.text,"html.parser")

            born_date = soup_data.find('span',class_='author-born-date').text
            born_location = soup_data.find('span',class_='author-born-location').text
            description = soup_data.find('div',class_='author-description').text.strip()

            self.author_details.append({"author":author_name.replace("-", " "),"born_date": born_date,"born_location": born_location[3::],"description": description})
        print(self.author_details)

    def save_quote_file(self):
        with open('quotes.txt', 'w', encoding='utf-8') as file:
            
            file.write(f"Top 10 Tags: {self.top_10_tags}\n\n")
            count = 1
            for data in self.full_data:
                file.write(f'Quote - {count}\n')
                file.write(f"Author: {data['author']}\n")
                file.write(f"Quote : {data['quote']}\n")
                file.write(f"Tags  : {','.join(data['tags'])}\n")
                file.write("\n")
                count += 1
    
    def save_author_file(self):
        with open('author-details.txt','w',encoding='utf-8') as file:
            for data in self.author_details:
                file.write(f"Author: {data['author']}\n")
                file.write(f"Born Date: {data['born_date']}\n")
                file.write(f"Born Location: {data['born_location']}\n")
                file.write(f"Description: {data['description']}\n\n")

    def run(self):
        self.scrape_logic()
        self.scrape_author_details()
        self.save_quote_file()
        self.save_author_file()

quote_scrape = QuoteScrape(10)
quote_scrape.run()