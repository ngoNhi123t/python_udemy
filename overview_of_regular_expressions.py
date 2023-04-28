# kieemr tra oo input với regular express / regEx
#regEX hay regular expression: biểu thức chính quy
#chuỗi kí tự đặc biệt được định nghĩa tạo nên các mẫu (pattern). Được sử dụng để: phaant ích cú pháp, sự trùng khớp, tìm kiếm, thay thế trong các chuỗi và đoạn kí tự.
# abcd...: chữ
#123...: số
# \d: bất cứ số nào
# \D: bất kì gì trừ số
# .: bất cứ kí tự nào
# [abc]: chỉ a,b hoặc c  
# [^abc]: ko có a,b,c 
# [0-9]: số từ 0-9
# \w: bất cứ ký tự chữ nào
# \W: bất cứ gì trừ chữ
# {m}: lặp lại m lần
# {m,n}: lặp lại tối thiểu m lần và tối đa n lần
# "^": kí tự bắt đầu của chuỗi nhập: vd: ^A 
# "$": kí tự kết thúc
# ".": bất cứ ký tự nào, xuống dòng bị loại trừ
# "*": các kí tự trc có thể lặp 0 hoặc nhiều lần
# vd: "ri*l": riiil, riil, rl.
# "+"kí tự trước nó lặp 1 hoặc nhiều lần
# => tác dụng : kiểm tra tính hợp lệ haowcj tìm kiếm và thay thế


### chi tiết
#\s: kí tự khoảng trắng
#\S: ko pải khoảng trắng thay thế ^\s
#\b: thuộc a-z hoặc A-Z, 0-9 hoặc _
#a|b: a hoặc b
# i: tìm kiếm ko phân biệt hoa thường
#m: tìm kiếm nhiều dòng
#u đối sánh chính xác các mẫu được mã hóa bởi UTF-8
#/ bắt đâu haowcj kết thức chuỗi
#\ biểu diện một kí tự ngAy sau, từ kí tự đb thành kí tự thường và ngược lại

###SEARCHING FOR BASIC PATTERNS

text =" The person's phone number is 488-555-1234. Call soon"
print('phone' in text)
import re
pattern ='phone'
print(re.search(pattern,text))
match = re.search(pattern,text)
print(match)
print(match.span())
print(match.start())
### tìm tất cả 

text1 =" the phone is the phone hi phone"
matches = re.findall("phone", text1)
print(matches)
print(len(matches))
###To get actual match objects, use the iterator:
for match in re.finditer("phone", text1):
    print(match.span())
# group()
print(match.group())

#####
text =" The person's phone number is 488-555-1234. Call soon"
#r'mypattern'
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print(phone)
phone1 = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone1)

### group 
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results= re.search(phone_pattern, text)
print(results.group())

## Can then also call by group position.
# remember groups were separated by parenthesis ()
# Something to note is that group ordering starts at 1. Passing in 0 returns everything
###

print(results.group(2))


####Or operator |
print(re.search(r'man|woman','This man was here'))
###The Wildcard Character
print(re.findall(r".at","The cat in the hat sat here.")
      )
print(re.findall(r"....at","The cat in the hat sat here."))
print(re.findall(r"...at","The bat went splat"))
print(re.findall(r"\S+at","The bat went splat"))
#Starts with and Ends With
# We can use the ^ to signal starts with, and the $ to signal ends with:
#cuối chuỗi
print(re.findall(r".at$","The bat went splat"))
#đầu chuỗi
print(re.findall(r"^\w","1 The bat went splat"))

####Exclusion

## sử dụng ^ kết hợp [], bất kì gì trong ngawocj đều bị loại trừ

## vd:
phrase = "there are 3 numbers 34 inside 5 this sentence."
print(re.findall(r'[^\d]+',phrase))
print(re.findall(r'[^abc]+', phrase))
clear = 's'.join(re.findall(r'[^\s]+',phrase))
print(clear)

text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
print(re.findall(r'[\w]+-[\w]+',text))

###Parenthesis for Multiple Options
# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"
re.search(r'cat(fish|nap|claw)',text)
re.search(r'cat(fish|nap|claw)',texttwo)
# None returned
re.search(r'cat(fish|nap|claw)',textthree)
