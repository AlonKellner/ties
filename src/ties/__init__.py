"""A CLI tool to duplicate and sync file content with advanced transformations."""

from .__about__ import __version__, __version_tuple__
from ._file_processing import process_files
from .common_transforms import embed_environ

__all__ = [
    "__commit_id__",
    "__version__",
    "__version_tuple__",
    "embed_environ",
    "process_files",
]
