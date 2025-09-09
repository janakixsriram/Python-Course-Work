from movie import Cinema, Movie, Showtime, Manager, Customer

def main():
    print("🎬 Welcome to Movie Ticket Booking System 🎟️")

    cinema = Cinema("PVR Multiplex")
    manager = Manager("Alice", "alice@cinema.com")

    # Manager adds movies and showtimes
    movie1 = Movie("Inception", 148)
    movie2 = Movie("Interstellar", 169)
    cinema.add_movie(movie1)
    cinema.add_movie(movie2)

    show1 = Showtime(movie1, "6:00 PM")
    show2 = Showtime(movie2, "9:00 PM")
    cinema.add_showtime(show1)
    cinema.add_showtime(show2)

    # Register customer
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    customer = Customer(name, email)

    while True:
        print("\n===== MENU =====")
        print("1. View Movies")
        print("2. View Showtimes")
        print("3. View Seats")
        print("4. Book Ticket")
        print("5. View My Bookings")
        print("6. Cinema Report")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\n🎬 Movies Available:")
            for idx, movie in enumerate(cinema.movies, 1):
                print(f"{idx}. {movie}")

        elif choice == "2":
            print("\n⏰ Showtimes:")
            for idx, show in enumerate(cinema.showtimes, 1):
                print(f"{idx}. {show.movie.title} at {show.time}")

        elif choice == "3":
            print("\nChoose showtime to see seats:")
            for idx, show in enumerate(cinema.showtimes, 1):
                print(f"{idx}. {show.movie.title} at {show.time}")
            s_choice = int(input("Enter choice: "))
            if 1 <= s_choice <= len(cinema.showtimes):
                cinema.showtimes[s_choice-1].display_seats()

        elif choice == "4":
            print("\nChoose showtime to book:")
            for idx, show in enumerate(cinema.showtimes, 1):
                print(f"{idx}. {show.movie.title} at {show.time}")
            s_choice = int(input("Enter choice: "))
            if 1 <= s_choice <= len(cinema.showtimes):
                show = cinema.showtimes[s_choice-1]
                show.display_seats()
                seat_no = int(input("Enter seat number: "))
                cinema.book_ticket(customer, show, seat_no)

        elif choice == "5":
            print("\n🧾 My Bookings:")
            if not customer.bookings:
                print("No bookings yet.")
            else:
                for b in customer.bookings:
                    print(b)

        elif choice == "6":
            print("\n📊 Cinema Report:")
            cinema.display_reports()
            Cinema.occupancy_report()

        elif choice == "0":
            print("👋 Thank you for using Movie Ticket Booking System!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
