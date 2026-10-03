"""Consolidated exception classes for es_mgmt.

All exceptions use ESMgmt prefix to prevent naming conflicts across submodules.
"""


class ESMgmtException(Exception):
    """Base exception for all es_mgmt errors."""


# Client exceptions
class ESMgmtConfigurationError(ESMgmtException):
    """Configuration validation or setup error."""


class ESMgmtConnectionError(ESMgmtException):
    """Error connecting to Elasticsearch."""


class ESMgmtNotMaster(ESMgmtConnectionError):
    """Error: connected to non-master node when master_only is True."""


class ESMgmtVersionError(ESMgmtException):
    """Error with Elasticsearch version."""


class ESMgmtSchemaValidationError(ESMgmtException):
    """Error validating configuration schema."""


class ESMgmtBuilderException(ESMgmtException):
    """Base exception for Builder errors."""


# Docker exceptions
class ESMgmtDockerException(ESMgmtException):
    """Base exception for Docker operations."""


class ESMgmtContainerError(ESMgmtDockerException):
    """Error with Docker container."""


class ESMgmtContainerNotFound(ESMgmtDockerException):
    """Container not found."""


class ESMgmtContainerRunningError(ESMgmtDockerException):
    """Container running error."""


# List actions
class ESMgmtActionError(ESMgmtException):
    """List action failed."""


# Reindex exceptions
class ESMgmtReindexException(ESMgmtException):
    """Base exception for reindex operations."""


class ESMgmtTaskNotFoundError(ESMgmtReindexException):
    """Task not found in Elasticsearch."""


class ESMgmtReindexError(ESMgmtReindexException):
    """Error during reindex operation."""


class ESMgmtTaskTimeoutError(ESMgmtReindexException):
    """Timeout waiting for task to complete."""


# Redact exceptions
class ESMgmtRedactException(ESMgmtException):
    """Base exception for redaction operations."""


class ESMgmtFatalError(ESMgmtRedactException):
    """Fatal error that should not be retried."""


class ESMgmtMissingIndex(ESMgmtRedactException):
    """Index not found."""


class ESMgmtRedactionError(ESMgmtRedactException):
    """Error during redaction."""


# Snapshot exceptions
class ESMgmtSnapshotException(ESMgmtException):
    """Base exception for snapshot operations."""


class ESMgmtRestoreError(ESMgmtSnapshotException):
    """Error during restore operation."""


class ESMgmtRepositoryError(ESMgmtSnapshotException):
    """Error related to snapshot repository."""


# Checkpoint exceptions
class ESMgmtCheckpointException(ESMgmtException):
    """Base exception for checkpoint tracking operations."""


class ESMgmtClientError(ESMgmtCheckpointException):
    """Error related to Elasticsearch client operations."""


class ESMgmtMissingDocument(ESMgmtCheckpointException):
    """Document not found in tracking index."""


# Wait exceptions
class ESMgmtWaitException(ESMgmtException):
    """Base exception for wait operations."""


class ESMgmtWaitFatal(ESMgmtWaitException):
    """Fatal error that should not be retried."""


class ESMgmtWaitTimeout(ESMgmtWaitException):
    """Timeout waiting for operation to complete."""


class ESMgmtExceptionCount(ESMgmtWaitException):
    """Too many exceptions raised."""


class ESMgmtIlmWaitError(ESMgmtWaitException):
    """Error during ILM phase/step wait."""
