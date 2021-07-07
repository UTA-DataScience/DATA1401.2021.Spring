#!/usr/bin/env python
ecl_dict = { 'nicholas boeker'  : 'student'
           , 'bradley bridges'  : 'student'
           , 'sagar dhana'      : 'student' 
           , 'travis driver'    : 'student'
           , 'eric gagliano'    : 'student'
           , 'christian garcia' : 'student'
           , 'matthew goree'    : 'student'
           , 'lucero herrera'   : 'student'
           , 'jake janssen'     : 'student'
           , 'michael langford' : 'student'
           , 'colin lewis'      : 'student'
           , 'mark loveland'    : 'student'
           , 'emilio mendiola'  : 'student'
           , 'kreshel nguyen'   : 'student'
           , 'russell philley'  : 'student'
           , 'caleb phillips'   : 'student'
           , 'joseph robbins'   : 'student'
           , 'bradley smith'    : 'student'
           , 'vivek varier'     : 'assistant'
           , 'amir shahmoradi'  : 'instructor'
           }
name = input("\n Please enter the full name of the person: ")
if name in ecl_dict:    # First make sure the name is in our dictionary
    if ecl_dict[name] == 'instructor':
        print( '\nThe name you enetered: {} belongs to the instructor of the ECL course. His office hours are Mondays 5-6 p.m.\n'.format(name) )
    elif ecl_dict[name] == 'assistant':
        print( '\nThe name you enetered: {} belongs to the Teaching Assistant of the ECL course. His office hours are Tuesdays 9-11 a.m.\n'.format(name) )
    elif ecl_dict[name] == 'student':
        print( '\nThe name you enetered: {} belongs to one of the amazing students in our class. You can certainly reach him during the weekly ECL classes on Wednesdays 9-10 a.m.\n'.format(name) )
else:
    print('\nThe name you entered: {} does not correspond to any real person in ECL class. Make sure you are not looking for a ghost, as our class is ghost-free.\n'.format(name) )