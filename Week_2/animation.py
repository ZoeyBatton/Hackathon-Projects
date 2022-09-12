import time 
import os 

all_animation = ["Move It","  Move It","      Move It","          Move It","              Move It","                  Move It","                      Move It","                          Move It","                              Move It"
,"                                  Move It","                                     Move It"]
counter = 0
total_animation = len(all_animation)
def Make_It_Move():
    global counter
    while counter < total_animation:
        print(all_animation[counter])
        time.sleep(.2)
        # the_time
        os.system('cls||clear')
        counter = counter + 1
    counter = 0
    Make_It_Move()
Make_It_Move()
