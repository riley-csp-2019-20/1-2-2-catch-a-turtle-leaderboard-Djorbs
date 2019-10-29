#-----import statements-----
import turtle as trtl
import random
import leaderboard as lb
#-----game configuration----
shape = "turtle"
size = 2
color = "brown"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 20
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#leaderboard variables
leaderboard_file_name = "a112_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name~ ")
#-----initialize turtle-----
polnareff = trtl.Turtle(shape = shape)
polnareff.color(color)
polnareff.shapesize(size)
polnareff.penup()
polnareff.speed(0)
scorer = trtl.Turtle(shape = shape)
scorer.ht()
scorer.penup()
scorer.speed(0)
scorer.goto(-420, 350)
counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(340, 350)
#-----game functions--------
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    runturtlerun()
    manage_leaderboard()
    
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
def turtlebooped(x,y):
  change_position()
  score_count()
  polnareff.color(random_color())
def change_position():
  polnareff.ht()
  new_positx = random.randint(-240, 240)
  new_posity = random.randint(-240, 240)
  polnareff.goto(new_positx, new_posity)
  polnareff.st()
def score_count(): 
  global score
  score += 100
  font = ("Arial", 30)
  scorer.clear()
  scorer.write(score, font = font)
def runturtlerun():
  wn.bgcolor(random_color())#This is my customization. The background changes to a random color when the game ends.
  polnareff.ht
  polnareff.goto(999, 999)
def random_color(): #This is my customization. The turtle changes color everytime it is clicked.
  r = random.random()
  g = random.random()
  b = random.random()
  return (r,g,b)
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global giorno

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, giorno, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, giorno, score)

#-----events----------------
wack.onclick(turtlebooped)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()