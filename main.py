# def mint_chocolate():
#     print("Yum")

# def french_vanilla():
#     print("Yuck")

# mint_chocolate()
# french_vanilla()

# def say_hello(user_name, pet):
#   print(f"hello! good morning, {user_name}, and, {pet}")

# say_hello("human", "canine")
# say_hello(23+46, 21+399)

# def tax_calc(og_value):
#   return og_value * 0.35
# def pay_tax(tax):
#   print("Transaction Succesful", tax)
# to_pay = tax_calc(18)
# pay_tax(to_pay)

# mint_chocolate = True
# french_vanilla = False

# if mint_chocolate:
#   print("Mint Chocolate Best")
# else:
#   print("Mint Chocolate Toothpaste")

# winner = 8
# if winner >= 12:
#   print("Daddy?")
# elif winner >= 8:
#   print("Smash")
# elif winner < 8:
#   print("Lol")

# age = int(input("Are you old enough for the smutty smut?"))

# if age < 18:
#   print("No smutty smut for you")
# elif age > 18:
#   print("Go to school.")
# else:
#   print("Congratulations on becoming on adult!")

# 3.4
"""
from random import randint

user_choice = int(input("Choose a number 1-100"))

pc_choice = randint(1, 100)

if user_choice == pc_choice:
  print("w luck")
elif user_choice > pc_choice:
  print("Skill issue, go lower. PC chose", pc_choice)
elif user_choice < pc_choice:
  print("Skill issue, go higher. PC chose", pc_choice)
"""

# 3.5
"""
size = 0
while size <= 20:
  print("I'm growing:", size, "in.")
  size = size + 1
  """

# 3.6 & #3.7
"""
from random import randint

pc_choice = randint(1, 100)

playing = True

while playing: 
  user_choice = int(input("Choose a number 1-100: "))
  if user_choice == pc_choice:
    print("w luck")
    playing = False
  elif user_choice > pc_choice:
    print("Skill issue, go lower.")
  elif user_choice < pc_choice:
    print("Skill issue, go higher.")
  """

# 4.0 | Homework: Find out the shortcut for emoji keyboard
"""
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

print(days_of_week)

days_of_week.append(["Saturday", "Sunday"])

print(days_of_week)
"""

# 4.2
"""
pies = ["Apple", "Peach", "Grape","Cream 😩"]

print(pies)

"""

# 4.3
"""
player = {
  'name': 'Paul',
  'age': 12,
  'lactose': 'tolerant' , 
  'Hotel' : 'triviago' ,
  'Status' : '💀'
}
print(player.get('lactose'))
print(player)
player.pop('lactose')
print(player)
#"""
# 4.5 - #4.8
"""

from requests import get

websites = [
  "https://archiveofourown.org",
  "tumblr.com",
  "twitter.com",
  "google.com" ,
  "facebook.com"
]

results = {
 
}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  if response.status_code == 200:
    results[website] = "Ok"
    #print(f"{website} has wakey-wakied.")
  else:  
    results[website] = "Not okay"
    #print(f"{website} has NOT wakey-wakied.")


print(results)
#"""
# nums = [1,3,5,7,9]

# index = 0
# for num in nums:
#   print(index," : ",num)
#   index = index + 1
# 0 : 1
# 1 : 3
# 2 : 5
# 3 : 7
# 4 : 9

# nums = [9,1,3,5,7,9,11,13]

# enum = enumerate(nums)


# print(1 in nums)
# print(1 not in nums)
# print(1 + 2)
# print("1" + "2")
# print( 2 * 3)
# for index, num in enumerate(nums):
#   print(index," : ",num)

# print(nums[0])
# print(nums[1:3])

# print(nums[1:6:2])

# print(len(nums))
# print(min(nums))
# print(max(nums))

# print(nums.index(x[, 0[, 7]]))
# print(nums.count(1))


# for index, num in enumerate(nums):
#   if num % 2 == 0:
#     print(num, " : ","even")
#   else:
#     print(num, " : ","odd")

# for num in range(10):
#   if num % 2 == 0:
#     print(num, " : ","even")
#   else:
#     print(num, " : ","odd")


# for num in (range(9)):
#   print(num)

# 2 x 1 = 2

# #5-3
# from requests import get

# og_url = "https://weworkremotely.com/remote-jobs/search?utf8=&term="
# searched_term = "python"

# response = get(f"{og_url}{searched_term}")
# if response.status_code != 200:
#   print("Can't request website")
# else:
#   print(response.text)

# #5-4

# from bs4 import BeautifulSoup
# og_url = "https://weworkremotely.com/remote-jobs/search?utf8=&term="
# searched_term = "python"

# response = get(f"{og_url}{searched_term}")
# if response.status_code != 200:
#   print("Can't request website")
# else:
#   soup = BeautifulSoup(response.text, "html.parser")
#   print(soup.find_all('section', class_="jobs"))
# print("Initial Commit")
# print("Hello !!")


#5-8
# from requests import get
# from bs4 import BeautifulSoup

# og_url = "https://weworkremotely.com/remote-jobs/search?utf8=&term="
# searched_term = "python"

# response = get(f"{og_url}{searched_term}")
# if response.status_code != 200:
#   print("Can't request website")
# else:
#   results = []
#   soup = BeautifulSoup(response.text, "html.parser")
#   jobs = soup.find_all('section', class_="jobs")
#   for job_section in jobs:
#     job_posts = job_section.find_all('li')
#     job_posts.pop(-1)
#     for post in job_posts:
#       anchors = post.find_all('a')
#       anchor = anchors[1]
#       link = anchor['href']
#       company, kind, region = anchor.find_all('span', class_='company')

#       title = anchor.find('span', class_='title')
#       job_data = {
#         'company': company.string,
#         'region': region.string,
#         'position': title.string
#       }
#       results.append(job_data)
#       #print(company.string, kind.string, region.string, title.string)
# for result in results:
#   print(result)
#   print("///////////////////")

# for nums in range(2, 10):
#   n = 1
#   while n < 10:
#     print(f"{nums} x {n} = {nums*n}") 
#     n = n+1
#     if n == 10:
#       print()


# print(abs(10))
# print(abs(-10))

# print (max( 4,12,43.3,19,100 ) )


# Intermission: Gugudan

# print("What Dan?")
# input_dan = int(input())
# print(f"inputed : {input_dan}")

# for num in range(9):
#   print(f"{input_dan} x {num+1} = {input_dan * (num+1)}")

#5.10
# from requests import get
# from bs4 import BeautifulStoneSoup
# from extractors.wwr import extract_wwr_jobs

#jobs = extract_wwr_jobs("python")
#print(jobs)

# base_url = "https://kr.indeed.com/jobs?q="
# search_term = "python"

# response = get(f"{base_url}{search_term}")

# if response.status_code != 200:
#     print("Cannot request page")
# else:
#     soup = BeautifulSoup(response.text, "html.parser")
#     job_list = soup.find("ul", class_="jobsearch-ResultsList")
#     jobs = job_list.find_all('li', recursive=False)
#     for job fin jobs:
#       print(jobs)
#       print("/////////")

# 

# from requests import get
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_experimental_option("detach", True)  # 브라우저 꺼짐 방지 코드
# browser = webdriver.Chrome(options=options)
# browser.get(
#     'https://kr.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=89395b6ac5014113')

# print(browser.page_source)

# jobs = extract_wwr_jobs("python")
# print(jobs)

# base_url = "https://kr.indeed.com/jobs?q="
# search_term = "python"

# response = get(f"{base_url}{search_term}")

# if response.status_code != 200:
#     print("Cannot request page")
# else:
#     soup = BeautifulSoup(response.text, "html.parser")
#     job_list = soup.find("ul", class_="jobsearch-ResultsList")
#     jobs = job_list.find_all('li', recursive=False)
#     for job in jobs:
#       zone = job.find("div", class_="mosiac-zone")
#       if zone == None:
#          print("Job li")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from requests import get

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("detach", True)  # 브라우저 꺼짐 방지 코드
browser = webdriver.Chrome(options=options)
base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"
# response = get(f"{base_url}{search_term}")


browser.get(
    f"{base_url}{search_term}")

# if response.status_code != 200:
#      print("Cannot request page")
# else:
soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = job_list.find_all('li', recursive=False)
results = []
for job in jobs:
     zone = job.find("div", class_="mosaic-zone")
     if zone == None:        
        anchor = job.select_one("h2 a")
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
            'link': f"https://kr.indeed.com{link}",
            'company': company.string,
            'location': location.string,
            'position': title
          }

        results.append(job_data)

# print(results)
for result in results:
    print(result, "/////////\n")
# print("\n////////\n")