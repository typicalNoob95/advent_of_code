import math

class OrderingRule:
    def __init__(self, line):
        pages = line.replace("\n", "").split("|")
        self.page = int(pages[0])
        self.page_after = int(pages[1])

class Update:
    def __init__(self, line):
        self.pages = [int(page) for page in line.replace("\n", "").split(",")]

    def is_sorted(self, ordering_rules_per_page: dict) -> bool:
        for page in self.pages:
            pages_after = ordering_rules_per_page.get(page)
            # Verification that there is at least one page ordering rule for this page
            if pages_after != None:
                page_index = self.pages.index(page)
                if not all(page_index < self.pages.index(page_after) for page_after in pages_after if
                           page_after in self.pages):
                    return False
        return True

    def sort(self, ordering_rules_per_page: dict) -> None:
        while not self.is_sorted(ordering_rules_per_page):
            for page in self.pages:
                page_index = self.pages.index(page)
                pages_after = ordering_rules_per_page.get(page)
                if pages_after is not None:
                    pages_after_indexes = [self.pages.index(pa) for pa in pages_after if pa in self.pages]
                    if len(pages_after_indexes) > 0:
                        lowest_pages_after_index = min(pages_after_indexes)
                        if page_index > lowest_pages_after_index:
                            self.pages.insert(lowest_pages_after_index, self.pages.pop(page_index))

def parse_input(filepath: str) -> (list[OrderingRule], list[Update]):
    ordering_rules = []
    updates = []

    with open(filepath) as file:
        ordering_rules_section = True#
        for line in file.readlines():
            if line == "\n":
                ordering_rules_section = False

            if ordering_rules_section:
                ordering_rules.append(OrderingRule(line))
            else:
                if line != "\n":
                    updates.append(Update(line))

    return ordering_rules, updates

def get_ordering_rules_per_page(ordering_rules: list[OrderingRule]) -> dict:
    ordering_rules_per_page = {}
    for ordering_rule in ordering_rules:
        if ordering_rules_per_page.get(ordering_rule.page) is not None:
            ordering_rules_per_page[ordering_rule.page].append(ordering_rule.page_after)
        else:
            ordering_rules_per_page[ordering_rule.page] = [ordering_rule.page_after]

    return ordering_rules_per_page

def get_ordered_and_unordered_updates(updates: list[Update], ordering_rules_per_page: dict) -> (list[Update], list[Update]):
    rightly_ordered_updates = []
    unordered_updates = []
    for update in updates:
        if update.is_sorted(ordering_rules_per_page):
            rightly_ordered_updates.append(update)
        else:
            unordered_updates.append(update)

    return rightly_ordered_updates, unordered_updates

def calculate_sum_of_middle_pages(updates: list[Update]) -> int:
    sum_of_middle_pages = 0
    for update in updates:
        number_of_pages = len(update.pages)
        # Assuming always an uneven number of pages
        middle_page_index = math.floor(number_of_pages / 2)
        sum_of_middle_pages += update.pages[middle_page_index]
    return sum_of_middle_pages

if __name__ == "__main__":
    filepath = "/home/fl/PycharmProjects/AOC2024/day_five/input.txt"
    ordering_rules, updates = parse_input(filepath)

    ordering_rules_per_page = get_ordering_rules_per_page(ordering_rules)
    rightly_ordered_updates, unordered_updates = get_ordered_and_unordered_updates(updates, ordering_rules_per_page)

    print(f"[PART ONE] - The sum of the middle pages is: {calculate_sum_of_middle_pages(rightly_ordered_updates)}")
    for update in unordered_updates:
        update.sort(ordering_rules_per_page)
    print(f"[PART TWO] - The sum of the middle pages is: {calculate_sum_of_middle_pages(unordered_updates)}")