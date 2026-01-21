"""
-------------------------------------------------------
User class definition.
-------------------------------------------------------
Author: Ryan F

Defines the user class for the pyMQ backend
-------------------------------------------------------
"""

class user:
    """
    Defines an object for a single user, contains storage for name, username, wand ID and questfile
    
    """
    
    def __init__(self, name, username, wandID, questfile, currency, XP):
        """
        
        initialize a user into the pyMQ database
        Use: newUser = User(name, username, wandID, questfile, currency, XP)
        
        Parameters: 
            name - real name of user
            username - in-game username of user
            wandID - identifier of wand, pair with IR response to get this (TODO: learn how this shit works first)
            questfile - contains a copy of quest.csv with their username appended onto the name, this will contain quest progress
            currency - amount of ingame currency that this user possesses
            XP - amount of XP this user possesses
        
        """
        self.name  = name
        self.username = username
        self. wandID = wandID
        self.questfile = questfile
        self.currency = currency
        self.XP = XP
        return
    
    def __str__(self):
        """
        
        Tostring, shows values of user when printed
        
        """
        
        
        return (
        f"{'Name:':12}{self.name}\n"
        f"{'Username:':12}{self.username}\n"
        f"{'Wand ID:':12}{self.wandID}\n"
        f"{'questfile:':12}{self.questfile}"
        f"{'currency:':12}{self.currency}"
        f"{'xp:':12}{self.XP}"
        
        
        )
    
    def __hash__(self):
        """
        -------------------------------------------------------
        Generates a hash value from a user ingame name.
        Use: h = hash(source)
        -------------------------------------------------------
        Returns:
            value - the total of the characters in the name string (int > 0)
        -------------------------------------------------------
        """
        value = 0

        for c in self.username:
            value = value + ord(c)
        return value