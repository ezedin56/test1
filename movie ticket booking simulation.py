def movie_booking_system():
    # Available movies with showtimes and prices
    movies = {
        1: {
            "title": "Avengers: Endgame",
            "showtimes": ["10:00 AM", "2:30 PM", "7:00 PM", "9:45 PM"],
            "price": 12.50,
            "genre": "Action"
        },
        2: {
            "title": "The Lion King",
            "showtimes": ["11:00 AM", "3:15 PM", "6:30 PM"],
            "price": 10.00,
            "genre": "Animation"
        },
        3: {
            "title": "Inception",
            "showtimes": ["1:00 PM", "4:45 PM", "8:30 PM"],
            "price": 11.00,
            "genre": "Sci-Fi"
        },
        4: {
            "title": "La La Land",
            "showtimes": ["12:30 PM", "5:00 PM", "7:45 PM"],
            "price": 9.50,
            "genre": "Musical"
        },
        5: {
            "title": "The Dark Knight",
            "showtimes": ["10:30 AM", "3:00 PM", "6:15 PM", "9:30 PM"],
            "price": 11.50,
            "genre": "Action"
        }
    }
    
    # Booking history
    bookings = []
    total_cost = 0
    
    print("=" * 60)
    print("         🎬 WELCOME TO MOVIE TICKET BOOKING SYSTEM")
    print("=" * 60)
    
    def display_movies():
        print("\n🎭 NOW SHOWING:")
        print("-" * 70)
        print(f"{'ID':<3} {'Movie Title':<25} {'Genre':<10} {'Price':<8} {'Showtimes'}")
        print("-" * 70)
        
        for movie_id, movie_info in movies.items():
            showtimes_str = ", ".join(movie_info["showtimes"])
            print(f"{movie_id:<3} {movie_info['title']:<25} {movie_info['genre']:<10} ${movie_info['price']:<7.2f} {showtimes_str}")
    
    def book_tickets():
        nonlocal total_cost
        
        display_movies()
        
        # Movie selection
        try:
            movie_choice = int(input("\n🎟️  Enter Movie ID to book tickets: "))
            
            if movie_choice not in movies:
                print("❌ Invalid Movie ID! Please try again.")
                return False
            
            selected_movie = movies[movie_choice]
            
            # Showtime selection
            print(f"\n🕐 Available showtimes for '{selected_movie['title']}':")
            for i, showtime in enumerate(selected_movie["showtimes"], 1):
                print(f"   {i}. {showtime}")
            
            try:
                showtime_choice = int(input(f"\nSelect showtime (1-{len(selected_movie['showtimes'])}): "))
                
                if showtime_choice < 1 or showtime_choice > len(selected_movie["showtimes"]):
                    print("❌ Invalid showtime selection!")
                    return False
                
                selected_showtime = selected_movie["showtimes"][showtime_choice - 1]
                
                # Number of tickets
                try:
                    num_tickets = int(input(f"\nEnter number of tickets: "))
                    
                    if num_tickets <= 0:
                        print("❌ Number of tickets must be at least 1!")
                        return False
                    if num_tickets > 10:
                        print("⚠️  Maximum 10 tickets per booking!")
                        return False
                    
                    # Calculate cost
                    subtotal = selected_movie["price"] * num_tickets
                    
                    # Display booking summary
                    print("\n" + "=" * 50)
                    print("           BOOKING SUMMARY")
                    print("=" * 50)
                    print(f"🎬 Movie: {selected_movie['title']}")
                    print(f"🕐 Showtime: {selected_showtime}")
                    print(f"🎟️  Tickets: {num_tickets}")
                    print(f"💰 Price per ticket: ${selected_movie['price']:.2f}")
                    print(f"💵 Subtotal: ${subtotal:.2f}")
                    print("=" * 50)
                    
                    # Confirmation
                    confirm = input("\nConfirm booking? (yes/no): ").strip().lower()
                    
                    if confirm in ['yes', 'y']:
                        # Save booking
                        booking = {
                            "movie": selected_movie["title"],
                            "showtime": selected_showtime,
                            "tickets": num_tickets,
                            "price_per_ticket": selected_movie["price"],
                            "subtotal": subtotal
                        }
                        
                        bookings.append(booking)
                        total_cost += subtotal
                        
                        print(f"\n✅ Booking confirmed! {num_tickets} ticket(s) for '{selected_movie['title']}'")
                        print(f"   Showtime: {selected_showtime}")
                        print(f"   Total for this booking: ${subtotal:.2f}")
                        return True
                    else:
                        print("❌ Booking cancelled.")
                        return False
                        
                except ValueError:
                    print("❌ Please enter a valid number for tickets!")
                    return False
                    
            except ValueError:
                print("❌ Please enter a valid showtime number!")
                return False
                
        except ValueError:
            print("❌ Please enter a valid Movie ID!")
            return False
    
    # Main booking loop
    
    
    # Final summary
    print("\n" + "=" * 60)
    print("           FINAL BOOKING SUMMARY")
    print("=" * 60)
    
    if not bookings:
        print("No bookings were made. Thank you for visiting!")
    else:
        total_tickets = sum(booking['tickets'] for booking in bookings)
        
        print(f"📊 Total Movies Booked: {len(bookings)}")
        print(f"🎟️  Total Tickets: {total_tickets}")
        print(f"💰 Total Cost: ${total_cost:.2f}")
        
        print("\n🎬 Your Movie Bookings:")
        for i, booking in enumerate(bookings, 1):
            print(f"  {i}. {booking['movie']} - {booking['showtime']} ({booking['tickets']} tickets)")
        
        print(f"\n🎉 Thank you for your purchase! Enjoy your movies! 🍿")

# Run the movie booking system
if __name__ == "__main__":
    movie_booking_system()