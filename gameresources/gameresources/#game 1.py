import turtle as trtl
import random as rand
#----initialize------------------------
t = trtl.Turtle()
wn = trtl.Screen()
t.penup()
t.setposition(-500,-300)
t.pendown()
#----variables------------------------
score = 0
level = 1
difficulty = 5
#----functions------------------------
def make_screen():
	t.speed(0)
	t.pencolor("Purple")
	t.pensize(5)
	for x in range(2):
		t.forward(1000)
		t.left(90)
		t.forward(600)
		t.left(90)
	t.penup()
	t.setposition(-250,0)
	t.pendown()
	t.speed(1)

def level_score_update():
	global score
	global difficulty
	score += 1
	print(score)
	stamp_counter = (score)%difficulty
	if stamp_counter == 0:
		t.clearstamps()
		t.clearstamp()
		t.clear()
		global level
		level += 1
		difficulty += 5



	


	

	
def ghost_clicked(x,y):
	t.stamp()
	t.speed(0)
	x = rand.randint(-400, 400)
	y = rand.randint(-200,200)
	t.penup()
	t.setposition(x,y)
	t.pendown()
	level_score_update()




#----game actions-----------------------
wn.bgpic('background.gif')
wn.addshape('ghost.gif')
t.shape('ghost.gif')
make_screen()
t.onclick(ghost_clicked)




wn.mainloop()
