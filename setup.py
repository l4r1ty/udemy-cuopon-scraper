import time

f = open("secret.py", "w")
dict={}
username=input("Enter reddit username:\n")
f.write("username=\""+username+"\"")
password=input("Enter reddit password:\n")
f.write("\npassword=\""+password+"\"")
client_id=input("Paste the client id:\n")
f.write("\nclient_id=\""+client_id+"\"")
client_token=input("Paste client token (secret):\n")
f.write("\nclient_token=\""+client_token+"\"")
f.write("\nuser_agent=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36\"")
src_mail=input("Enter source mail address, which is used to send the mail about the new coupons\n")
print("\nMake sure, you enabled less secure apps on this account!\n")
time.sleep(2)
f.write("\nsrc_mail=\""+src_mail+"\"")
mail_pw=input("Enter the source mail's password:\n")
f.write("\nmail_pw=\""+mail_pw+"\"")
dst_mail=input("Enter the destination mail address, where you will receive the mails about the coupons:\n")
f.write("\ndst_mail=\""+dst_mail+"\"")
print("Secret file generated successfully!")
f.close()

f = open("keywords.txt", "w")
print("\n\nEnter keywords you are interested in. Separate the keywords with space.\nFor example: docker python kubernetes etc.")
keywords=input()
f.write(keywords)
print("Keywords file generated successfully!")
f.close()