def strawberries(rows, columns, days, dead_strawberries):
    if rows in range(columns) and columns in range(1000) and days in range(1000):
        alive_strawberries = (rows * columns) - len(dead_strawberries)
        neighbours = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for day in range(days):
            result = []
            for strawberry in dead_strawberries:
                for neighbour in neighbours:
                    new_strawberry = (strawberry[0] + neighbour[0], strawberry[1] + neighbour[1])
                    if new_strawberry[0] in range(rows) and new_strawberry[1] in range(columns):
                        if new_strawberry not in dead_strawberries and new_strawberry not in result:
                            result.append(new_strawberry)
                            alive_strawberries -= 1
            for strawberry in result:
                dead_strawberries.append(strawberry)
        return alive_strawberries
    else:
        raise ValueError()
