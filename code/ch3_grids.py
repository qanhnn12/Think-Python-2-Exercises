from ch3_do_twice import do_four, do_twice


# Grid with 2 columns and 2 rows

def two_row():
    print('+', '- '*4 + '+', '- '*4 + '+')


def two_col():
    print('|', ' '*7, '|', ' '*7, '|')


def above_two_grid():
    two_row()
    do_four(two_col)


def two_grid():
    do_twice(above_two_grid)
    two_row()


# Grid with 4 rows and 4 columns

def four_row():
    print('+', '- '*4 + '+', '- '*4 + '+', '- '*4 + '+', '- '*4 + '+')


def four_col():
    print('|', ' '*7, '|', ' '*7, '|', ' '*7, '|', ' '*7, '|')


def above_four_grid():
    four_row()
    do_four(four_col)


def four_grid():
    do_twice(above_four_grid)
    four_row()
    do_four(four_col)
    four_row()


if __name__ == '__main__':
    print('This is a grid with 2 rows and 2 columns:')
    two_grid()
    print('This is a grid with 4 rows and 4 columns:')
    four_grid()