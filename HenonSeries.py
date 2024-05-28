import math
import turtle

class Iteration:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = 0
        self.y = 0

    def iterateX(self):
        result = self.y + 1 - self.a * self.x ** 2
        self.x = result
        return result

    def iterateY(self):
        result = self.b * self.x
        self.y = result
        return result

    def runIterations(self, num_iterations):

        for i in range(num_iterations):
            x_result = self.iterateX()
            y_result = self.iterateY()
            
            print(f"x{i+1} = {x_result}")
            print(f"y{i+1} = {y_result}")

        self.drawGraphAxe(5, 6)

    def drawGraphAxe(self, Xdataset, Ydataset):
         # Création de la fenêtre turtle
        turtle.setup(800, 600)
        # turtle.speed(0)
        # turtle.penup()

        # turtle.goto(0 * 100, 0 * 100)
        # turtle.dot()
        
        # Dessiner l'axe x
        turtle.forward(200)
        turtle.stamp()
        turtle.write("X", font=("Arial", 12, "normal"))
        turtle.backward(200)

        # Dessiner l'axe y
        turtle.left(90)
        turtle.forward(200)
        turtle.stamp()
        turtle.write("Y", font=("Arial", 12, "normal"))
        turtle.backward(200)
        turtle.right(90)

        # Cacher la tortue et afficher le dessin
        turtle.hideturtle()
        turtle.done()

if __name__ == "__main__":
    iteration = Iteration(a=1.4, b=0.3)
    iteration.runIterations(500)
