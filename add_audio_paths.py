import os
import csv
import shutil

def add_audio_paths_to_csv(csv_file_path, audio_folder, output_file=None):
    """
    Add audio file paths to the beginning of each line in a CSV file.
    
    Args:
        csv_file_path (str): Path to the CSV file to modify
        audio_folder (str): Path to the folder containing audio files
        output_file (str, optional): Path to save the output file. If None, a new file will be created with '_with_audio' suffix.
    """
    if output_file is None:
        # Create a default output file name if none provided
        base_name = os.path.splitext(csv_file_path)[0]
        output_file = f"{base_name}_with_audio.csv"
    
    # Check if the audio folder exists
    if not os.path.exists(audio_folder):
        print(f"Warning: Audio folder '{audio_folder}' does not exist. Using placeholder paths.")
    
    # Get list of audio files if folder exists
    audio_files = []
    if os.path.exists(audio_folder):
        audio_files = sorted([f for f in os.listdir(audio_folder) 
                      if os.path.isfile(os.path.join(audio_folder, f)) and 
                      f.lower().endswith(('.wav', '.mp3', '.ogg', '.flac'))])
        print(f"Found {len(audio_files)} audio files in {audio_folder}")
    
    print(f"Processing CSV file: {csv_file_path}")
    print(f"Output will be saved to: {output_file}")
    
    # Create a backup of the original file
    backup_file = f"{csv_file_path}.bak"
    shutil.copy2(csv_file_path, backup_file)
    print(f"Created backup of original file at: {backup_file}")
    
    # Process the file line by line
    with open(csv_file_path, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        
        line_count = 0
        
        for line in infile:
            line = line.strip()
            
            # Generate audio file path (either real or placeholder)
            if line_count < len(audio_files):
                audio_path = os.path.join(audio_folder, audio_files[line_count]).replace('\\', '/')
            else:
                # Create a placeholder path if there aren't enough audio files
                audio_path = f"{audio_folder}/audio_{line_count:04d}.wav".replace('\\', '/')
            
            # Add the audio path to the beginning of the line
            modified_line = f"{audio_path},{line}\n"
            outfile.write(modified_line)
            
            line_count += 1
    
    print(f"Processed {line_count} lines.")
    print(f"Added {line_count} audio file paths to the CSV.")

if __name__ == "__main__":
    # Define file paths
    csv_file_path = "D:\\test\\train-00002-of-00026_translated_translated.csv"
    audio_folder = "D:\\audio"  # Change this to the actual path when you have it
    
    # Process the file
    add_audio_paths_to_csv(csv_file_path, audio_folder)