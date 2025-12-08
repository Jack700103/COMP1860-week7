import sys
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_7segment(a, b, c, d, e, f, g, code="2014563"):
    if code != "2014563":
        print("Error: Incorrect group code. Please enter the correct code from your activity sheet.")
        return

    top = " " + ("-" * 5) if a else " " * 6

    upper_right = "|" if b else " "
    upper_left = "|" if f else " "

    middle = " " + ("-" * 5) if g else " " * 6

    lower_right = "|" if c else " "
    lower_left = "|" if e else " "

    bottom = " " + ("-" * 5) if d else " " * 6

    display = [
        " " + top + " ",
        upper_left + " " * 5 + upper_right,
        upper_left + " " * 5 + upper_right,
        " " + middle + " ",
        lower_left + " " * 5 + lower_right,
        lower_left + " " * 5 + lower_right,
        " " + bottom + " "
    ]

    clear_screen()
    print("\n7-Segment Display:")
    print("=" * 10)
    for line in display:
        print(line)
    print("=" * 10)
    print("Segments: a={} b={} c={} d={} e={} f={} g={}".format(a, b, c, d, e, f, g))
    print("\n")

def parse_simulator_output(filename):
    results = []
    
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

        for line in lines[1:]:
            parts = [p for p in line.strip().split(' ') if p]

            if len(parts) >= 11:
                in3 = int(parts[1])
                in2 = int(parts[3])
                in1 = int(parts[5])
                in0 = int(parts[7])
                a = int(parts[9])
                b = int(parts[11])
                c = int(parts[13])
                d = int(parts[15])
                e = int(parts[17])
                f = int(parts[19])
                g = int(parts[21])
                
                results.append((in3, in2, in1, in0, a, b, c, d, e, f, g))
    
    except Exception as e:
        print(f"Error parsing file: {e}")
        return []
    
    return results

def main():
    print("7-Segment Display Visualizer")
    print("===========================")

    group_code = input("Enter your group code (from activity sheet): ").strip()

    filename = input("Enter path to simulator output file (.out): ").strip()
    
    try:
        results = parse_simulator_output(filename)
        
        if not results:
            print("No valid data found in the output file.")
            return
        
        print(f"\nFound {len(results)} test cases. Displaying...")
        
        for i, (in3, in2, in1, in0, a, b, c, d, e, f, g) in enumerate(results):
            hex_value = in3 * 8 + in2 * 4 + in1 * 2 + in0
            hex_digit = hex(hex_value)[2:].upper()
            
            print(f"\nTest Case #{i+1}: Input = {in3}{in2}{in1}{in0} ({hex_digit})")
            display_7segment(a, b, c, d, e, f, g, group_code)
            time.sleep(2) 
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
