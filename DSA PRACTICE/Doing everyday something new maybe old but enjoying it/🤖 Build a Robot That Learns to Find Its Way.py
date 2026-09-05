#size  of   my  robot's worl

ROWS=10
COLS=10

#Robot  positio
robot_row=4
robot_col=0

#goal position
goal_row=3
goal_col=3


def  show_world():
    for  row in range(ROWS):
        for col in range(COLS):


            if row==robot_row and col==robot_col:
                print("R",end=" ")

            elif row==goal_row and col==goal_col:
                print("G",end=" ")

            else:
                print(".",end=" ")


        print()

    while True:
        direction=input("move  the  robot (w/s/a/d:)").lower()

        if direction=="q":
            print("robot   stopped")
            break

        move_robot(direction)
        show_world()











def move_robot(direction):
    global robot_row,robot_col

    if  direction=="w":
        robot_row-=1

    elif direction=="s":
        robot_row+=1


    elif direction =="a":
        robot_col-=1


    elif direction=="d":
        robot_col+=1






show_world()