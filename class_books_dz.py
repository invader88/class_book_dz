class Book:
    def __init__(self, year, name, author):
        self.year = year
        self.name = name
        self.author = author
        self.reviews = [] 
    def __eq__(book1, book2):
        if book1.year == book2.year and book1.name == book2.name and book1.author == book2.author:
            return True
        else:
            return False
    def add_review(self, your_review):
        self.reviews.append(your_review)
        print("Thanks for your review")
    def show_reviews(self):
        for i in self.reviews:
            print('{}. {}'.format(self.reviews.index(i)+1,i))
            

