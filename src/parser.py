import xlrd

# Open the workbook
workbook = xlrd.open_workbook("./resources/schedule.xls", formatting_info=True)
# Open the worksheet
worksheet = workbook.sheet_by_index(0)


def get_merged_cell_value(row, col) -> str:
    merged_cells = worksheet.merged_cells
    # Iterate over the merged cell ranges
    for merged_cell in merged_cells:
        # Check if the cell is in this merged cell range
        if merged_cell[0] <= row < merged_cell[1] and merged_cell[2] <= col < merged_cell[3]:
            # Get the value of the top-left cell in the range
            value = worksheet.cell_value(merged_cell[0], merged_cell[2])
            return value


def parse_nominator_schedule(group_num) -> list:
    schedule_numerator = []
    col_start = 4
    for i in range(col_start, worksheet.nrows):
        if worksheet.cell_value(i, 1) != '':
            val = get_merged_cell_value(i, group_num)
            if val is None:
                val = worksheet.cell_value(i, group_num)
            schedule_numerator.append([get_merged_cell_value(i, 0), get_merged_cell_value(i, 1), val])
    return schedule_numerator


def parse_denominator_schedule(group_num) -> list:
    schedule_denominator = []
    i = 5
    while i <= worksheet.nrows - 1:
        val = get_merged_cell_value(i, group_num)
        if val is None:
            val = worksheet.cell_value(i, group_num)
        schedule_denominator.append([get_merged_cell_value(i, 0), get_merged_cell_value(i, 1), val])
        delimiter_list = [19, 36, 53, 70, 87]
        if i in delimiter_list:
            i += 1
        i += 2
    return schedule_denominator
