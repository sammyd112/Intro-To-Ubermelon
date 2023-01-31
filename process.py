log_file = open("um-server-01.txt")


def generate_sales_reports(log_file):
    for line in log_file:
        """Remove spaces from end of each line"""
        line = line.rstrip()
        """Slice list to index the day"""
        day = line[0:3]
        """Search for Mon in the list"""
        if day == "Mon":
            """Print lines that contain Mon"""
            print(line)


generate_sales_reports(log_file)
