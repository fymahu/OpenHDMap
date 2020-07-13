# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/proto/spiral_curve_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/planning/proto/spiral_curve_config.proto',
  package='apollo.planning',
  syntax='proto2',
  serialized_pb=_b('\n0modules/planning/proto/spiral_curve_config.proto\x12\x0f\x61pollo.planning\"s\n\x11SpiralCurveConfig\x12\x17\n\x0csimpson_size\x18\x01 \x01(\x05:\x01\x39\x12 \n\x12newton_raphson_tol\x18\x02 \x01(\x01:\x04\x30.01\x12#\n\x17newton_raphson_max_iter\x18\x03 \x01(\x05:\x02\x32\x30')
)




_SPIRALCURVECONFIG = _descriptor.Descriptor(
  name='SpiralCurveConfig',
  full_name='apollo.planning.SpiralCurveConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='simpson_size', full_name='apollo.planning.SpiralCurveConfig.simpson_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=9,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='newton_raphson_tol', full_name='apollo.planning.SpiralCurveConfig.newton_raphson_tol', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0.01),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='newton_raphson_max_iter', full_name='apollo.planning.SpiralCurveConfig.newton_raphson_max_iter', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=20,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=184,
)

DESCRIPTOR.message_types_by_name['SpiralCurveConfig'] = _SPIRALCURVECONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpiralCurveConfig = _reflection.GeneratedProtocolMessageType('SpiralCurveConfig', (_message.Message,), dict(
  DESCRIPTOR = _SPIRALCURVECONFIG,
  __module__ = 'modules.planning.proto.spiral_curve_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.SpiralCurveConfig)
  ))
_sym_db.RegisterMessage(SpiralCurveConfig)


# @@protoc_insertion_point(module_scope)
