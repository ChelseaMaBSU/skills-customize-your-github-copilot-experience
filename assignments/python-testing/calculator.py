def add(first_number, second_number):
    return first_number + second_number


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def apply_discount(price, discount_percent):
    # TODO: Apply the discount as a percentage of the price.
    return price - discount_percent


def split_bill(total, people):
    # TODO: Raise ValueError when people is zero or negative.
    return round(total / people, 2)