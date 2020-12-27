from typing import MutableMapping
from functions.transformations import *
import pandas as pd
import numpy as np
from datetime import datetime

def test_fullnameWithMiddle():
    firstname = "Bob"
    middlename = "George"
    lastname = "Gregory"
    assert create_fullName(firstname,lastname,middlename) == "Bob George Gregory"

def test_fullnameNoMiddle():
    firstname = "Bob"
    lastname = "Gregory"
    assert create_fullName(firstname,lastname) == "Bob Gregory"

def test_fullnameNoMiddleSpaces():
    firstname = "Bob"
    lastname = "Gregory"
    assert create_fullName(firstname,lastname).count(' ') == 1

def test_FullNameSpaces():
    firstname = "Bob"
    middlename = 'George'
    lastname = "Gregory"
    assert create_fullName(firstname,lastname, middlename).count(' ') == 2