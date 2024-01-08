"""
Dataset obtained from Data World about Liverpool Football Club and it's Premiership Title challenges.
https://data.world/ryanes/comparing-liverpool-fc-title-challenges
"""
from SimpleGraphics import *


# The function below opens the dataset file, reads it, and returns information requested to be used in other functions.
def fileReader(file_name):
    with open(file_name, "r") as file:
        text = file.readlines()
        header = text[0].strip().split(",")
        data = []
        opponents = {}
        for lineCount in text[1:]:
            values = lineCount.strip().split(",")
            row = {header[i]: values[i] for i in range(len(header))}
            data.append(row)
            # Opponent Counter
            opponent = row["visitor"] if row["home"] == "Liverpool" else row["home"]
            if not opponent in opponents:
                opponents[opponent] = 1
            else:
                opponents[opponent] += 1
        big5Opponents = [
            "Manchester United",
            "Arsenal",
            "Chelsea",
            "Manchester City",
            "Tottenham_Hotspur",
        ]
        points_gained = {team: 0 for team in big5Opponents}
        for j in data:
            home = j["home"]
            visitor = j["visitor"]
            result = j["result"]
            points = int(j["points"])
            if home in big5Opponents:
                points_gained[home] += points
            elif visitor in big5Opponents:
                points_gained[visitor] += points
        # Infographic 3 Information
        games = []
        for game in data:
            game = {
                "hgoal": int(game["hgoal"]),
                "vgoal": int(game["vgoal"]),
                "total_goals": int(game["hgoal"]) + int(game["vgoal"]),
            }
            games.append(game)
        # Below, I am sorting the games dictionars.
        games.sort(key=lambda x: x["total_goals"], reverse=True)
        top4games = games[:4]
    # The return function below returns variables created earlier in the function.
    return (home, visitor, result, points, opponents, points_gained, top4games)


"""Infographic Title and Summary"""


# This function presents all required information such as titles and summary of each infographic.
def infoData():
    infographicTitle = "Liverpool FC Season View"
    infographicOneTitle = "1. Points Gained vs. Traditional Top 5"
    descriptionOne = "In England, there are 6 teams considered as the \n'Traditional Top 6'. That includes Liverpool FC. \nWe look at how many points Liverpool FC were able to \npick up against each of these Top 5 clubs in all \nseasons present in the dataset. \nAs we can see, Liverpool FC picked \nup the most points against Manchester United, \ntheir arch-rivals and picked up the least points against Chelsea."
    infographicTwoTitle = "2. Games vs. Other Team"
    descriptionTwo = "In the graph above, we compare the most games \nLiverpool have played against each club in the dataset. \nThis ranges from the season, 2008 to the season, 2018. \nWe notice an equal amount of \ngames were played against some teams. \nWhile only one team had more games. "
    infographicThreeTitle = "3. Most Goals in Games Involving Liverpool"
    descriptionThree = "Below, we visualize the highest number of goals \nscored in games when Liverpool have been involved. \nThe highest being 9 goals, combine second highest being \n8 goals and third highest being 7 goals. I'm sure this \nstatistic has changed in recent seasons considering \nLiverpool have been at their peak for the past 3 years. "
    return (
        infographicTitle,
        infographicOneTitle,
        infographicTwoTitle,
        infographicThreeTitle,
        descriptionOne,
        descriptionTwo,
        descriptionThree,
    )


# The infoOutlines function draws the outline of each infographic which I will then add more information to later on.
def infoOutlines(infographicTitle):
    """
    The function creates an infographic with a title and three different shapes with different colors
    and outlines.

    :param infographicTitle: A string variable that represents the title of the infographic
    """
    # We begin by resizing the window to allow presentation of all information.
    resize(1700, 1050)
    # Changing the background of the canvas to white.
    background("white")
    setFont("Trebuchet MS", "22", "bold+underline")
    # I am writing up the title of the infographic which I imported from the infoData() function.
    text(850, 40, infographicTitle)
    # Line Divider
    setOutline("white")
    line(0, 56, 1700, 56)
    # Infographic 1
    setFill("cyan")
    setOutline("red")
    ellipse(175, 125, 350, 350)
    # Infographic 2
    setFill("cyan")
    setOutline("black")
    line(1150, 100, 1150, 470, 1600, 470)
    # Infographic 3
    setFill("beige")
    setOutline("light sea green")
    ellipse(720, 680, 250, 250)


# The get_color function is a function set up to allow looping through each color. It takes in one parameter, the index and returns color variable to be used in other functions.
def get_color(index):
    """
    The function returns a color from a list based on the index provided.

    :param index: The index parameter is an integer that represents the position of the desired color in
    the colors list
    :return: a color from the `colors` list based on the `index` parameter passed to the function. The
    color is determined by using the modulo operator to get the remainder of `index` divided by the
    length of the `colors` list, and then using that result as the index to retrieve a color from the
    list.
    """
    # A list containing each of the colors.
    colors = [
        "violet",
        "salmon",
        "orange red",
        "grey",
        "royal blue",
        "medium spring green",
        "powder blue",
        "light blue",
    ]
    color = colors[index % len(colors)]
    return color


def infoGraphicOne(chartTitle, desc1, pointsGained):
    """
    The function creates a pie chart with data on points gained by five football teams and displays it
    with a chart title and description.

    :param chartTitle: The title of the chart/graphic being created
    :param desc1: A description or caption for the chart. It will be displayed below the chart title
    :param pointsGained: A dictionary containing the points gained by a team in a football league
    against the Big 5 opponents (Manchester United, Arsenal, Chelsea, Manchester City, Tottenham
    Hotspur)
    :return: nothing (i.e., None).
    """
    setOutline("blue3")
    setFont("Trebuchet MS", "13", "bold+underline")
    text(355, 520, chartTitle)
    setFont("Trebuchet MS", "13", "normal")
    text(300, 640, desc1)
    # I am setting up a list containing the Big 5 Opponents. We will use this list to trim data originally collected using the fileReader() function.
    big5Opponents = [
        "Manchester United",
        "Arsenal",
        "Chelsea",
        "Manchester City",
        "Tottenham_Hotspur",
    ]

    for team in big5Opponents:
        if team not in pointsGained:
            pointsGained[team] = 0

    numSectors = len(big5Opponents)
    sectorValues = list(pointsGained.values())
    totalValue = sum(sectorValues)
    startAngle = 0

    for j in range(-1, numSectors):
        setFill(get_color(j))
        endAngle = startAngle + (sectorValues[j] / totalValue) * 360
        pieSlice(175, 125, 350, 350, startAngle, endAngle)
        startAngle = endAngle
    for i, team in enumerate(big5Opponents):
        setFill(get_color(i))
        setOutline(get_color(i))
        ellipse(50, 120 + 70 * i, 20, 20)
        setFont("Trebuchet MS", "8")
        setOutline("black")
        text(60, 150 + 70 * i, team)
    return


def infoGraphicTwo(chartTitle, desc2, opponents):
    """
    The function creates a bar graph with the top 5 opponents and their game counts.

    :param chartTitle: The title of the chart/graphic
    :param desc2: Unfortunately, the parameter desc2 is not defined in the code snippet provided. Can
    you please provide more information or context about the function and its parameters?
    :param opponents: The opponents parameter is a dictionary where the keys are the names of the
    opponents and the values are the number of games played against them
    :return: nothing (i.e., None).
    """
    sorted_opponents = sorted(opponents.items(), key=lambda x: x[1], reverse=True)
    top5 = dict(sorted_opponents[:5])
    opponent_name = list(top5.keys())
    opponent_count = list(top5.values())
    max_games = max(opponent_count)

    setOutline("blue3")
    setFont("Trebuchet MS", "13", "bold+underline")
    text(1350, 525, chartTitle)
    setFont("Trebuchet MS", "13", "normal")
    text(1400, 615, desc2)
    setFont("Trebuchet MS", "10", "bold")
    text(1075, 285, "Games Played")
    setFont("Trebuchet MS", "10", "bold")
    text(1375, 480, "Teams")
    text(1135, 470, "0")
    text(1135, 417, "1")
    text(1135, 364, "2")
    text(1135, 311, "3")
    text(1135, 258, "4")
    text(1135, 205, "5")
    text(1135, 152, "6")
    text(1135, 99, "7")

    graphCount = 0
    legend_x = 1580
    for i in range(len(opponent_count)):
        barLabel = opponent_name[i]
        barValue = opponent_count[i]
        color = get_color(i)
        graphCount += 10
        setFill(color)
        setOutline(color)
        rect(
            1200 + graphCount + i * 50,
            470 - barValue * (320 / max_games),
            40,
            barValue * (320 / max_games),
        )
        setFill(color)
        rect(legend_x, 150 + i * 50, 20, 20)
        setFont("Arial", "7")
        setOutline("black")
        text(legend_x + 10, 177 + i * 50, barLabel)
    return


def infoGraphicThree(chartTitle, desc3, top4Goals):
    """
    This function creates an infographic with a chart title, description, and four rectangles displaying
    the total goals for the top four games.

    :param chartTitle: The title of the chart/graphic being created
    :param desc3: A description or explanation related to the chart or the data being presented in the
    chart
    :param top4Goals: A list of dictionaries containing information about the top 4 goalscorers in a
    particular league or competition. Each dictionary contains the name of the player and their total
    number of goals scored
    """
    setOutline("blue3")
    setFont("Trebuchet MS", "13", "bold+underline")
    text(850, 575, chartTitle)
    setFont("Trebuchet MS", "13", "normal")
    text(850, 470, desc3)
    setFill("alice blue")
    setOutline("dodger blue")
    rect_positions = [(795, 640), (915, 753), (795, 860), (680, 753)]
    for i, game in enumerate(top4Goals):
        rect_x, rect_y = rect_positions[i]
        rect(rect_x, rect_y, 100, 100)
        setFont("Trebuchet MS", "10", "bold")
        text(rect_x + 50, rect_y + 32, "Total Goals:")
        setFont("Trebuchet MS", "20", "bold")
        text(rect_x + 50, rect_y + 57, str(game["total_goals"]))


def main():
    """
    This function reads data from a CSV file and uses it to generate three different infographics.
    """
    file_name = "dataset.csv"
    titleMain, titleOne, titleTwo, titleThree, desc1, desc2, desc3 = infoData()
    infoOutlines(titleMain)
    home, visitor, result, points, opponents, pointsGained, top4goals = fileReader(
        file_name
    )
    text = fileReader(file_name)
    infoGraphicOne(titleOne, desc1, pointsGained)
    infoGraphicTwo(titleTwo, desc2, opponents)
    infoGraphicThree(titleThree, desc3, top4goals)


# The `main()` function is the main entry point of the program. It calls other functions to read data
# from a dataset file, draw outlines for three infographics, and then draw the actual data for each
# infographic. Specifically, it calls the `fileReader()` function to read data from the dataset file,
# and then calls the `infoOutlines()`, `infoGraphicOne()`, `infoGraphicTwo()`, and
# `infoGraphicThree()` functions to draw the outlines and data for each infographic.
main()
