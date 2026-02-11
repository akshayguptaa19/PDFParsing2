# 1. Install and import library

# pip install PyPDF2
# import PyPDF2

# 2. Open a PDF file in read-binary mode
# import PyPDF2

# file = open("sample.pdf", "rb")
# reader = PyPDF2.PdfReader(file)


# 3. Display total number of pages
# print(len(reader.pages))

# 4. Extract text from first page
# print(reader.pages[0].extract_text())

# 5. Extract text from last page
# last_page = len(reader.pages) - 1
# print(reader.pages[last_page].extract_text())

# 6. Extract text from all pages
# for page in reader.pages:
#     print(page.extract_text())

# 7. Save extracted text into .txt file
# text = ""
# for page in reader.pages:
#     text += page.extract_text()

# with open("output.txt", "w", encoding="utf-8") as f:
#     f.write(text)


# 8. Count total characters
# text = ""
# for page in reader.pages:
#     text += page.extract_text()

# print(len(text))

# 9. Count total words
# words = text.split()
# print(len(words))

# 10. Count total lines
# lines = text.split("\n")
# print(len(lines))

# 11. Check whether specific word exists
# word = "Python"
# print(word in text)

# 12. Count how many times a word appears
# print(text.count("Python"))

# 13. Extract text from user-specified page
# page_num = int(input("Enter page number: "))
# print(reader.pages[page_num - 1].extract_text())

# 14. Print number of words on each page
# for i, page in enumerate(reader.pages):
#     words = page.extract_text().split()
#     print(f"Page {i+1}: {len(words)} words")

# 15. Find longest word
# words = text.split()
# print(max(words, key=len))

# 16. Find shortest word
# print(min(words, key=len))

# 17. Print only numeric values
# import re
# numbers = re.findall(r'\d+', text)
# print(numbers)

# 18. Extract email IDs
# emails = re.findall(r'\S+@\S+', text)
# print(emails)

# 19. Extract phone numbers
# phones = re.findall(r'\d{10}', text)
# print(phones)

# 20. Extract only uppercase lin
# for line in text.split("\n"):
#     if line.isupper():
#         print(line)

# 21. Convert text to lowercase
# print(text.lower())

# 22. Remove special characters
# clean = re.sub(r'[^A-Za-z0-9\s]', '', text)
# print(clean)

# 23. Count frequency of each word
# from collections import Counter
# freq = Counter(words)
# print(freq)

# 24. Most frequent word
# print(freq.most_common(1))

# 25. Split text into sentences
# sentences = text.split(".")
# print(sentences)

# 26. Search keyword and show page numbers
# keyword = "Python"
# for i, page in enumerate(reader.pages):
#     if keyword in page.extract_text():
#         print("Found on page:", i+1)

# 27. Merge text from multiple PDFs
# files = ["file1.pdf", "file2.pdf"]
# all_text = ""

# for f in files:
#     file = open(f, "rb")
#     reader = PyPDF2.PdfReader(file)
#     for page in reader.pages:
#         all_text += page.extract_text()

# print(all_text)


# 28. Extract only even-numbered pages
# for i, page in enumerate(reader.pages):
#     if (i+1) % 2 == 0:
#         print(page.extract_text())


# 29. Extract only odd-numbered pages
# for i, page in enumerate(reader.pages):
#     if (i+1) % 2 != 0:
#         print(page.extract_text())

# 30. Handle error if file not found
# try:
#     file = open("sample.pdf", "rb")
# except FileNotFoundError:
#     print("File not found!")




