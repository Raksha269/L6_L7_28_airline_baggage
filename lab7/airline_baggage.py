
import math


def parse_booking(code):
    if not isinstance(code, str):
        return None

    parts = [part.strip() for part in code.split("-")]

    if len(parts) != 3:
        return None

    airline, flight, seat = parts

    if not airline or not flight or not seat:
        return None

    try:
        flight_number = int(flight)
    except ValueError:
        return None

    return airline.upper(), flight_number, seat[-1].upper()


def total_weight(weights_csv):
    if not isinstance(weights_csv, str):
        return None

    if not weights_csv.strip():
        return None

    try:
        weights = [
            float(weight.strip())
            for weight in weights_csv.split(",")
        ]
    except ValueError:
        return None

    if not all(math.isfinite(w) and w >= 0 for w in weights):
        return None

    return sum(weights)


def tag_label(name):
    if not isinstance(name, str):
        return None

    parts = name.split()

    if len(parts) < 2:
        return None

    return parts[0][0].upper() + ". " + parts[1].upper()


def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter a booking code (e.g. AI-203-12A): ")
    result = parse_booking(user_input)
    print("Airline, Flight and Seat Letter:", result)

    print("\n==== Running total_weight ====")
    user_input = input("Enter bag weights in kg as CSV (e.g. 12.5,7,23): ")
    result = total_weight(user_input)
    print("Total Weight:", result)

    print("\n==== Running tag_label ====")
    user_input = input("Enter a passenger name (first and last): ")
    result = tag_label(user_input)
    print("Tag Label:", result)


if __name__ == "__main__":
    main()
