# [[[fill git_describe()]]]
__version__ = '2023.10.7+parent.8f638cb1'
# [[[end]]] (checksum: d31a7e4fc048d9d235192794e33ee6a0)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
