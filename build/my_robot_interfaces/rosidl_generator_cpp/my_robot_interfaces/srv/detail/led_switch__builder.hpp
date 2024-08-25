// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interfaces:srv/LedSwitch.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__LED_SWITCH__BUILDER_HPP_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__LED_SWITCH__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_robot_interfaces/srv/detail/led_switch__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_LedSwitch_Request_switched_on
{
public:
  explicit Init_LedSwitch_Request_switched_on(::my_robot_interfaces::srv::LedSwitch_Request & msg)
  : msg_(msg)
  {}
  ::my_robot_interfaces::srv::LedSwitch_Request switched_on(::my_robot_interfaces::srv::LedSwitch_Request::_switched_on_type arg)
  {
    msg_.switched_on = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::srv::LedSwitch_Request msg_;
};

class Init_LedSwitch_Request_led_number
{
public:
  Init_LedSwitch_Request_led_number()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LedSwitch_Request_switched_on led_number(::my_robot_interfaces::srv::LedSwitch_Request::_led_number_type arg)
  {
    msg_.led_number = std::move(arg);
    return Init_LedSwitch_Request_switched_on(msg_);
  }

private:
  ::my_robot_interfaces::srv::LedSwitch_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::srv::LedSwitch_Request>()
{
  return my_robot_interfaces::srv::builder::Init_LedSwitch_Request_led_number();
}

}  // namespace my_robot_interfaces


namespace my_robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_LedSwitch_Response_success
{
public:
  Init_LedSwitch_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_robot_interfaces::srv::LedSwitch_Response success(::my_robot_interfaces::srv::LedSwitch_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::srv::LedSwitch_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::srv::LedSwitch_Response>()
{
  return my_robot_interfaces::srv::builder::Init_LedSwitch_Response_success();
}

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__LED_SWITCH__BUILDER_HPP_
