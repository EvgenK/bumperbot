// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_robot_interfaces:srv/LedSwitch.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__LED_SWITCH__STRUCT_H_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__LED_SWITCH__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/LedSwitch in the package my_robot_interfaces.
typedef struct my_robot_interfaces__srv__LedSwitch_Request
{
  int64_t led_number;
  bool switched_on;
} my_robot_interfaces__srv__LedSwitch_Request;

// Struct for a sequence of my_robot_interfaces__srv__LedSwitch_Request.
typedef struct my_robot_interfaces__srv__LedSwitch_Request__Sequence
{
  my_robot_interfaces__srv__LedSwitch_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__srv__LedSwitch_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/LedSwitch in the package my_robot_interfaces.
typedef struct my_robot_interfaces__srv__LedSwitch_Response
{
  bool success;
} my_robot_interfaces__srv__LedSwitch_Response;

// Struct for a sequence of my_robot_interfaces__srv__LedSwitch_Response.
typedef struct my_robot_interfaces__srv__LedSwitch_Response__Sequence
{
  my_robot_interfaces__srv__LedSwitch_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__srv__LedSwitch_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__LED_SWITCH__STRUCT_H_
