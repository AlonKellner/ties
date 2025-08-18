"""A CLI tool to duplicate and sync file content with advanced transformations."""

from ._file_processing import process_files
from ._version import __commit_id__, __version__, __version_tuple__
from .common_transforms import embed_environ

__all__ = [
    "__commit_id__",
    "__version__",
    "__version_tuple__",
    "embed_environ",
    "process_files",
]
