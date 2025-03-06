# open_topic_6523_ws
This is open topic about autonomous vehicle use autoware with carla simulation
# How to run 
1. Run carla
```bash
cd carla
make launch
```

2. Spawn car by run autoware ros bridge
```bash
ros2 launch carla_autoware_bridge carla_autoware_demo.launch.py timeout:=120 view:=true town:=Town10HD
```

3. Run LIO-SAM
```bash
ros2 launch carla_mapping lio_sam.launch.py
```

4. Save map from LIO-SAM
```bash
ros2 service call /lio_sam/save_map lio_sam/srv/SaveMap "{resolution: 0.2, destination: /Town10_map}"
```

5. Run autoware
```bash
ros2 launch autoware_launch e2e_simulator.launch.xml map_path:=$HOME/autoware_map/Town10 vehicle_model:=sample_vehicle sensor_model:=awsim_sensor_kit simulator_type:=carla carla_map:=Town10HD

ros2 launch autoware_launch e2e_simulator.launch.xml map_path:=$HOME/autoware_map/Town10 vehicle_model:=carla_tesla_model3 sensor_model:=sample_sensor_kit

ros2 launch autoware_launch planning_simulator.launch.xml map_path:=$HOME/autoware_map/Town10 vehicle_model:=carla_tesla_model3 sensor_model:=sample_sensor_kit
```