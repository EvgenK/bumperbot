# generated from rosidl_generator_py/resource/_idl.py.em
# with input from my_robot_interfaces:msg/LedState.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_LedState(type):
    """Metaclass of message 'LedState'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('my_robot_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'my_robot_interfaces.msg.LedState')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__led_state
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__led_state
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__led_state
            cls._TYPE_SUPPORT = module.type_support_msg__msg__led_state
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__led_state

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class LedState(metaclass=Metaclass_LedState):
    """Message class 'LedState'."""

    __slots__ = [
        '_led_one_is_active',
        '_led_two_is_active',
        '_led_three_is_active',
    ]

    _fields_and_field_types = {
        'led_one_is_active': 'boolean',
        'led_two_is_active': 'boolean',
        'led_three_is_active': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.led_one_is_active = kwargs.get('led_one_is_active', bool())
        self.led_two_is_active = kwargs.get('led_two_is_active', bool())
        self.led_three_is_active = kwargs.get('led_three_is_active', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.led_one_is_active != other.led_one_is_active:
            return False
        if self.led_two_is_active != other.led_two_is_active:
            return False
        if self.led_three_is_active != other.led_three_is_active:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def led_one_is_active(self):
        """Message field 'led_one_is_active'."""
        return self._led_one_is_active

    @led_one_is_active.setter
    def led_one_is_active(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'led_one_is_active' field must be of type 'bool'"
        self._led_one_is_active = value

    @builtins.property
    def led_two_is_active(self):
        """Message field 'led_two_is_active'."""
        return self._led_two_is_active

    @led_two_is_active.setter
    def led_two_is_active(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'led_two_is_active' field must be of type 'bool'"
        self._led_two_is_active = value

    @builtins.property
    def led_three_is_active(self):
        """Message field 'led_three_is_active'."""
        return self._led_three_is_active

    @led_three_is_active.setter
    def led_three_is_active(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'led_three_is_active' field must be of type 'bool'"
        self._led_three_is_active = value
