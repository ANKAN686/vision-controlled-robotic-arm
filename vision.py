# ============================================
# MAIN TRACKING LOOP
# ============================================

def run_ball_tracker():
    """Run the ball tracking system with webcam."""
    
    # Create tracker
    tracker = BallTracker3D(
        ball_diameter_cm=BALL_DIAMETER_CM,
        color_lower=BALL_COLOR_LOWER,
        color_upper=BALL_COLOR_UPPER,
        focal_length=FOCAL_LENGTH_PIXELS
    )
    
    # Open webcam
    cap = cv.VideoCapture(CAMERA_INDEX)
    
    
    
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
    
    # Set resolution (optional)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
    
    print("Ball Tracker Started!")
    print("=" * 40)
    print(f"Ball diameter: {BALL_DIAMETER_CM} cm")
    print(f"Max position shift: {MAX_SHIFT} px")
    print(f"Max radius change: {MAX_RADIUS_CHANGE} px")
    print(f"Press 'q' to quit")
    print(f"Press 'c' to enter color calibration mode")
    print(f"Press 'r' to reset tracking")
    print("=" * 40)
    
    # For FPS calculation
    prev_time = time.time()
    fps = 0
    
    # Color calibration mode
    calibration_mode = False
    clicked_point = None
    
    def mouse_callback(event, x, y, flags, param):
        nonlocal clicked_point
        if event == cv.EVENT_LBUTTONDOWN:
            clicked_point = (x, y)
    
    cv.namedWindow('Ball Tracker 3D')
    cv.setMouseCallback('Ball Tracker 3D', mouse_callback)
    
    kernel = np.ones((5, 5), np.uint8)
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read frame")
            break
        
        # Flip horizontally for mirror effect
        frame = cv.flip(frame, 1)
        
        # Calculate FPS
        current_time = time.time()
        fps = 1 / (current_time - prev_time + 0.001)
        prev_time = current_time
        
        # Color calibration mode
        if calibration_mode and clicked_point is not None:
            x, y = clicked_point
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            
            # Get color at clicked point (average 5x5 region)
            region = hsv[max(0,y-2):y+3, max(0,x-2):x+3]
            avg_hsv = np.mean(region, axis=(0, 1)).astype(int)
            
            print(f"\nClicked HSV: {avg_hsv}")
            print(f"Suggested range:")
            print(f"  Lower: [{max(0, avg_hsv[0]-10)}, {max(0, avg_hsv[1]-50)}, {max(0, avg_hsv[2]-50)}]")
            print(f"  Upper: [{min(179, avg_hsv[0]+10)}, 255, 255]")
            
            clicked_point = None
        
        # Process frame
        annotated_frame, position_3d, detection = tracker.process_frame(frame)
        
        # Display FPS
        cv.putText(annotated_frame, f"FPS: {fps:.1f}", (annotated_frame.shape[1] - 100, 30), 
                   cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        # Calibration mode indicator
        if calibration_mode:
            cv.putText(annotated_frame, "CALIBRATION MODE - Click on ball", 
                      (10, annotated_frame.shape[0] - 20), 
                      cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        
        # Calculate and display IK angles in terminal
        if position_3d:
            try:
                ik_result = ik_2dof(position_3d[0], position_3d[1], L1, L2, position_3d[2])
                # Clear line and print (using \r to overwrite previous output)
                print(f"\r{ik_result.strip()}", end="", flush=True)
            except ValueError as e:
                print(f"\rIK Error: {str(e)}", end="", flush=True)
        else:
            print(f"\rNo valid 3D position", end="", flush=True)
        
        # Show frameq
        cv.imshow('Ball Tracker 3D', annotated_frame)
        
        # Handle key presses
        key = cv.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            calibration_mode = not calibration_mode
            print(f"Calibration mode: {'ON' if calibration_mode else 'OFF'}")
        elif key == ord('r'):
            tracker.reset_tracking()
            print("Tracking reset - accepting new detections")
            
    
    cap.release()
    cv.destroyAllWindows()
    print("\nTracker stopped.")

# Run the tracker
run_ball_tracker()
# Return string base_angle, shoulder_angle, wrist_angle\n