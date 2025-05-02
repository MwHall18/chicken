Testing Protocol for Chicken Predator Deterrent System

Objective: 
To verify the functionality of the deterrent system that uses LiDAR, sound, water, and light components to protect chickens from predators. The system must activate each deterrent at the specified range and respond accurately to approaching objects.

Materials:
Measuring tape or measuring device
Person or object to approach the system
Power source with an extension cord
Water source for the water pump
Digital document for recording test results
Camera or Stopwatch 

Pre-Test Setup:
Ensure all components are correctly connected
LiDAR system to Raspberry Pi
Light, sound, and water components to Raspberry Pi
Position the system
Set up the system in the test area
Ensure LiDAR has an unobstructed line of sight for the stated distances.
Prepare components
Fill the water drum for the water pump
Test speaker and lights for proper functionality

Individual Component Testing
LiDAR Detection Testing
Objective: Ensure LiDAR detects objects at a specified distance (500cm)
Test Steps:
Stand at varying distances (e.g., 490cm, 500cm, 510cm) from the LiDAR sensor
Record if and when the system detects movement within 500cm
Ensure no false positives or negatives are recorded
Success Criteria
LiDAR should detect all movement within 500cm and not outside this range.
Light Activation Testing
Objective: Ensure lights activate within 400cm from the device.
Test Steps
Move towards the system at 390cm, 400cm, and 410cm.
Confirm light activation within 400cm
Check timely response upon detection
Success Criteria:
Lights activate between 301cm and 400cm and do not activate outside of this range
Sound Activation Testing
Objective: Ensure sound activates within 300cm
Test Steps
Approach the system at distances of 290cm, 300cm, and 310cm
Ensure Sound activates when within 300cm
Success Criteria
Sound activates between 201cm and 300cm and remains off outside of this range.
Water Activation Testing
Objective: Ensure the water pump activates within 200cm
Test Steps
Approach the system at distances of 190cm, 200cm, and 210cm.
Confirm the water pump activates at 200cm
Success Criteria
Water dispersion should activate at 200cm and within and stop outside this range.
Full System Testing
 Test with all components activated 
Test Steps
Start at a distance of 500cm and move toward the system
Monitor whether each deterrent activates at the correct distance as you approach
LiDar detects at 500cm
Light activates at 400cm
Sound Activaes at 300cm
Water Activates at 200cm
Record if all systems activate and deactivate correctly without delay
Success Criteria
All components activate at their specified range and do so without delay
Troubleshooting and Adjustments
If any component fails to activate at the correct distance, perform the following:
LiDAR: Adjust its positioning and sensitivity settings
Lights: Check wiring and adjust brightness if it is too dim
Sound: Check speaker volume and connection
Water: Adjust water pressure and check the pump functionality
Re-test after adjustments to ensure proper functionality
Post-Test Documentation:
Record the success or failure of each test
Note any issues or adjustments made
Take photos or videos of test setups for reference
Keep track of results in a digital or physical log sheet for future reference
Success Criteria for Full System: 
LiDAR detects movement accurately at 500cm
Lights activate between 301cm and 400cm
Sound activates between 201cm and 300cm
Water activates within 200cm
There are no significant delays between the detection and activation of components.
Post-Test Analysis and Improvements
False positives/negatives: Adjust LiDAR sensitivity or sensor positioning
Activation Delays:  Ensure Raspberry Pi is processing inputs quickly enough; make coding adjustments if needed
Component Adjustments: Fine-tune water pressure, light brightness speaker volume, and connectivity if necessary
