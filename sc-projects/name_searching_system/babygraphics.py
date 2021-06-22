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
    i = 0
    x_coordinate = None
    interval = (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS)
    # return year_index * interval + GRAPH_MARGIN_SIZE
    for year in YEARS:
        if year == year_index:
            x_coordinate = GRAPH_MARGIN_SIZE + interval * i
            break
        else:
            i += 1
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################

    # this is the upper line of the canvas
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # this is the bottom line of the canvas
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    for year in YEARS:
    # for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year), 0,
                           get_x_coordinate(CANVAS_WIDTH, year), CANVAS_HEIGHT
                           , width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year) + TEXT_DX,
                           CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           anchor=tkinter.NW,
                           text=year)


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
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    chart_interval = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / 1000

    color_count = 0

    for name in lookup_names:
        a = 0
        past_x = None
        past_y = None
        if name in name_data:
            new_d = name_data[name]
            print(new_d)
            # {'2010':'57', '2000':'104'}
            for i in range(len(YEARS)):
                key = str(YEARS[i])
                val = new_d.get(key, 1000)
            # for key, val in new_d.items():
            #     print(f'key, val at {a}: {key}, {val}')

                if int(val) < 1000:
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, int(key)) + TEXT_DX,
                                       GRAPH_MARGIN_SIZE + int(val) * chart_interval,
                                       anchor=tkinter.SW, text=name + ' ' + val, fill=COLORS[color_count])
                    current_x = get_x_coordinate(CANVAS_WIDTH, int(key))
                    current_y = GRAPH_MARGIN_SIZE + int(val) * chart_interval
                    if a != 0:  # this is to make sure we start connect dots after the second dot
                        canvas.create_line(past_x, past_y, current_x, current_y, width=LINE_WIDTH,
                                           fill=COLORS[color_count])
                    past_x = current_x
                    past_y = current_y
                    #print(f'val: {val}')
                else:
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, int(key)) + TEXT_DX,
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       anchor=tkinter.SW, text=name + ' *', fill=COLORS[color_count])
                    current_x = get_x_coordinate(CANVAS_WIDTH, int(key))
                    current_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    #print('aaa')
                    if a != 0:  # this is to make sure we start connect dots after the second dot
                        canvas.create_line(past_x, past_y, current_x, current_y, width=LINE_WIDTH,
                                           fill=COLORS[color_count])
                    past_x = current_x
                    past_y = current_y

                a += 1
        color_count += 1
        if color_count == 4:
            color_count = 0


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
