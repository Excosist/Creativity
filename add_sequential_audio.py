import os

def add_sequential_audio_paths(csv_file_path, audio_folder, output_file=None, file_ext='.wav'):
    """
    Add sequential audio file paths to the beginning of each line in a CSV file.
    
    Args:
        csv_file_path (str): Path to the CSV file to modify
        audio_folder (str): Base path for the audio files
        output_file (str, optional): Path to save the output file. If None, a new file will be created with '_with_audio' suffix.
        file_ext (str, optional): File extension for the audio files. Default is '.wav'
    """
    if output_file is None:
        # Create a default output file name if none provided
        base_name = os.path.splitext(csv_file_path)[0]
        output_file = f"{base_name}_with_audio.csv"
    
    print(f"Processing CSV file: {csv_file_path}")
    print(f"Output will be saved to: {output_file}")
    
    # Process the file line by line
    with open(csv_file_path, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        
        line_count = 0
        
        for line in infile:
            line = line.strip()
            
            # Generate sequential audio file path
            audio_path = f"{audio_folder}/audio_{line_count:04d}{file_ext}".replace('\\', '/')
            
            # Add the audio path to the beginning of the line
            modified_line = f"{audio_path},{line}\n"
            outfile.write(modified_line)
            
            line_count += 1
    
    print(f"Processed {line_count} lines.")
    print(f"Added {line_count} sequential audio file paths to the CSV.")

if __name__ == "__main__":
    # Define file paths
    csv_file_path = "D:\\test\\train-00002-of-00026_translated_translated.csv"
    audio_folder = "D:\\audio"  # Path to your audio folder
    
    # Process the file
    add_sequential_audio_paths(csv_file_path, audio_folder)