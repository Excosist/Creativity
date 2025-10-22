import pyautogui
import time

def emulate_key_sequence(duration=5):
    """
    Emulates a sequence of key presses for the specified duration.
    Sequence: Backspace, Up arrow, Right arrow, Up arrow, Up arrow
    
    Args:
        duration (int): Duration in seconds to run the emulation
    """
    # Make sure to give the user time to switch to their target window
    print("You have 5 seconds to switch to the window where you want to emulate key presses...")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    print("Starting key press emulation! Press Ctrl+C in the terminal to stop.")
    
    start_time = time.time()
    
    try:
        while time.time() - start_time < duration:
            # Press the sequence of keys
            pyautogui.press('backspace')
            pyautogui.press('up')
            pyautogui.press('right')
            pyautogui.press('up')
            pyautogui.press('up')
    except KeyboardInterrupt:
        print("\nKey press emulation stopped by user.")
    
    print(f"\nCompleted key press emulation after {duration} seconds.")

if __name__ == "__main__":
    try:
        # Default to 5 seconds, but allow customization
        duration = 7
        user_input = input(f"Enter duration in seconds (default is {duration}): ")
        if user_input.strip():
            duration = float(user_input)
        
        emulate_key_sequence(duration)
    except Exception as e:
        print(f"An error occurred: {e}")