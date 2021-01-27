from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_position = [(20,0), (0,0), (-20,0)]
        self.segments = []
        self.distance = 20
        self.init_snake_position()
        self.head = self.segments[0]
        
    def init_snake_position(self):
        for position in self.snake_position:
            self.add_segment(position)
            
    
    def add_segment(self, position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)

            self.segments.append(new_segment)

    
    def move(self):
        
        for segment in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment-1].xcor()
            new_y = self.segments[segment-1].ycor()
            self.segments[segment].goto(new_x, new_y)

        self.head.forward(self.distance)
        

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            
        
        
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
        
       

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            
        

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
  

    def extend(self):
        self.add_segment(self.segments[-1].position())
        


        