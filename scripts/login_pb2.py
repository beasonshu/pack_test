# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: login.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='login.proto',
    package='login',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b(
        '\n\x0blogin.proto\x12\x05login\"\x88\x01\n\x0c\x63l_login_req\x12\x15\n\rlogin_account\x18\x01 \x01(\t\x12\x12\n\nlogin_pass\x18\x02 \x01(\t\x12\x13\n\x0blogin_token\x18\x03 \x01(\t\x12\x12\n\nlogin_type\x18\x04 \x01(\r\x12\x13\n\x0bplatform_id\x18\x05 \x01(\t\x12\x0f\n\x07\x61rea_id\x18\x06 \x01(\r\"\x84\x01\n\x0cgt_login_ack\x12\r\n\x05\x65rror\x18\x01 \x01(\r\x12\x11\n\tclient_id\x18\x02 \x01(\r\x12\x15\n\rlogin_account\x18\x03 \x01(\t\x12\x12\n\nlogin_pass\x18\x04 \x01(\t\x12\x13\n\x0blogin_token\x18\x05 \x01(\t\x12\x12\n\nlogin_type\x18\x06 \x01(\rb\x06proto3')
)

_CL_LOGIN_REQ = _descriptor.Descriptor(
    name='cl_login_req',
    full_name='login.cl_login_req',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='login_account', full_name='login.cl_login_req.login_account', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='login_pass', full_name='login.cl_login_req.login_pass', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='login_token', full_name='login.cl_login_req.login_token', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='login_type', full_name='login.cl_login_req.login_type', index=3,
            number=4, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='platform_id', full_name='login.cl_login_req.platform_id', index=4,
            number=5, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='area_id', full_name='login.cl_login_req.area_id', index=5,
            number=6, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=23,
    serialized_end=159,
)

_GT_LOGIN_ACK = _descriptor.Descriptor(
    name='gt_login_ack',
    full_name='login.gt_login_ack',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='error', full_name='login.gt_login_ack.error', index=0,
            number=1, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='client_id', full_name='login.gt_login_ack.client_id', index=1,
            number=2, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='login_account', full_name='login.gt_login_ack.login_account', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='login_pass', full_name='login.gt_login_ack.login_pass', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='login_token', full_name='login.gt_login_ack.login_token', index=4,
            number=5, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='login_type', full_name='login.gt_login_ack.login_type', index=5,
            number=6, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=162,
    serialized_end=294,
)

DESCRIPTOR.message_types_by_name['cl_login_req'] = _CL_LOGIN_REQ
DESCRIPTOR.message_types_by_name['gt_login_ack'] = _GT_LOGIN_ACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

cl_login_req = _reflection.GeneratedProtocolMessageType('cl_login_req', (_message.Message,), {
    'DESCRIPTOR': _CL_LOGIN_REQ,
    '__module__': 'login_pb2'
    # @@protoc_insertion_point(class_scope:login.cl_login_req)
})
_sym_db.RegisterMessage(cl_login_req)

gt_login_ack = _reflection.GeneratedProtocolMessageType('gt_login_ack', (_message.Message,), {
    'DESCRIPTOR': _GT_LOGIN_ACK,
    '__module__': 'login_pb2'
    # @@protoc_insertion_point(class_scope:login.gt_login_ack)
})
_sym_db.RegisterMessage(gt_login_ack)

# @@protoc_insertion_point(module_scope)