def sort_by_column(self, csv_cont, col, reverse=False):
        """
        Sorts CSV contents by column name (if col argument is type <str>)
        or column index (if col argument is type <int>).

        """
        header = csv_cont[0]
        body = csv_cont[1:]
        if isinstance(col, str):
            col_index = header.index(col)
        else:
            col_index = col
        body = sorted(body,
               key=operator.itemgetter(col_index),
               reverse=reverse)
        body.insert(0, header)
        return body