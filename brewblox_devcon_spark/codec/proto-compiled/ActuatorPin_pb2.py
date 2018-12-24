# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ActuatorPin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2
import ActuatorDigital_pb2 as ActuatorDigital__pb2
import DigitalConstraints_pb2 as DigitalConstraints__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ActuatorPin.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x41\x63tuatorPin.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\x1a\x15\x41\x63tuatorDigital.proto\x1a\x18\x44igitalConstraints.proto\"\xa8\x01\n\x0b\x41\x63tuatorPin\x12%\n\x05state\x18\x01 \x01(\x0e\x32\x0e.blox.AD.StateB\x06\x8a\xb5\x18\x02\x30\x01\x12\x0e\n\x06invert\x18\x03 \x01(\x08\x12/\n\rconstrainedBy\x18\x04 \x01(\x0b\x32\x18.blox.DigitalConstraints\x12(\n\x0estrippedFields\x18\x63 \x03(\rB\x10\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x92?\x02\x10\x01:\x07\x8a\xb5\x18\x03\x18\xb2\x02\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,ActuatorDigital__pb2.DESCRIPTOR,DigitalConstraints__pb2.DESCRIPTOR,])




_ACTUATORPIN = _descriptor.Descriptor(
  name='ActuatorPin',
  full_name='blox.ActuatorPin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='blox.ActuatorPin.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\0020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invert', full_name='blox.ActuatorPin.invert', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='constrainedBy', full_name='blox.ActuatorPin.constrainedBy', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strippedFields', full_name='blox.ActuatorPin.strippedFields', index=3,
      number=99, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002(\001\222?\0028\020\222?\002\020\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\212\265\030\003\030\262\002'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=275,
)

_ACTUATORPIN.fields_by_name['state'].enum_type = ActuatorDigital__pb2._AD_STATE
_ACTUATORPIN.fields_by_name['constrainedBy'].message_type = DigitalConstraints__pb2._DIGITALCONSTRAINTS
DESCRIPTOR.message_types_by_name['ActuatorPin'] = _ACTUATORPIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActuatorPin = _reflection.GeneratedProtocolMessageType('ActuatorPin', (_message.Message,), dict(
  DESCRIPTOR = _ACTUATORPIN,
  __module__ = 'ActuatorPin_pb2'
  # @@protoc_insertion_point(class_scope:blox.ActuatorPin)
  ))
_sym_db.RegisterMessage(ActuatorPin)


_ACTUATORPIN.fields_by_name['state']._options = None
_ACTUATORPIN.fields_by_name['strippedFields']._options = None
_ACTUATORPIN._options = None
# @@protoc_insertion_point(module_scope)
