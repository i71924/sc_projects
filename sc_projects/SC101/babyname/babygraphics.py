"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    year_width = (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS)
    return GRAPH_MARGIN_SIZE + year_index * year_width


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH, fill='black')
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH, fill='black')
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW,
                           fill='black')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid
    color_index = 0  # identify the color
    for name in lookup_names:
        y1 = 0
        for i in range(len(YEARS)):
            if str(YEARS[i]) in name_data[name] and int(name_data[name][str(YEARS[i])]) <= MAX_RANK:
                if y1 == 0:
                    y1 = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK * int(name_data[name][str(YEARS[i])])
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i), y1, text=name + str(name_data[name][str(YEARS[i])])
                                       , anchor=tkinter.SW, fill=COLORS[color_index % len(COLORS)])
                else:
                    y2 = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK * int(name_data[name][str(YEARS[i])])
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i), y2, text=name + str(name_data[name][str(YEARS[i])])
                                       , anchor=tkinter.SW, fill=COLORS[color_index % len(COLORS)])
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i-1), y1, get_x_coordinate(CANVAS_WIDTH, i), y2,
                                       width=LINE_WIDTH, fill=COLORS[color_index % len(COLORS)])
                    y1 = y2
            else:   # No name in this year or the rank is lower than MAX_RANK
                if y1 == 0:
                    y1 = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i), y1, text=name+'*', anchor=tkinter.SW,
                                       fill=COLORS[color_index % len(COLORS)])
                else:
                    y2 = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i), y2, text=name+'*', anchor=tkinter.SW,
                                       fill=COLORS[color_index % len(COLORS)])
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i-1), y1, get_x_coordinate(CANVAS_WIDTH, i), y2,
                                       width=LINE_WIDTH, fill=COLORS[color_index % len(COLORS)])
                    y1 = y2
        color_index += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()