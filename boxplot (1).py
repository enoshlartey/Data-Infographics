# draw multiple boxplots
from SimpleGraphics import *

# draw a boxplot
# parameters:
#   x -- x-coordinate of the top-left corner of the box
#   y -- y-coordinate of the top-left corner of the box
#   w -- width of the box
#   h -- height of the box
#   median -- the y-coordinate of the line of median
#   max -- the y-coordinate of the maximum value
#   min -- the y-coordinate of the minimum value
# return:
#   nothing
def drawBoxplot(x, y, w, h, median, max, min):

    # draw box
    rect(x, y, w, h)

    # draw median, max and min
    line(x, median, x+w, median)
    line(x, max, x+w, max)
    line(x, min, x+w, min)

    # draw vertical lines
    xMidLine = x + w/2
    line(xMidLine, max, xMidLine, y)
    line(xMidLine, y+h, xMidLine, min)    

# The main function
def main():
    drawBoxplot(400, 300, 100, 200, 350, 150, 550)
    drawBoxplot(600, 160, 100, 250, 270, 80, 500)

main()