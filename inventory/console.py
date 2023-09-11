#!/usr/bin/env python3
""" Console Module """
import cmd
import sys
from models import storage
from models.chemicals import Chemical
from models.locations import Location
from models.inventory import Inventory
from datetime import datetime


class InventoryCommand(cmd.Cmd):
    """Contains the functionality for the chemical inventory console"""

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    # all classes available in the db
    classes = {'Chemical': Chemical, 'Location': Location, 'Inventory': Inventory}

    # attributes allowed for additives
    chemical_attr = [
            'item_code', 'name', 'product_code', 'package_size',
            'manufacturer','expiry_date', 'batch_number'
            ]

    # attributes allowed for cement
    inventory_attr = [
            'location', 'chemical', 'no_of_sacks',
            'no_of_gal', 'no_of_drums'
            ]

    # attributes allowed for locations
    location_attr = ['name']

    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ Method to exit the console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_add(self, args):
        """ Create an object of any class"""

        # chec for invalid inputs
        if not args or ' ' in args or args not in self.classes:
            print("** invalid input **")
            print("enter <add Chemical, add Inventory or add Location>")
            return
        attr = {
                'Chemical': self.chemical_attr,
                'Location': self.location_attr,
                'Inventory': self.inventory_attr
                }

        floats = ['no_of_gal', 'no_of_sacks', 'no_of_drums', 'kg_per_sack']
       
        new = self.classes[args]()
        for att in attr[args]:
            value = ""
            while True:
                get = "(YYYY-MM-DD)" if att == "expiry_date" else ""
                value = input(f"    {att}{get}: ")
                try:
                    if att in floats:
                        value = float(value)
                    elif att == "expiry_date":
                        value = datetime.strptime(value, "%Y-%m-%d")
                    break
                except Exception as e:
                    print("Error: ", e)

            setattr(new, att, value)

        new.save()
        print()

    def help_add(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method to show an individual object """
        pass

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ Destroys a specified object """
        pass

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        pass

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        pass

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_update(self, args):
        """ Updates a certain object with new info """
        pass

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    InventoryCommand().cmdloop()
