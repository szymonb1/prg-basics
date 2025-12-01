# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   seats_amount = 0
   for row in seats:
      for seat in row:
         seats_amount += 1
   return seats_amount

def seats_available(seats):
   available_seats_amount = 0
   for row in seats:
      for seat in row:
         if seat == "A":
            available_seats_amount += 1
         else:
            pass
   return available_seats_amount

def seats_booked(seats):
   booked_seats_amount = 0
   for row in seats:
      for seat in row:
         if seat == "B":
            booked_seats_amount += 1
         else:
            pass
   return booked_seats_amount

def seat_status(seats, row, place):
   if seats[row - 1][place - 1] == "A":
      return "Available"
   else:
      return "booked"

print('CINEMA INFORMATION TABLE')
print(f'Total seats: {seats_total(cinema_seats)}')
print(f'Seats available: {seats_available(cinema_seats)}')
print(f'Seats booked: {seats_booked(cinema_seats)}')         
print(f'Seat in row 1, place 1: {seat_status(cinema_seats, 1, 1)}')
print(f'Seat in row 5, place 5:', {seat_status(cinema_seats, 5, 5)})
print(f'Seat in row 3, place 5:', {seat_status(cinema_seats, 3, 5)})