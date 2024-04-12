from basic_decor_library.Workbook import Workbook
from models.Category.Category import Category

class FilteredReviewsFile(Workbook):
    def __init__(self):
        super().__init__()

    def write_data(self, categories: list[Category]):
        header_col_index = self.find_column_index("Header")
        keywords_col_index = self.find_column_index("Keywords")
        description_col_index = self.find_column_index("Description")
        og_title_col_index = self.find_column_index("og:title")
        og_url_col_index = self.find_column_index("og:url")

        start_row_index = self._sheet.max_row + 1

        for index, category in enumerate(categories):
            self._sheet.cell(row=start_row_index + index, column=header_col_index).value = category.header
            self._sheet.cell(row=start_row_index + index, column=keywords_col_index).value = category.keywords
            self._sheet.cell(row=start_row_index + index, column=description_col_index).value = category.description
            self._sheet.cell(row=start_row_index + index, column=og_title_col_index).value = category.og_title
            self._sheet.cell(row=start_row_index + index, column=og_url_col_index).value = category.og_url

        self.save_workbook()
