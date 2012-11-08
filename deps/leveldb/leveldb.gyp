# Originally taken from the Chromium source leveldatabase.gyp, adapted & simplified for node-levelup

# Copyright (c) 2011 The LevelDB Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file. See the AUTHORS file for names of contributors.

{
  'target_defaults': {
    'defines': [
      'LEVELDB_PLATFORM_LIBUV=1',
      'USE_SNAPPY=1',
    ],
    'include_dirs': [
      'leveldb-1.5.0/',
      'leveldb-1.5.0/include/',
    ],
    'conditions': [
      ['OS == "win"', {
        'include_dirs': [
          'leveldb-1.5.0/port/win',
        ],
      }],
      ['OS == "linux"', {
        'defines': [
          'OS_LINUX=1',
        ],
        'CCFLAGS': [
          '-fno-builtin-memcmp',
          '-pthread',
          '-fPIC',
        ],
      }],
      ['OS == "solaris"', {
        'defines': [
          'OS_SOLARIS=1',
        ],
        'CCFLAGS': [
          '-fno-builtin-memcmp',
          '-pthread',
          '-fPIC',
        ],
      }],
      ['OS == "mac"', {
        'defines': [
          'OS_MACOSX=1',
        ],
        'CCFLAGS': [
          '-fno-builtin-memcmp',
          '-fPIC',
        ],
      }],
    ],
  },
  'targets': [
    {
      'target_name': 'leveldb',
      'type': 'static_library',
      'dependencies': [
        "../snappy/snappy.gyp:snappy",
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'leveldb-1.5.0/include/',
          'leveldb-1.5.0/',
        ],
        'conditions': [
          ['OS == "win"', {
            'include_dirs': [
              'leveldb-1.5.0/port/win',
            ],
          }],
        ],
      },
      'sources': [
        'leveldb-1.5.0/db/builder.cc',
        'leveldb-1.5.0/db/builder.h',
        'leveldb-1.5.0/db/db_impl.cc',
        'leveldb-1.5.0/db/db_impl.h',
        'leveldb-1.5.0/db/db_iter.cc',
        'leveldb-1.5.0/db/db_iter.h',
        'leveldb-1.5.0/db/filename.cc',
        'leveldb-1.5.0/db/filename.h',
        'leveldb-1.5.0/db/dbformat.cc',
        'leveldb-1.5.0/db/dbformat.h',
        'leveldb-1.5.0/db/log_format.h',
        'leveldb-1.5.0/db/log_reader.cc',
        'leveldb-1.5.0/db/log_reader.h',
        'leveldb-1.5.0/db/log_writer.cc',
        'leveldb-1.5.0/db/log_writer.h',
        'leveldb-1.5.0/db/memtable.cc',
        'leveldb-1.5.0/db/memtable.h',
        'leveldb-1.5.0/db/repair.cc',
        'leveldb-1.5.0/db/skiplist.h',
        'leveldb-1.5.0/db/snapshot.h',
        'leveldb-1.5.0/db/table_cache.cc',
        'leveldb-1.5.0/db/table_cache.h',
        'leveldb-1.5.0/db/version_edit.cc',
        'leveldb-1.5.0/db/version_edit.h',
        'leveldb-1.5.0/db/version_set.cc',
        'leveldb-1.5.0/db/version_set.h',
        'leveldb-1.5.0/db/write_batch.cc',
        'leveldb-1.5.0/db/write_batch_internal.h',
        'leveldb-1.5.0/helpers/memenv/memenv.cc',
        'leveldb-1.5.0/helpers/memenv/memenv.h',
        'leveldb-1.5.0/include/leveldb/cache.h',
        'leveldb-1.5.0/include/leveldb/comparator.h',
        'leveldb-1.5.0/include/leveldb/db.h',
        'leveldb-1.5.0/include/leveldb/env.h',
        'leveldb-1.5.0/include/leveldb/filter_policy.h',
        'leveldb-1.5.0/include/leveldb/iterator.h',
        'leveldb-1.5.0/include/leveldb/options.h',
        'leveldb-1.5.0/include/leveldb/slice.h',
        'leveldb-1.5.0/include/leveldb/status.h',
        'leveldb-1.5.0/include/leveldb/table.h',
        'leveldb-1.5.0/include/leveldb/table_builder.h',
        'leveldb-1.5.0/include/leveldb/write_batch.h',
        'leveldb-1.5.0/port/port.h',
        'leveldb-1.5.0/port/libuv/port_uv.cc',
        'leveldb-1.5.0/port/libuv/port_uv.h',
        'leveldb-1.5.0/table/block.cc',
        'leveldb-1.5.0/table/block.h',
        'leveldb-1.5.0/table/block_builder.cc',
        'leveldb-1.5.0/table/block_builder.h',
        'leveldb-1.5.0/table/filter_block.cc',
        'leveldb-1.5.0/table/filter_block.h',
        'leveldb-1.5.0/table/format.cc',
        'leveldb-1.5.0/table/format.h',
        'leveldb-1.5.0/table/iterator.cc',
        'leveldb-1.5.0/table/iterator_wrapper.h',
        'leveldb-1.5.0/table/merger.cc',
        'leveldb-1.5.0/table/merger.h',
        'leveldb-1.5.0/table/table.cc',
        'leveldb-1.5.0/table/table_builder.cc',
        'leveldb-1.5.0/table/two_level_iterator.cc',
        'leveldb-1.5.0/table/two_level_iterator.h',
        'leveldb-1.5.0/util/arena.cc',
        'leveldb-1.5.0/util/arena.h',
        'leveldb-1.5.0/util/bloom.cc',
        'leveldb-1.5.0/util/cache.cc',
        'leveldb-1.5.0/util/coding.cc',
        'leveldb-1.5.0/util/coding.h',
        'leveldb-1.5.0/util/comparator.cc',
        'leveldb-1.5.0/util/crc32c.cc',
        'leveldb-1.5.0/util/crc32c.h',
        'leveldb-1.5.0/util/env.cc',
        'leveldb-1.5.0/util/env_posix.cc',
        'leveldb-1.5.0/util/filter_policy.cc',
        'leveldb-1.5.0/util/hash.cc',
        'leveldb-1.5.0/util/hash.h',
        'leveldb-1.5.0/util/logging.cc',
        'leveldb-1.5.0/util/logging.h',
        'leveldb-1.5.0/util/mutexlock.h',
        'leveldb-1.5.0/util/options.cc',
        'leveldb-1.5.0/util/random.h',
        'leveldb-1.5.0/util/status.cc',
      ],
    },
  ],
}
