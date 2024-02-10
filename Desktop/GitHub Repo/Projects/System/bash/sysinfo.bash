#!/bin/bash

# _doc_
# ----------------------------------
# SysInfo - A System Information Gathering Script for macOS
#
# Date: 23rd Dec 2023
# Author: Jakob Balkovec
# Version: 1.0
# File: sysinfo.bash
# License: MIT
#
# This script gathers and displays key system information on macOS.
# It includes general information, hardware details, system load and performance, network configuration,
# software information, logs and events, battery status, and hypervisor information (if available).
# The gathered information is written to a log file named "system_info_macos.log".
# ----------------------------------
# _/doc_

# Constants
readonly LOG_FILE="system_info_macos.log"
readonly DELIMITER="-------------------"

# Error codes
readonly SUCCESS="100"
readonly FILE_ERROR="200"
readonly GENERAL_ERROR="300"

# _doc_
# ----------------------------------
# General Information
#
# This function fetches general information about the system and writes it to a file named LOG_FILE.
# It includes the hostname, OS version, and kernel version.
# ----------------------------------
# _/doc_
fetch_general_info()
{
  echo "[General Information]" >> "$LOG_FILE"
  echo "$DELIMITER" >> "$LOG_FILE"

  echo "[Hostname]: $(hostname)" >> "$LOG_FILE"
  echo "[OS Version]: $(sw_vers -productVersion)" >> "$LOG_FILE"
  echo "[Kernel Version]: $(uname -a)" >> "$LOG_FILE"
}

# _doc_
# ----------------------------------
# Hardware Information
# 
# This function fetches hardware information and appends it to the LOG_FILE file.
# It retrieves CPU information, memory (RAM) size, disk usage, and GPU information.
# The information is written in a formatted manner with appropriate labels.
# ----------------------------------
#_/doc_
fetch_hardware_info()
{
  echo -e "\n\n[Hardware Information]" >> "$LOG_FILE"
  echo "$DELIMITER" >> "$LOG_FILE"

  echo "[CPU Information]: $(sysctl -n machdep.cpu.brand_string)" >> "$LOG_FILE"
  echo "[Memory (RAM)]: $(sysctl -n hw.memsize | awk '{print $0/1073741824 " GB"}')" >> "$LOG_FILE"
  echo "[Disk Usage]: $(df -h / | awk 'NR==2 {print $3 " | " $5}')" >> "$LOG_FILE"
  echo "[GPU Information]: $(system_profiler SPDisplaysDataType | grep Chip)" >> "$LOG_FILE"
}

# _doc_
# ----------------------------------
# System Load and Performance
#
# This function fetches and logs information about the system load and performance, 
# including CPU usage, memory usage, and network information.
# ----------------------------------
# _/doc_
fetch_load_and_performance()
{
  echo -e "\n\n[Load and Performance]" >> "$LOG_FILE"
  echo "$DELIMITER" >> "$LOG_FILE"

  echo "[CPU Usage]: $(top -l 1 | grep "CPU usage" | awk '{print $3+$5 "%"}')" >> "$LOG_FILE"
  echo "[Memory Usage]: $(top -l 1 | grep PhysMem | awk '{print $2/1024 " MB"}')" >> "$LOG_FILE"
  echo -e "[Network Information]:\n$(netstat -ib | awk '/en0/ {print "Sent - " $7 " | Received - " $10}')" >> "$LOG_FILE"
}

# _doc_
# ----------------------------------
# Network Configuration
#
# This function fetches the network configuration information and appends it to the LOG_FILE file.
# It retrieves the IP addresses, network interfaces, and routing table information.
# ----------------------------------
# _/doc_
fetch_network_config()
{
  echo -e "\n\n[Network Configuration]" >> "$LOG_FILE"
  echo "$DELIMITER" >> "$LOG_FILE"

  echo "[IP Addresses]: $(ipconfig getifaddr en0)" >> "$LOG_FILE"
  echo "[Network Interfaces]: $(networksetup -listallhardwareports | grep -E "(Device|Ethernet)" | awk '{print $2}')" >> "$LOG_FILE"
  echo "[Routing Table]: $(netstat -nr)" >> "$LOG_FILE"
}

# _doc_
# ----------------------------------
# Logs and Events
#
# This function fetches system logs and events and appends them to a file named LOG_FILE.
# ----------------------------------
# _/doc_
fetch_logs_and_events()
{
  echo -e "\n\n[Logs and Events]" >> "$LOG_FILE"
  echo "$DELIMITER" >> "$LOG_FILE"

  echo "[System Logs]: $(cat /var/log/system.log)" >> "$LOG_FILE"
}

# _doc_
# ----------------------------------
# Battery Information
#
# This function fetches and logs Battery data, such as battery charge, cycles, and health.
# such as temperature, fan speed, and power supply status.
# ----------------------------------
# _/doc_
fetch_power_supply_status()
{
  echo -e "\n\n[Power Supply Status]" >> "$LOG_FILE"
  echo "$DELIMITER" >> "$LOG_FILE"
  
  echo -e "[Power Supply Status]:\n$(pmset -g batt)" >> "$LOG_FILE"
}

# _doc_
# ----------------------------------
# Virtualization
#
# This function fetches information about the hypervisor and appends it to the LOG_FILE file.
#
# _debug_
# This function is not working properly, it is not fetching the hypervisor information.
# _/debug_
# ----------------------------------
# _/doc_
fetch_hypevisor_info()
{
  echo -e "\n\n[Hypervisor Information]" >> "$LOG_FILE"
  echo "$DELIMITER" >> "$LOG_FILE"

  hypervisor_info=$(sysctl -a | grep machdep.cpu.features)

  if [ -n "$hypervisor_info" ]; then
    echo "[Hypervisor Information]: $hypervisor_info" >> "$LOG_FILE"
  else
    echo "[Hypervisor Information]: Not available" >> "$LOG_FILE"
  fi
}

# _doc_
# ----------------------------------
# Deletes the previous System Info Log
# ----------------------------------
# _/doc_
delete_system_info_log() {
  file_path="/Users/jbalkovec/Desktop/Projects/System/bash/system_info_macos.log"

  if [ -f "$file_path" ]; then
    rm "$file_path"
    echo -e "[File deleted successfully ERRC := 100]"
  else
    echo -e "[File does not exist ERRC := 300]"
  fi
}

# _doc_
# ----------------------------------
# Main Function, invokes all methods and can be reconfigured to invoke only specific methods.
# ----------------------------------
# _/doc_
main()
{
  # Format
  echo -e "\n\n[SYSTEM INFO REPORT]\n$DELIMITER$DELIMITER"

  # Clear log file
  delete_system_info_log

  # Fetch new system info
  fetch_general_info
  fetch_hardware_info
  fetch_load_and_performance
  fetch_network_config
  fetch_software_info
  fetch_logs_and_events
  fetch_power_supply_status
  fetch_hypevisor_info

  # Check if log file was created
  if [ -f "$LOG_FILE" ]; then
    echo -e "[Log file exported successfully ERRC := 100]"
  else
    echo -e "[Log file was not created ERRC := 200]"
  fi

  echo -e "$DELIMITER$DELIMITER\n[END OF SYSTEM INFO REPORT]\n"
}

main

