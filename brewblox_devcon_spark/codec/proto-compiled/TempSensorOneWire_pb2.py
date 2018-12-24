# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TempSensorOneWire.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TempSensorOneWire.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17TempSensorOneWire.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\xb2\x01\n\x11TempSensorOneWire\x12-\n\x05value\x18\x01 \x01(\x11\x42\x1e\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12\"\n\x06offset\x18\x03 \x01(\x11\x42\x12\x8a\xb5\x18\x02\x08\x02\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12\x17\n\x07\x61\x64\x64ress\x18\x04 \x01(\x06\x42\x06\x8a\xb5\x18\x02 \x01\x12(\n\x0estrippedFields\x18\x63 \x03(\rB\x10\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x92?\x02\x10\x01:\x07\x8a\xb5\x18\x03\x18\xae\x02\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])




_TEMPSENSORONEWIRE = _descriptor.Descriptor(
  name='TempSensorOneWire',
  full_name='blox.TempSensorOneWire',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='blox.TempSensorOneWire.value', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\0020\001\212\265\030\002\010\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='blox.TempSensorOneWire.offset', index=1,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\010\002\212\265\030\003\020\200 \222?\0028 '), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='blox.TempSensorOneWire.address', index=2,
      number=4, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002 \001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strippedFields', full_name='blox.TempSensorOneWire.strippedFields', index=3,
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
  serialized_options=_b('\212\265\030\003\030\256\002'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=242,
)

DESCRIPTOR.message_types_by_name['TempSensorOneWire'] = _TEMPSENSORONEWIRE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TempSensorOneWire = _reflection.GeneratedProtocolMessageType('TempSensorOneWire', (_message.Message,), dict(
  DESCRIPTOR = _TEMPSENSORONEWIRE,
  __module__ = 'TempSensorOneWire_pb2'
  # @@protoc_insertion_point(class_scope:blox.TempSensorOneWire)
  ))
_sym_db.RegisterMessage(TempSensorOneWire)


_TEMPSENSORONEWIRE.fields_by_name['value']._options = None
_TEMPSENSORONEWIRE.fields_by_name['offset']._options = None
_TEMPSENSORONEWIRE.fields_by_name['address']._options = None
_TEMPSENSORONEWIRE.fields_by_name['strippedFields']._options = None
_TEMPSENSORONEWIRE._options = None
# @@protoc_insertion_point(module_scope)
