from abc import ABC, abstractmethod

# ---------- Base Classes ----------
class User(ABC):
    def __init__(self, name, email):
        self._name = name
        self._email = email

    @abstractmethod
    def display_info(self):
        pass


class Customer(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.bookings = []

    def display_info(self):
        print(f"Customer: {self._name}, Email: {self._email}, Bookings: {len(self.bookings)}")


class Manager(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    def display_info(self):
        print(f"Manager: {self._name}, Email: {self._email}")


# ---------- Entities ----------
class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"{self.title} ({self.duration} mins)"


class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self._is_booked = False

    def book(self):
        if not self._is_booked:
            self._is_booked = True
            return True
        return False

    def is_available(self):
        return not self._is_booked

    def __str__(self):
        return f"Seat {self.seat_number} - {'Available' if self.is_available() else 'Booked'}"


class Showtime:
    def __init__(self, movie, time, total_seats=5):
        self.movie = movie
        self.time = time
        self.seats = [Seat(i+1) for i in range(total_seats)]

    def display_seats(self):
        for seat in self.seats:
            print(seat)


class Payment:
    def __init__(self, amount):
        self._amount = amount
        self._status = "Pending"

    def process_payment(self):
        self._status = "Success"
        return True

    def get_status(self):
        return self._status

    @staticmethod
    def calculate_convenience_fee(amount):
        return round(amount * 0.05, 2)  # 5% fee


class Booking:
    def __init__(self, customer, showtime, seat, payment):
        self.customer = customer
        self.showtime = showtime
        self.seat = seat
        self.payment = payment

    def __str__(self):
        return (f"Booking: {self.customer._name}, "
                f"Movie: {self.showtime.movie.title}, "
                f"Seat: {self.seat.seat_number}, "
                f"Status: {self.payment.get_status()}")


# ---------- Cinema Manager ----------
class Cinema:
    total_bookings = 0  # class attribute

    def __init__(self, name):
        self.name = name
        self.movies = []
        self.showtimes = []
        self.bookings = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def add_showtime(self, showtime):
        self.showtimes.append(showtime)

    def book_ticket(self, customer, showtime, seat_number, base_price=200):
        seat = showtime.seats[seat_number-1]
        if seat.book():
            amount = base_price + Payment.calculate_convenience_fee(base_price)
            payment = Payment(amount)
            payment.process_payment()
            booking = Booking(customer, showtime, seat, payment)
            customer.bookings.append(booking)
            self.bookings.append(booking)
            Cinema.total_bookings += 1
            print(" Booking successful!")
            print(booking)
        else:
            print(" Seat already booked!")

    @classmethod
    def occupancy_report(cls):
        print(f"Total Bookings across all cinemas: {cls.total_bookings}")

    def display_reports(self):
        print(f"Cinema: {self.name}")
        for booking in self.bookings:
            print(booking)
