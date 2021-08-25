import os

class AskQuestion():
    print("Hi! I'm bot which help you get titles of website from google")
    website = input("Which phrase do you want to get?: ")
    print(f"Okay! I will print {website}")

    os.system("scrapy crawl google -o google.csv")
