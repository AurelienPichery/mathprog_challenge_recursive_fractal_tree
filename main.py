import turtle

# Instantiate the Turtle
drawer = turtle.Turtle()

# Set the Turtle's parameters
drawer.left(90)
drawer.speed(100)


# Define the recursive function
def tree(i):
    if i > 10:
        # Draw the branch and reorient yourself for the next one
        drawer.forward(i)
        drawer.left(12)

        # Fractal equation determining the next branch size
        tree(6*i/7)

        # Draw the right branch
        drawer.right(24)

        tree(6*i/7)

        # Reorient yourself at the exact same direction of your current branch, and go at the beginning of it
        drawer.left(12)
        drawer.backward(i)


tree(i=100)
turtle.done()  # Keep the window open
