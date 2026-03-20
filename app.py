from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For session, but we'll use forms

# List of cities in Karnataka
cities = sorted([
    'Bangalore', 'Mysore', 'Mangalore', 'Hubli', 'Belgaum', 'Gulbarga', 'Davangere', 'Bellary',
    'Bijapur', 'Shimoga', 'Tumkur', 'Raichur', 'Bidar', 'Hospet', 'Gadag', 'Udupi',
    'Chikmagalur', 'Kolar', 'Hassan', 'Dharwad', 'Bagalkot', 'Haveri', 'Koppal', 'Yadgir',
    'Chamarajanagar', 'Ramanagara', 'Chikkaballapur', 'Mandya', 'Chitradurga'
])

# List of hotel names
hotels_list = [
    'Grand Palace Hotel', 'City View Inn', 'Royal Comfort Resort', 'Elite Stay Hotel',
    'Sunset Boulevard Hotel', 'Mountain View Lodge', 'River Side Inn', 'Garden Paradise Hotel',
    'Urban Oasis Resort', 'Heritage Hotel', 'Modern Comfort Inn', 'Lake View Hotel',
    'Forest Retreat Lodge', 'Seaside Resort', 'Hilltop Hotel', 'Valley Inn',
    'Desert Rose Hotel', 'Ocean Breeze Resort', 'Skyline Hotel', 'Countryside Lodge'
]

@app.route('/')
def home():
    return render_template('index.html', cities=cities)

@app.route('/select_city', methods=['POST'])
def select_city():
    name = request.form['name']
    phone = request.form['phone']
    city = request.form['city']
    # Select 5 random hotels for the city
    selected_hotels = random.sample(hotels_list, 5)
    return render_template('booking.html', name=name, phone=phone, city=city, hotels=selected_hotels)

@app.route('/payment', methods=['POST'])
def payment():
    name = request.form['name']
    phone = request.form['phone']
    city = request.form['city']
    hotel = request.form['hotel']
    rooms = request.form['rooms']
    room_type = request.form['room_type']
    prices = {'single': 1000, 'double': 1500}
    price_per_room = prices[room_type]
    total = price_per_room * int(rooms)
    return render_template('payment.html', name=name, phone=phone, city=city, hotel=hotel, rooms=rooms, room_type=room_type, price_per_room=price_per_room, total=total)

@app.route('/thankyou', methods=['POST'])
def thankyou():
    name = request.form['name']
    phone = request.form['phone']
    city = request.form['city']
    hotel = request.form['hotel']
    rooms = request.form['rooms']
    room_type = request.form['room_type']
    payment_method = request.form['payment_method']
    prices = {'single': 1000, 'double': 1500}
    price_per_room = prices[room_type]
    total = price_per_room * int(rooms)
    # Mock SMS send
    message = f"Booking confirmed! Name: {name}, City: {city}, Hotel: {hotel}, Room Type: {room_type} Bed, Rooms: {rooms}, Total: ₹{total}, Payment: {payment_method}"
    print(f"SMS sent to {phone}: {message}")
    return render_template('thank_you.html', name=name, phone=phone, city=city, hotel=hotel, rooms=rooms, room_type=room_type, price_per_room=price_per_room, total=total, payment_method=payment_method)

if __name__ == '__main__':
    app.run(debug=True)