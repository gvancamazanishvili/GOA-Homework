# 3) შემოატანინეთ მომხმარებელს ასაკი integer-ის სახით, თუ ასაკი ნაკლები იქნება 18 გამოიტანეთ "შესვლა აკრძალულია", სვხა შემთხვევაში "Processing Data...."


age = int (input("Enter your age"))
if age < 18:
    print ("შესვლა აკრძალულია")
 
else:
    print ("Processing Data....")
    