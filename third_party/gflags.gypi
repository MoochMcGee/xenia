# Copyright 2013 Ben Vanik. All Rights Reserved.
{
  'targets': [
    {
      'target_name': 'gflags',
      'type': '<(library)',

      'direct_dependent_settings': {
        'conditions': [
          ['OS != "win"', {
            'include_dirs': [
              'gflags/src/',
            ],
          }],
          ['OS == "win"', {
            'include_dirs': [
              'gflags/src/windows/',
            ],
            'defines': [
              'GFLAGS_DLL_DECL=',
              'GFLAGS_DLL_DEFINE_FLAG=',
              'GFLAGS_DLL_DECLARE_FLAG=',
            ],
          }],
        ],
      },

      'sources': [
        'gflags/src/gflags.cc',
        'gflags/src/gflags_completions.cc',
        'gflags/src/gflags_nc.cc',
        'gflags/src/gflags_reporting.cc',
      ],

      'conditions': [
        ['OS != "win"', {
          'include_dirs': [
            'gflags/src/',
          ],
        }],
        ['OS == "win"', {
          'include_dirs': [
            'gflags/src/windows/',
            'gflags/src/',
          ],
          'sources+': [
            'gflags/src/windows/port.cc',
          ],
          'defines': [
            'PATH_SEPARATOR=\'\\\\\'',
            'GFLAGS_DLL_DECL=',
            'GFLAGS_DLL_DEFINE_FLAG=',
            'GFLAGS_DLL_DECLARE_FLAG=',
          ],
        }],
      ],
    }
  ]
}
