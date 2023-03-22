import xlrd


class Parser:

    workbook: xlrd.book
    worksheet: xlrd.book.XL_WORKSHEET

    def __init__(self, schedule_path):
        try:
            self.workbook = xlrd.open_workbook(schedule_path, formatting_info=True)
        except FileNotFoundError as err:
            print(err)
        except IsADirectoryError:
            print("AAAA")
        self.worksheet = self.workbook.sheet_by_index(0)

    def get_merged_cell_value(self, row, col) -> str:
        merged_cells = self.worksheet.merged_cells
        # Iterate over the merged cell ranges
        for merged_cell in merged_cells:
            # Check if the cell is in this merged cell range
            if merged_cell[0] <= row < merged_cell[1] and merged_cell[2] <= col < merged_cell[3]:
                # Get the value of the top-left cell in the range
                value = self.worksheet.cell_value(merged_cell[0], merged_cell[2])
                return value

    def parse_nominator_schedule(self, course_num, group_num, subgroup_num) -> list:
        group_index = self.__get_group_index(group_num, course_num, subgroup_num)
        schedule_numerator = []
        col_start = 4
        for i in range(col_start, self.worksheet.nrows):
            if self.worksheet.cell_value(i, 1) != '':
                val = self.get_merged_cell_value(i, group_index)
                if val is None:
                    val = self.worksheet.cell_value(i, group_index)
                schedule_numerator.append([self.get_merged_cell_value(i, 0), self.get_merged_cell_value(i, 1), val])
        return schedule_numerator

    def parse_denominator_schedule(self, course_num, group_num, subgroup_num) -> list:
        group_index = self.__get_group_index(group_num, course_num, subgroup_num)
        schedule_denominator = []
        i = 5
        while i <= self.worksheet.nrows - 1:
            val = self.get_merged_cell_value(i, group_index)
            if val is None:
                val = self.worksheet.cell_value(i, group_index)
            schedule_denominator.append([self.get_merged_cell_value(i, 0), self.get_merged_cell_value(i, 1), val])
            delimiter_list = [19, 36, 53, 70, 87]
            if i in delimiter_list:
                i += 1
            i += 2
        return schedule_denominator

    def __get_course(self, course_num):
        first_course = range(2, 34)
        second_course = range(35, 62)
        third_course = range(62, 82)
        fourth_course = range(82, self.worksheet.ncols)
        match course_num:
            case 1:
                return first_course
            case 2:
                return second_course
            case 3:
                return third_course
            case 4:
                return fourth_course

    def __get_group_index(self, group_num, course_num, subgroup_num):
        course_range = self.__get_course(course_num)
        curr_group = f'{group_num}группа'
        print(curr_group)
        group_index = -1
        for i in course_range:
            if self.worksheet.cell_value(1, i).replace(' ', '') == curr_group:
                if subgroup_num == 2:
                    group_index = i + 1
                else:
                    group_index = i
                break
        print(group_index)
        return group_index
