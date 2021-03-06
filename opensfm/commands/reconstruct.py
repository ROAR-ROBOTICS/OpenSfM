from . import command
from opensfm.actions import reconstruct


class Command(command.CommandBase):
    name = 'reconstruct'
    help = "Compute the reconstruction"

    def run_impl(self, dataset, args):
        reconstruct.run_dataset(dataset)

    def add_arguments_impl(self, parser):
        pass
