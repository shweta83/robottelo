"""
Usage::

    hammer capsule [OPTIONS] SUBCOMMAND [ARG] ...

Parameters::

    SUBCOMMAND                    subcommand
    [ARG] ...                     subcommand arguments

Subcommands::

    content                       Manage the capsule content
    create                        Create a capsule
    delete                        Delete a capsule
    import-classes                Import puppet classes from puppet Capsule.
    info                          Show a capsule
    list                          List all capsules
    refresh-features              Refresh capsule features
    update                        Update a capsule
"""
from robottelo.cli.base import Base


class Capsule(Base):
    """
    Manipulates Foreman's capsule.
    """

    command_base = 'capsule'

    @classmethod
    def content_add_lifecycle_environment(cls, options):
        """Add lifecycle environments to the capsule."""

        cls.command_sub = 'content add-lifecycle-environment'

        return cls.execute(cls._construct_command(options), output_format='csv')

    @classmethod
    def content_available_lifecycle_environments(cls, options):
        """List the lifecycle environments not attached to the capsule."""

        cls.command_sub = 'content available-lifecycle-environments'

        return cls.execute(cls._construct_command(options), output_format='csv')

    @classmethod
    def content_info(cls, options):
        """Get current capsule synchronization status."""

        cls.command_sub = 'content info'

        return cls.execute(cls._construct_command(options), output_format='json')

    @classmethod
    def content_lifecycle_environments(cls, options):
        """List the lifecycle environments attached to the capsule."""

        cls.command_sub = 'content lifecycle-environments'

        return cls.execute(cls._construct_command(options), output_format='csv')

    @classmethod
    def content_remove_lifecycle_environment(cls, options):
        """Remove lifecycle environments from the capsule."""

        cls.command_sub = 'content remove-lifecycle-environment'

        return cls.execute(cls._construct_command(options), output_format='csv')

    @classmethod
    def content_synchronization_status(cls, options):
        """Get current capsule synchronization status."""

        cls.command_sub = 'content synchronization-status'

        return cls.execute(cls._construct_command(options), output_format='csv')

    @classmethod
    def content_synchronize(cls, options, return_raw_response=None, timeout=3600000):
        """Synchronize the content to the capsule."""

        cls.command_sub = 'content synchronize'

        return cls.execute(
            cls._construct_command(options),
            output_format='csv',
            ignore_stderr=True,
            return_raw_response=return_raw_response,
            timeout=timeout,
        )

    @classmethod
    def content_update_counts(cls, options):
        """Trigger content counts update."""

        cls.command_sub = 'content update-counts'

        return cls.execute(cls._construct_command(options), output_format='json')

    @classmethod
    def import_classes(cls, options):
        """Import puppet classes from puppet Capsule."""

        cls.command_sub = 'import-classes'

        return cls.execute(cls._construct_command(options), output_format='csv')

    @classmethod
    def refresh_features(cls, options):
        """Refresh capsule features."""

        cls.command_sub = 'refresh-features'

        return cls.execute(cls._construct_command(options), output_format='csv')
