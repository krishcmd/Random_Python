from turtle import *
begin_fill()
while True:
    forward(width)
    left(90)
    forward(height)
    left(90)
    if abs(pos())<1:
        break
end_fill()
done()
