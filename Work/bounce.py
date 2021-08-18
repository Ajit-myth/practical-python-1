# bounce.py
#
# Exercise 1.5
ball_ht = 100.0 #metres
bounce_ht = 0.6 #is it floating

for i in range(1,11):
    ball_ht = round(ball_ht * bounce_ht, 4)
    print (i,ball_ht)

    
