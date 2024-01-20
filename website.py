class Website:
    """Contains information about website structure"""

    def __init__(self, name, url, search_url, results_selector, name_selector, check_game_selector, check_game_function, price_selector, dynamically_generated, consoles):
        self.name = name
        self.url = url
        self.search_url = search_url
        self.results_selector = results_selector
        self.name_selector = name_selector
        self.check_game_selector = check_game_selector
        self.check_game_function = check_game_function
        self.price_selector = price_selector
        self.dynamically_generated = dynamically_generated
        self.consoles = consoles
