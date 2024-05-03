import os
import cv2
import face_recognition
# Path to the folder containing videos
videos_folder = 'C:/Users/joshi/OneDrive/Desktop/New/Fake'
output_folder = 'C:/Users/joshi/OneDrive/Desktop/New/Images/Fake'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to extract faces from a video
def extract_faces(video_path, output_folder, max_frames=12):
    # Open video file
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    face_count = 0
    
    while cap.isOpened() and face_count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to RGB (face_recognition uses RGB)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find faces in the frame
        face_locations = face_recognition.face_locations(rgb_frame)

        # Iterate through detected faces
        for top, right, bottom, left in face_locations:
            # Crop face
            face_img = frame[top:bottom, left:right]
            # Save face with video and frame number
            face_filename = f'{os.path.basename(video_path)}_frame_{frame_count}_face_{face_count}.jpg'
            face_output_path = os.path.join(output_folder, face_filename)
            cv2.imwrite(face_output_path, face_img)
            face_count += 1

        frame_count += 1

    cap.release()

# Iterate through all video files in the folder
for filename in os.listdir(videos_folder):
    if filename.endswith('.mp4') or filename.endswith('.avi'):
        video_path = os.path.join(videos_folder, filename)
        # Extract faces from each video
        extract_faces(video_path, output_folder, max_frames=12)
