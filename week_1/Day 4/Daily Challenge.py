#Daily Challenge: Pagination

import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0  
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        if page_num < 1:
            raise ValueError("Page number must be >= 1")
        if page_num > self.total_pages:
            self.current_idx = self.total_pages - 1  
        else:
            self.current_idx = page_num - 1
        return self  

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        visible_items = self.get_visible_items()
        return "\n".join(str(item) for item in visible_items)
if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    print("Page 1 items:", p.get_visible_items())

    p.next_page()
    print("Page 2 items:", p.get_visible_items())

    p.last_page()
    print("Last page items:", p.get_visible_items())

    p.go_to_page(7)
    print("Current page:", p.current_idx + 1)

    try:
        p.go_to_page(0)
    except ValueError as e:
        print("Error:", e)
