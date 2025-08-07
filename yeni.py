import random
import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch The Turtle")
drawing_board.bgpic("Su Altı Canlılığı ve Mercanlar.gif")

# Global değişkenler
score = 0
game_over = False

turtle_list = []
fake_turtle_list = []

score_turtle = turtle.Turtle()
def setup_score_turtle():
    score_turtle.penup()
    score_turtle.color("dark blue")
    score_turtle.hideturtle()
    score_turtle.setpos(0, 350)
    score_turtle.write("Score: {}".format(score), move=False, align="center", font=("Arial", 30, "normal"))

# Turtle oluşturma fonksiyonu
def make_turtle(x, y):
    t = turtle.Turtle()
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("green")
    t.goto(x * 15, y * 15)
    t.hideturtle()

    def handle_click(x_click, y_click):
        global score
        if not game_over:
            score += 1
            score_turtle.clear()
            score_turtle.write("Score: {}".format(score), move=False, align="center", font=("Arial", 30, "normal"))

    t.onclick(handle_click)
    turtle_list.append(t)

def make_fake_turtle(a,b):
    t = turtle.Turtle()
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("red")
    t.goto(a * 15, b * 15)
    t.hideturtle()

    def handle_click(a_click,b_click):
        global score
        if not game_over:
            score -= 1
            score_turtle.clear()
            score_turtle.write("Score: {}".format(score), move=False, align="center", font=("Arial", 30, "normal"))

    t.onclick(handle_click)
    fake_turtle_list.append(t)

def setup_fake_turtles():
    fake_coords = [
        (-25, 25), (-15, 25), (25, -25), (25, 5), (-25, -15),
        (-10, 20), (10, -20), (15, 15), (-15, -10), (0, 0),
    ]
    for a, b in fake_coords:
        make_fake_turtle(a, b)

x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]

# Tüm turtle'ları oluştur
def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def hide_fake_turtles():
    for t in fake_turtle_list:
        t.hideturtle()


def make_fake_turtles():
    pass

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        hide_fake_turtles() # sahte turtle'ları da gizle

        # Gerçek turtle'lardan birini göster
        random.choice(turtle_list).showturtle()

        if random.random() < 0.8 and fake_turtle_list:
            fake_count = random.randint(2, 4)  # 2 ile 4 arasında sahte turtle göster
            fake_samples = random.sample(fake_turtle_list, k=min(fake_count, len(fake_turtle_list)))
            for fake in fake_samples:
                fake.showturtle()

        drawing_board.ontimer(show_turtles_randomly, 500)

# Sayaç turtle'ı
countdown_turtle = turtle.Turtle()

def countdown(time):
    global game_over
    countdown_turtle.penup()
    countdown_turtle.color("black")
    countdown_turtle.hideturtle()
    countdown_turtle.setpos(0, 300)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.write("Time: {}".format(time), move=False, align="center", font=("Arial", 30, "normal"))
        drawing_board.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        hide_turtles()
        countdown_turtle.write("Game Over!", move=False, align="center", font=("Arial", 30, "normal"))


turtle.tracer(0)
setup_turtles()
setup_score_turtle()
hide_turtles()
setup_fake_turtles()
show_turtles_randomly()
countdown(20)
turtle.tracer(1)
turtle.mainloop()
