# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/tools/navigator/dbmap/proto/dbmap.proto

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
  name='modules/tools/navigator/dbmap/proto/dbmap.proto',
  package='apollo.dbmap',
  syntax='proto2',
  serialized_pb=_b('\n/modules/tools/navigator/dbmap/proto/dbmap.proto\x12\x0c\x61pollo.dbmap\"F\n\x07\x44\x42Point\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\t\n\x01s\x18\x04 \x01(\x01\x12\x0f\n\x07heading\x18\x05 \x01(\x01\".\n\x06\x44\x42Line\x12$\n\x05point\x18\x01 \x03(\x0b\x32\x15.apollo.dbmap.DBPoint\"o\n\x12\x44\x42NeighbourSegment\x12\x0f\n\x07start_s\x18\x01 \x01(\x01\x12\r\n\x05\x65nd_s\x18\x02 \x01(\x01\x12\x0f\n\x07path_id\x18\x03 \x01(\t\x12\x14\n\x0cpath_start_s\x18\x04 \x01(\x01\x12\x12\n\npath_end_s\x18\x05 \x01(\x01\"D\n\x0f\x44\x42NeighbourPath\x12\x31\n\x07segment\x18\x01 \x03(\x0b\x32 .apollo.dbmap.DBNeighbourSegment\"\xad\x02\n\x06\x44\x42Path\x12\n\n\x02id\x18\x01 \x01(\t\x12\"\n\x04path\x18\x02 \x03(\x0b\x32\x14.apollo.dbmap.DBLine\x12*\n\x0cleft_bounday\x18\x03 \x03(\x0b\x32\x14.apollo.dbmap.DBLine\x12+\n\rright_bounday\x18\x04 \x03(\x0b\x32\x14.apollo.dbmap.DBLine\x12\x30\n\tleft_path\x18\x05 \x03(\x0b\x32\x1d.apollo.dbmap.DBNeighbourPath\x12\x31\n\nright_path\x18\x06 \x03(\x0b\x32\x1d.apollo.dbmap.DBNeighbourPath\x12\x35\n\x0e\x64uplicate_path\x18\x07 \x03(\x0b\x32\x1d.apollo.dbmap.DBNeighbourPath\",\n\x05\x44\x42Map\x12#\n\x05paths\x18\x01 \x03(\x0b\x32\x14.apollo.dbmap.DBPath')
)




_DBPOINT = _descriptor.Descriptor(
  name='DBPoint',
  full_name='apollo.dbmap.DBPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='apollo.dbmap.DBPoint.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='apollo.dbmap.DBPoint.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='apollo.dbmap.DBPoint.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='s', full_name='apollo.dbmap.DBPoint.s', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heading', full_name='apollo.dbmap.DBPoint.heading', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=65,
  serialized_end=135,
)


_DBLINE = _descriptor.Descriptor(
  name='DBLine',
  full_name='apollo.dbmap.DBLine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='apollo.dbmap.DBLine.point', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=137,
  serialized_end=183,
)


_DBNEIGHBOURSEGMENT = _descriptor.Descriptor(
  name='DBNeighbourSegment',
  full_name='apollo.dbmap.DBNeighbourSegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_s', full_name='apollo.dbmap.DBNeighbourSegment.start_s', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_s', full_name='apollo.dbmap.DBNeighbourSegment.end_s', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path_id', full_name='apollo.dbmap.DBNeighbourSegment.path_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path_start_s', full_name='apollo.dbmap.DBNeighbourSegment.path_start_s', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path_end_s', full_name='apollo.dbmap.DBNeighbourSegment.path_end_s', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=185,
  serialized_end=296,
)


_DBNEIGHBOURPATH = _descriptor.Descriptor(
  name='DBNeighbourPath',
  full_name='apollo.dbmap.DBNeighbourPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='segment', full_name='apollo.dbmap.DBNeighbourPath.segment', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=298,
  serialized_end=366,
)


_DBPATH = _descriptor.Descriptor(
  name='DBPath',
  full_name='apollo.dbmap.DBPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.dbmap.DBPath.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='apollo.dbmap.DBPath.path', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='left_bounday', full_name='apollo.dbmap.DBPath.left_bounday', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right_bounday', full_name='apollo.dbmap.DBPath.right_bounday', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='left_path', full_name='apollo.dbmap.DBPath.left_path', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right_path', full_name='apollo.dbmap.DBPath.right_path', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duplicate_path', full_name='apollo.dbmap.DBPath.duplicate_path', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=369,
  serialized_end=670,
)


_DBMAP = _descriptor.Descriptor(
  name='DBMap',
  full_name='apollo.dbmap.DBMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='paths', full_name='apollo.dbmap.DBMap.paths', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=672,
  serialized_end=716,
)

_DBLINE.fields_by_name['point'].message_type = _DBPOINT
_DBNEIGHBOURPATH.fields_by_name['segment'].message_type = _DBNEIGHBOURSEGMENT
_DBPATH.fields_by_name['path'].message_type = _DBLINE
_DBPATH.fields_by_name['left_bounday'].message_type = _DBLINE
_DBPATH.fields_by_name['right_bounday'].message_type = _DBLINE
_DBPATH.fields_by_name['left_path'].message_type = _DBNEIGHBOURPATH
_DBPATH.fields_by_name['right_path'].message_type = _DBNEIGHBOURPATH
_DBPATH.fields_by_name['duplicate_path'].message_type = _DBNEIGHBOURPATH
_DBMAP.fields_by_name['paths'].message_type = _DBPATH
DESCRIPTOR.message_types_by_name['DBPoint'] = _DBPOINT
DESCRIPTOR.message_types_by_name['DBLine'] = _DBLINE
DESCRIPTOR.message_types_by_name['DBNeighbourSegment'] = _DBNEIGHBOURSEGMENT
DESCRIPTOR.message_types_by_name['DBNeighbourPath'] = _DBNEIGHBOURPATH
DESCRIPTOR.message_types_by_name['DBPath'] = _DBPATH
DESCRIPTOR.message_types_by_name['DBMap'] = _DBMAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DBPoint = _reflection.GeneratedProtocolMessageType('DBPoint', (_message.Message,), dict(
  DESCRIPTOR = _DBPOINT,
  __module__ = 'modules.tools.navigator.dbmap.proto.dbmap_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dbmap.DBPoint)
  ))
_sym_db.RegisterMessage(DBPoint)

DBLine = _reflection.GeneratedProtocolMessageType('DBLine', (_message.Message,), dict(
  DESCRIPTOR = _DBLINE,
  __module__ = 'modules.tools.navigator.dbmap.proto.dbmap_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dbmap.DBLine)
  ))
_sym_db.RegisterMessage(DBLine)

DBNeighbourSegment = _reflection.GeneratedProtocolMessageType('DBNeighbourSegment', (_message.Message,), dict(
  DESCRIPTOR = _DBNEIGHBOURSEGMENT,
  __module__ = 'modules.tools.navigator.dbmap.proto.dbmap_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dbmap.DBNeighbourSegment)
  ))
_sym_db.RegisterMessage(DBNeighbourSegment)

DBNeighbourPath = _reflection.GeneratedProtocolMessageType('DBNeighbourPath', (_message.Message,), dict(
  DESCRIPTOR = _DBNEIGHBOURPATH,
  __module__ = 'modules.tools.navigator.dbmap.proto.dbmap_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dbmap.DBNeighbourPath)
  ))
_sym_db.RegisterMessage(DBNeighbourPath)

DBPath = _reflection.GeneratedProtocolMessageType('DBPath', (_message.Message,), dict(
  DESCRIPTOR = _DBPATH,
  __module__ = 'modules.tools.navigator.dbmap.proto.dbmap_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dbmap.DBPath)
  ))
_sym_db.RegisterMessage(DBPath)

DBMap = _reflection.GeneratedProtocolMessageType('DBMap', (_message.Message,), dict(
  DESCRIPTOR = _DBMAP,
  __module__ = 'modules.tools.navigator.dbmap.proto.dbmap_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dbmap.DBMap)
  ))
_sym_db.RegisterMessage(DBMap)


# @@protoc_insertion_point(module_scope)
