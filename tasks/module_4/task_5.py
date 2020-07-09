"""Module4/Task5: Spreadsheet Correcter."""

import ezsheets


# Vars
SHEET_TOKEN = '1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg'


def check_error_in_google_spreadsheet() -> list:
    """Check which row in spreadsheet contains incorrect *expression.

    *Expression: beans_per_jar * jars = total_beans
    :return list of incorrect rows (int)
    """
    ss = ezsheets.Spreadsheet(SHEET_TOKEN)

    incorrect_rows = []
    row = 2
    while ss[0].getRow(row)[0]:
        beans_per_jar = int(ss[0].getRow(row)[0])
        jars = int(ss[0].getRow(row)[1])
        total_beans = beans_per_jar * jars

        if beans_per_jar * jars != total_beans:
            print(f'Mistake found at row: {row}.')
            incorrect_rows.append(row)
        row += 1
    return incorrect_rows


if __name__ == '__main__':
    check_error_in_google_spreadsheet()
