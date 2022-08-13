# util/__init__.py
# Copyright (C) 2005-2021 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: https://www.opensource.org/licenses/mit-license.php


from collections import defaultdict
from contextlib import contextmanager
from functools import partial
from functools import update_wrapper

from ._collections import coerce_generator_arg
from ._collections import coerce_to_immutabledict
from ._collections import collections_abc
from ._collections import column_dict
from ._collections import column_set
from ._collections import EMPTY_DICT
from ._collections import EMPTY_SET
from ._collections import FacadeDict
from ._collections import flatten_iterator
from ._collections import has_dupes
from ._collections import has_intersection
from ._collections import IdentitySet
from ._collections import ImmutableContainer
from ._collections import immutabledict
from ._collections import ImmutableProperties
from ._collections import LRUCache
from ._collections import ordered_column_set
from ._collections import OrderedDict
from ._collections import OrderedIdentitySet
from ._collections import OrderedProperties
from ._collections import OrderedSet
from ._collections import PopulateDict
from ._collections import Properties
from ._collections import ScopedRegistry
from ._collections import sort_dictionary
from ._collections import ThreadLocalRegistry
from ._collections import to_column_set
from ._collections import to_list
from ._collections import to_set
from ._collections import unique_list
from ._collections import UniqueAppender
from ._collections import update_copy
from ._collections import WeakPopulateDict
from ._collections import WeakSequence
from ._preloaded import preload_module
from ._preloaded import preloaded
from .compat import ABC
from .compat import arm
from .compat import b
from .compat import b64decode
from .compat import b64encode
from .compat import binary_type
from .compat import binary_types
from .compat import byte_buffer
from .compat import callable
from .compat import cmp
from .compat import cpython
from .compat import dataclass_fields
from .compat import decode_backslashreplace
from .compat import dottedgetter
from .compat import has_refcount_gc
from .compat import inspect_getfullargspec
from .compat import int_types
from .compat import iterbytes
from .compat import itertools_filter
from .compat import itertools_filterfalse
from .compat import local_dataclass_fields
from .compat import namedtuple
from .compat import next
from .compat import nullcontext
from .compat import osx
from .compat import parse_qsl
from .compat import perf_counter
from .compat import pickle
from .compat import print_
from .compat import py2k
from .compat import py37
from .compat import py38
from .compat import py39
from .compat import py3k
from .compat import pypy
from .compat import quote_plus
from .compat import raise_
from .compat import raise_from_cause
from .compat import reduce
from .compat import reraise
from .compat import string_types
from .compat import StringIO
from .compat import text_type
from .compat import threading
from .compat import timezone
from .compat import TYPE_CHECKING
from .compat import u
from .compat import ue
from .compat import unquote
from .compat import unquote_plus
from .compat import win32
from .compat import with_metaclass
from .compat import zip_longest
from .concurrency import asyncio
from .concurrency import await_fallback
from .concurrency import await_only
from .concurrency import greenlet_spawn
from .concurrency import is_exit_exception
from .deprecations import deprecated
from .deprecations import deprecated_20
from .deprecations import deprecated_20_cls
from .deprecations import deprecated_cls
from .deprecations import deprecated_params
from .deprecations import inject_docstring_text
from .deprecations import moved_20
from .deprecations import SQLALCHEMY_WARN_20
from .deprecations import warn_deprecated
from .deprecations import warn_deprecated_20
from .langhelpers import add_parameter_text
from .langhelpers import as_interface
from .langhelpers import asbool
from .langhelpers import asint
from .langhelpers import assert_arg_type
from .langhelpers import attrsetter
from .langhelpers import bool_or_str
from .langhelpers import chop_traceback
from .langhelpers import class_hierarchy
from .langhelpers import classproperty
from .langhelpers import clsname_as_plain_name
from .langhelpers import coerce_kw_type
from .langhelpers import constructor_copy
from .langhelpers import constructor_key
from .langhelpers import counter
from .langhelpers import create_proxy_methods
from .langhelpers import decode_slice
from .langhelpers import decorator
from .langhelpers import dictlike_iteritems
from .langhelpers import duck_type_collection
from .langhelpers import ellipses_string
from .langhelpers import EnsureKWArgType
from .langhelpers import format_argspec_init
from .langhelpers import format_argspec_plus
from .langhelpers import generic_repr
from .langhelpers import get_callable_argspec
from .langhelpers import get_cls_kwargs
from .langhelpers import get_func_kwargs
from .langhelpers import getargspec_init
from .langhelpers import has_compiled_ext
from .langhelpers import HasMemoized
from .langhelpers import hybridmethod
from .langhelpers import hybridproperty
from .langhelpers import iterate_attributes
from .langhelpers import map_bits
from .langhelpers import md5_hex
from .langhelpers import memoized_instancemethod
from .langhelpers import memoized_property
from .langhelpers import MemoizedSlots
from .langhelpers import method_is_overridden
from .langhelpers import methods_equivalent
from .langhelpers import monkeypatch_proxied_specials
from .langhelpers import NoneType
from .langhelpers import only_once
from .langhelpers import PluginLoader
from .langhelpers import portable_instancemethod
from .langhelpers import quoted_token_parser
from .langhelpers import safe_reraise
from .langhelpers import set_creation_order
from .langhelpers import string_or_unprintable
from .langhelpers import symbol
from .langhelpers import unbound_method_to_callable
from .langhelpers import walk_subclasses
from .langhelpers import warn
from .langhelpers import warn_exception
from .langhelpers import warn_limited
from .langhelpers import wrap_callable
