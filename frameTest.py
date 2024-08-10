def calculate_f_sleep_time(fps):
    # Calculate the time it takes for one frame to render (in seconds)
    frame_time = 1 / fps

    # Calculate the optimal sleep time for the "F" key press
    # We'll use a slightly longer sleep time to ensure the game registers the input
    f_sleep_time = frame_time * 1.2

    return f_sleep_time


# Example usage:
fps = int(input("Enter your current FPS: "))
f_sleep_time = calculate_f_sleep_time(fps)

print(f"Optimal sleep time for 'F' key press: {f_sleep_time:.4f} seconds")

# Replace the hardcoded sleep time in your original code with this calculated value
# For example:
# time.sleep(f_sleep_time)  # instead of time.sleep(0.02)
