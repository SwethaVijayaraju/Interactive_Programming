# template for "Stopwatch: The Game"
import simplegui
# define global variables
millisecond = 0
total_games = 0
games_won = 0
timer_running = False

def score(total, won):
    return str(won) + "/" + str(total)

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if t < 10:
        return "0:00." + str(t)
    elif t < 600:
        sec = t//10
        if sec < 10:
            return "0:0" + str(sec) + "." + str(t%10)
        else:
            return "0:" + str(sec) + "." + str(t%10)
    else:
        sec = (t%600)//10
        if sec < 10:
            return str(t//600) + ":0" + str(sec) + "." + str((t%600)%10)
        else:
            return str(t//600) + ":" + str(sec) + "." + str((t%600)%10)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer_running
    timer.start()
    timer_running = True

def stop():
    global total_games, games_won, timer_running
    timer.stop()
    if timer_running:
        if millisecond%10 == 0:
            total_games += 1
            games_won += 1
        else:
            total_games += 1
    timer_running = False

def reset():
    global timer_running, millisecond, total_games, games_won 
    timer.stop()
    timer_running = False
    millisecond = 0
    total_games = 0
    games_won = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global millisecond
    millisecond += 1

# define draw handler
def draw_handler(canvas):
    time = format(millisecond)
    canvas.draw_text(time, (115, 150), 32, 'Gray')
    canvas.draw_text(score(total_games, games_won), (250, 30), 24, 'Green')
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 300)
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)

# register event handlers
frame.add_button("Start", start, 50)
frame.add_button("Stop", stop, 50)
frame.add_button("Reset", reset, 50)

# start frame
frame.start()

# Please remember to review the grading rubric
