import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Three Bouncing Balls")

    canvas = tk.Canvas(window, width=600, height=400, bg="white")
    canvas.pack()

    balls = []
    colors = ["red", "blue", "green"]
    positions = [100, 300, 500]

    ground = 350

    # Get the starting heights
    for i in range(3):
        height = float(input("Initial drop height for ball " +
                             str(i + 1) + " in meters: "))

        if height <= 0:
            window.destroy()
            print("Height must be greater than zero.")
            return

        circle = canvas.create_oval(
            positions[i] - 20, 10,
            positions[i] + 20, 50,
            fill=colors[i]
        )

        # Height, bounces, circle, y, direction, start
        balls.append([height, 0, circle, 10.0, 1, height])

    def bounce():
        active = False

        for i in range(3):
            ball = balls[i]

            height = ball[0]
            bounces = ball[1]
            circle = ball[2]
            y = ball[3]
            direction = ball[4]
            start = ball[5]

            if direction == 0:
                continue

            active = True

            # Calculate bounce height
            top = ground - 340 * (height / start)

            # Move down
            if direction == 1:
                y = y + 5

                if y >= ground:
                    y = ground
                    bounces = bounces + 1
                    height = height * 0.6

                    if height < 0.001:
                        direction = 0
                    else:
                        direction = -1

            # Move up
            else:
                y = y - 5

                if y <= top:
                    y = top
                    direction = 1

            canvas.coords(
                circle,
                positions[i] - 20, y,
                positions[i] + 20, y + 40
            )

            ball[0] = height
            ball[1] = bounces
            ball[3] = y
            ball[4] = direction

        if active:
            window.after(20, bounce)
        else:
            for i in range(3):
                print("Ball", i + 1, "bounced",
                      balls[i][1], "times.")

    bounce()
    window.mainloop()

main()
