import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

# The URL of the page you want to scrape
category_url = "https://www.artofmanliness.com/health-fitness/fitness/"
base_url = "https://www.artofmanliness.com/"
all_topics_url = base_url + "all-topics/"

def get_parsed_html(url):
    # Make a request to the website
    r = requests.get(url)
    r.raise_for_status()

    # Parse the HTML of the site
    return BeautifulSoup(r.text, 'html.parser')


soup = get_parsed_html(all_topics_url)
topics = soup.find_all("div", class_= 'aom-archive-col')
# topic_names = []
# topic_dict = {}
# for topic in topics:
    # for i, a_tag in enumerate(a_tags):
    #     if i == 0:
    #         # This is a topic
    #         href = a_tag['href']
    #         if href:
    #             top = href.split(".com/")
    #             topic_name = top[1].replace("/", "")
    #             topic_names.append(topic_name)
    #             topic_dict[topic_name] = []
    #     else:
    #         topic_name = topic_names[-1]
    #         # This is subtopic
    #         href = a_tag['href']
    #         if href:
    #             top = href.split(topic_name + "/")
    #             if len(top) > 1:
    #                 sub_topic_name = top[1].replace("/", "")
    #                 topic_dict[topic_name].append(sub_topic_name)
    #             else:
    #                 top = href.split("tag/")
    #                 print(f"Top at tag {top}")
    #                 sub_topic_name = top[1].replace("/", "")
    #                 topic_dict[topic_name].append(sub_topic_name)

sub_topic_paths = []
for topic in topics:
    a_tags = topic.find_all("a")
    for a_tag in a_tags:
        href = a_tag['href']
        sub_topic_paths.append(href.replace(base_url, ''))

for sub_topic_path in sub_topic_paths[1:3]:
    sub_topic_soup = get_parsed_html(base_url + sub_topic_path)
    articles = sub_topic_soup.find_all("article")
    for article in articles:
        a_tag = article.find("a")
        href = a_tag['href']
        if "podcast" not in href:
            article_soup = get_parsed_html(href)
            article = article_soup.find(class_="post-content-column").text
            print(article)



# Example
# topic_dict = {
#     "fitness" : ["weights","cardio"]
# }

# for topic in topic_names:
#     topic_url = base_url + topic + "/"
#     topic_soup = get_parsed_html(topic_url)
#     topic_soup



# Gather Topics from all topics page
# Gather subtopics for each topic
# Make a dictionary of dictionaries: Topics to subtopics, subtopics pointing to titles
# ... Titles pointing to article text
# For each subtopic, gather article titles
# for each article, build article url, and extract text
topics = {

}

# # Find the links to the articles
# articles = soup.find_all("article")
# href_dict = {}
# for article in articles:
#     header = article.find('header')
#     name = header
#     href = article.find('a')['href']
#     href_dict[name] = str(href)

#
# article_url_list = list(href_dict.values())
# print(article_url_list)
#
# for article_url in article_url_list:
#     r = requests.get(article_url)
#
#     # Parse the HTML of the article
#     article_soup = BeautifulSoup(r.text, 'html.parser')
#
#     # Find all p tags
#     p_tags = article_soup.find_all('p')
#
#     # Open a file to write to
#     with open(f"{article_url.split('/')[-2]}.txt", 'w') as f:
#         for tag in p_tags:
#             # write the tag text to the file
#             f.write(tag.get_text())
#             f.write('\n')  # add a newline between paragraphs
#
#     # Sleep for a bit to avoid overwhelming the server
#     time.sleep(2)
#
#













# # Make a request to the website
# r = requests.get("https://www.artofmanliness.com/health-fitness/fitness/how-to-deadlift/")
# r.raise_for_status()
#
# # Parse the HTML of the site
# soup = BeautifulSoup(r.text, 'html.parser')
#
# # Find all p tags
# p_tags = soup.find_all('p')
#
# # Open a file to write to
# with open('article_contents.txt', 'w') as f:
#     for tag in p_tags:
#         # write the tag text to the file
#         f.write(tag.get_text())
#         f.write('\n')  # add a newline between paragraphs






















# # Base URL of the website
# base_url = "https://www.artofmanliness.com"
#
# # URL of the main topics page
# topics_url = f"{base_url}/all-topics/"
#
# # Send a GET request to the main topics page
# topics_response = requests.get(topics_url)
#
# # Create a BeautifulSoup object to parse the HTML content
# topics_soup = BeautifulSoup(topics_response.content, "html.parser")
#
# # Find the links to each topic
# topic_links = topics_soup.find_all("a", class_="category-thumb")
#
# # Iterate over the topic links
# for link in topic_links:
#     topic_url = urljoin(base_url, link["href"])
#
#     # Send a GET request to the topic page
#     topic_response = requests.get(topic_url)
#
#     # Create a BeautifulSoup object to parse the HTML content
#     topic_soup = BeautifulSoup(topic_response.content, "html.parser")
#
#     # Find the links to each article within the topic
#     article_links = topic_soup.find_all("a", class_="entry-title-link")
#
#     # Iterate over the article links
#     for article_link in article_links:
#         article_url = urljoin(base_url, article_link["href"])
#
#         # Send a GET request to the article page
#         article_response = requests.get(article_url)
#
#         # Create a BeautifulSoup object to parse the HTML content
#         article_soup = BeautifulSoup(article_response.content, "html.parser")
#
#         # Find the article title and content
#         article_title = article_soup.find("h1", class_="entry-title").text
#         article_content = article_soup.find("div", class_="entry-content").text
#
#         # Save the article title and content to a file
#         with open(f"{article_title}.txt", "w", encoding="utf-8") as file:
#             file.write(article_content)
#
# url = "https://www.artofmanliness.com/health-fitness/fitness/"
# response = requests.get(url)
# html_content = response.text
#
# soup = BeautifulSoup(html_content, "html.parser")
#
# article_links = soup.find_all("a", class_="entry-title-link")
#
# for link in article_links:
#     article_url = link["href"]
#     article_response = requests.get(article_url)
#     article_content = article_response.text
#
#     # Save the article content to a file or process it as needed
#     # For example, you can save it to a text file:
#     with open("article.txt", "w", encoding="utf-8") as file:
#         file.write(article_content)


