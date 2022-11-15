from git import Repo
from loguru import logger as Logger
import sys


class Manager():
    def __init__(self, logger: Logger, path_repository=None, origin='origin'):
        self.PREFIX_CLI = "pair/"
        self.origin = origin
        self.repository = Repo(path_repository, search_parent_directories=True)
        self.path_repository = path_repository
        self.logger = logger
        
    def _get_remote(self):
        return self.repository.remote(self.origin)

    def _safe_branch_checker(self):
        self.logger.debug(f"It's using the path: {self.path_repository}")
        self.logger.debug(
            f"It's working inside: {self.repository.working_tree_dir}")

        if self.PREFIX_CLI not in self.repository.active_branch.name:
            self.logger.error(
                "You need to be inside a pair/ branch before execute it."
            )
            return False
        return True

    def set_verbose(self, verbose: bool):
        if not verbose:
            self.logger.remove()
            self.logger.add(sys.stderr, level="INFO")

    def run_start(self):
        # Default origin remote
        self.logger.debug('Fetching data')

        if self.repository.active_branch.is_remote():
            self._get_remote().fetch()

        first_time = False

        # Only create a new branch if the current one hasn't the pair prefix
        if self.PREFIX_CLI not in self.repository.active_branch.name:
            first_time = True
            self.logger.debug("Creating branch")
            branch_name = self.PREFIX_CLI+self.repository.active_branch.name
            self.repository.git.checkout("-B", branch_name)
        else:
            self.logger.debug("Using same branch")
            branch_name = self.repository.active_branch.name

        if self.repository.active_branch.is_remote():
            self.logger.debug("Pulling")
            self._get_remote().pull(
                self.repository.active_branch.name
            )

        if len(self.repository.remotes):
            self.logger.debug("Pushing")
            self.repository.git.push(
                '--set-upstream', self._get_remote().name, branch_name)

        if first_time:
            self.logger.info(
                f"Done, branch '{branch_name}' created, happy pair programming 😄"
            )
        else:
            self.logger.info(f"Sync done, happy pair programming 😄")

    def run_next(self):
        is_safe = self._safe_branch_checker()
        if not is_safe:
            return

        self.logger.debug("Adding all the files")
        self.repository.git.add(A=True)

        if len(self.repository.index.diff("HEAD")) >= 1:
            self.logger.debug(
                "Commiting with pair default message, skipping the hooks")
            self.repository.git.commit(
                '-m', 'pair - [skip-cli]', '--no-verify')
        else:
            self.logger.debug("Nothing to commit.")

        if self.repository.active_branch.is_remote():
            self.logger.debug("Pushing")
            self.repository.git.push(
                '--set-upstream', self._get_remote().name, self.repository.active_branch.name)

    def run_done(self):
        is_safe = self._safe_branch_checker()
        if not is_safe:
            return

        # To keep the origin updated
        self.run_next()

        pair_branch = self.repository.active_branch.name
        branch_without_prefix = self.repository.active_branch.name.replace(
            self.PREFIX_CLI, ""
        )

        self.logger.debug("Coming back to the original branch")
        self.repository.git.checkout(branch_without_prefix)

        if self.repository.active_branch.is_remote():
            self.logger.debug("Fetching and pulling the data")
            self._get_remote().fetch()
            self._get_remote().pull()

        self.logger.debug("Merging with the pair branch")
        self.repository.git.merge(pair_branch, no_ff=True, no_commit=True)

        if self.origin in self.repository.remotes:
            for ref in self.repository.remotes[self.origin].refs:
                if pair_branch not in ref.name:
                    continue

                self.logger.debug("Deleting pair branch from the remote environment")

                self.repository.git.push(
                    self._get_remote().name,
                    '--delete',
                    pair_branch
                )

        if pair_branch in self.repository.heads:
            self.logger.debug("Deleting pair branch from the local environment")
            self.repository.heads[pair_branch].delete(
                self.repository, pair_branch, force=True)

        self.logger.info("🌟 Done, continue with the git commit command.")
