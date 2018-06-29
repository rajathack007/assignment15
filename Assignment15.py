#Q.1..Extract The user id,domain name and suffix from the following email address.
import re
e1="zuck26@facebook.com"
e2="page33@google.com"
e3="jeff42@amazon.com"
p=re.compile(r"([a-z0-9].+)@([a-z].+)\.([a-z].*)")
r1=p.findall(e1)
r2=p.findall(e2)
r3=p.findall(e3)
print(r1)
print(r2)
print(r3)

#Q.2.retrive all the  words starting with b or B from The following text...
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
p=re.compile(r"\b[Bb]\w+")
result=p.finditer(text)
for r in result :
    print(r)
#Q.3- Split the following irregular sentence into words 
sentence = "A, very very; irregular_sentence"
p=re.sub(r"[^a-zA-Z]"," ",sentence)
print(p)
#Q.1- Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs. 
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
p = re.sub(r"https?://[a-zA-Z]\.[a-zA-z0-9]+/[a-zA-Z0-9]+ [a-za-z:?]+ @[a-z]+ #?[a-z]+","",tweet)
q=re.sub(r"!|RT|@TheNextWeb:","",p)

print(q)

         
