subscription = str(input("Please sign up for Programmer's Toolkit Monthly Subsciption from Platinum, Gold, Silver, Bronze or Free Trial:"))

if subscription == "Platinum":
    print("Platinum subscription is $60 with a monthly gift of programming books!")
elif subscription == "Gold":
    print("Gold subscription is $50 with a monthly gift of figurines!")
elif subscription == "Silver":
    print("Silver subscription is $40 with a monthly gift of t-shirts!")
elif subscription == "Bronze":
    print("Bronze subscription is $30 with a monthly gift of stickers!")
else:
    print("Free trial subscription is free for 30 days with no monthly gift!")